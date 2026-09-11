#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import statistics
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

from common import DATA_DIR, load_aliases, load_config, normalize_item, parse_float, read_csv


def months_between(a: str, b: str) -> int:
    da = datetime.fromisoformat(a[:10])
    db = datetime.fromisoformat(b[:10])
    return abs((da.year - db.year) * 12 + da.month - db.month)


def flag_for_variance(pct: float | None, config: Dict[str, Any]) -> str:
    if pct is None:
        return "NO_BENCHMARK"
    levels = config["variance_flags_percent"]
    ap = abs(pct)
    if ap >= levels["critical"]:
        return "CRITICAL_REVIEW"
    if ap >= levels["high"]:
        return "HIGH_REVIEW"
    if ap >= levels["review"]:
        return "REVIEW"
    return "WITHIN_HISTORY_BAND"


def compare_record(record: Dict[str, Any], data_dir: Path) -> Dict[str, Any]:
    config = load_config(data_dir)
    aliases = load_aliases(data_dir)
    history = read_csv(data_dir / "master_item_history.csv")
    current_date = record.get("procurement_date") or record.get("review_date")
    current_state = record.get("state", "")
    result = {
        "procurement_reference": record.get("procurement_reference", ""),
        "state": current_state,
        "project_unit": record.get("project_unit", ""),
        "history_months": config["history_months"],
        "items": []
    }

    for raw in record.get("items", []):
        item = normalize_item(raw, aliases)
        current_rate = parse_float(
            (raw.get("award") or {}).get("awarded_landed_unit_rate")
            or raw.get("responsive_l1_landed_unit_rate")
            or raw.get("current_landed_unit_rate")
        )
        matches: List[Dict[str, str]] = []
        for h in history:
            if config.get("use_only_benchmark_eligible_awards", True) and h.get("benchmark_eligible") != "Y":
                continue
            if h.get("normalized_item_name", "").strip().lower() != item["normalized_item_name"].strip().lower():
                continue
            if config.get("require_same_canonical_unit", True) and h.get("canonical_unit") != item["canonical_unit"]:
                continue
            h_spec = h.get("specification_key") or "UNSPECIFIED"
            if config.get("require_same_specification_key", True):
                if item["specification_key"] != "UNSPECIFIED" and h_spec != item["specification_key"]:
                    continue
                if item["specification_key"] == "UNSPECIFIED" and not config.get("allow_unspecified_specification", True):
                    continue
            if current_date and h.get("procurement_date") and months_between(current_date, h["procurement_date"]) > int(config["history_months"]):
                continue
            matches.append(h)

        same_state = [m for m in matches if m.get("state") == current_state]
        preferred = same_state if same_state and config.get("same_state_first", True) else matches
        rates = [parse_float(m.get("awarded_landed_unit_rate")) for m in preferred if parse_float(m.get("awarded_landed_unit_rate")) > 0]
        all_rates = [parse_float(m.get("awarded_landed_unit_rate")) for m in matches if parse_float(m.get("awarded_landed_unit_rate")) > 0]
        latest = sorted(preferred, key=lambda r: r.get("procurement_date", ""), reverse=True)[0] if preferred else None
        median = statistics.median(rates) if rates else None
        mean = statistics.mean(rates) if rates else None
        min_rate = min(rates) if rates else None
        max_rate = max(rates) if rates else None
        latest_rate = parse_float(latest.get("awarded_landed_unit_rate")) if latest else None
        variance_median = ((current_rate - median) / median * 100) if current_rate and median else None
        variance_latest = ((current_rate - latest_rate) / latest_rate * 100) if current_rate and latest_rate else None
        confidence = "HIGH" if item["specification_key"] != "UNSPECIFIED" and len(rates) >= 2 else ("MEDIUM" if rates else "LOW")

        result["items"].append({
            "item_id": item["item_id"],
            "normalized_item_name": item["normalized_item_name"],
            "canonical_unit": item["canonical_unit"],
            "specification_key": item["specification_key"],
            "current_landed_unit_rate": current_rate or None,
            "same_state_comparable_count": len(same_state),
            "all_state_comparable_count": len(matches),
            "benchmark_basis": "same_state" if same_state and preferred is same_state else "all_DSC_states",
            "latest_comparable_rate": latest_rate,
            "latest_comparable_date": latest.get("procurement_date") if latest else None,
            "latest_comparable_state": latest.get("state") if latest else None,
            "median_rate": median,
            "mean_rate": mean,
            "min_rate": min_rate,
            "max_rate": max_rate,
            "all_state_median_rate": statistics.median(all_rates) if all_rates else None,
            "variance_vs_median_percent": round(variance_median, 2) if variance_median is not None else None,
            "variance_vs_latest_percent": round(variance_latest, 2) if variance_latest is not None else None,
            "variance_flag": flag_for_variance(variance_median, config),
            "comparison_confidence": confidence,
            "interpretation_note": "Variance flag triggers CPC review only; confirm specification, quantity, freight, installation, tax, geography and timing before judging price."
        })
    return result


def markdown_report(comp: Dict[str, Any]) -> str:
    lines = ["# CPC Historical Price Comparison", "", f"Procurement: {comp.get('procurement_reference','')}", f"State/Unit: {comp.get('state','')} / {comp.get('project_unit','')}", ""]
    for i in comp["items"]:
        lines += [
            f"## {i['normalized_item_name']}",
            f"- Current landed unit rate: {i['current_landed_unit_rate']}",
            f"- Comparable records: {i['all_state_comparable_count']} (same state: {i['same_state_comparable_count']})",
            f"- Benchmark basis: {i['benchmark_basis']}",
            f"- Latest comparable rate: {i['latest_comparable_rate']} ({i['latest_comparable_date'] or 'n/a'})",
            f"- Historical median: {i['median_rate']}",
            f"- Historical range: {i['min_rate']} to {i['max_rate']}",
            f"- Variance vs median: {i['variance_vs_median_percent']}%" if i['variance_vs_median_percent'] is not None else "- Variance vs median: not available",
            f"- Review flag: **{i['variance_flag']}**",
            f"- Confidence: {i['comparison_confidence']}",
            f"- Note: {i['interpretation_note']}",
            ""
        ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare a new CPC review record against historical finalized award benchmarks.")
    parser.add_argument("record")
    parser.add_argument("--data-dir", default=str(DATA_DIR))
    parser.add_argument("--json-output")
    parser.add_argument("--markdown-output")
    args = parser.parse_args()
    with open(args.record, "r", encoding="utf-8") as f:
        record = json.load(f)
    comp = compare_record(record, Path(args.data_dir))
    text = json.dumps(comp, indent=2, ensure_ascii=False)
    print(text)
    if args.json_output:
        Path(args.json_output).write_text(text + "\n", encoding="utf-8")
    if args.markdown_output:
        Path(args.markdown_output).write_text(markdown_report(comp), encoding="utf-8")

if __name__ == "__main__":
    main()
