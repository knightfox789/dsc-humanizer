#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict

from common import (
    AWARD_FIELDS, DATA_DIR, ITEM_FIELDS, MASTER_FIELDS, PROCUREMENT_FIELDS, QUOTE_FIELDS, VENDOR_FIELDS,
    bool_flag, calc_landed_unit_rate, fy_quarter, load_aliases, normalize_item, normalize_text, parse_float,
    read_csv, record_hash, stable_id, upsert, utc_today, write_csv
)

APPROVED_STATUSES = {"approved", "finalized", "finalised", "closed-approved", "order-issued"}


def require(record: Dict[str, Any], path: str) -> None:
    cur: Any = record
    for part in path.split("."):
        if not isinstance(cur, dict) or cur.get(part) in (None, ""):
            raise ValueError(f"Missing required field: {path}")
        cur = cur[part]


def rebuild_master(data_dir: Path) -> None:
    procurements = {r["procurement_id"]: r for r in read_csv(data_dir / "procurement_reviews.csv")}
    rows = []
    for award in read_csv(data_dir / "awards.csv"):
        p = procurements.get(award.get("procurement_id"), {})
        row = {k: award.get(k, "") for k in MASTER_FIELDS}
        for k in ["procurement_date","financial_year","quarter","state","project_unit","funding_partner","procurement_reference"]:
            row[k] = p.get(k, "")
        rows.append(row)
    write_csv(data_dir / "master_item_history.csv", MASTER_FIELDS, rows)


def process_record(record: Dict[str, Any], data_dir: Path, dry_run: bool = False) -> Dict[str, Any]:
    for field in ["review_date", "state", "project_unit", "procurement_reference", "cpc_verdict", "final_status"]:
        require(record, field)
    if not isinstance(record.get("items"), list) or not record["items"]:
        raise ValueError("At least one item is required")

    today = utc_today()
    procurement_date = record.get("procurement_date") or record["review_date"]
    fy, q = fy_quarter(procurement_date)
    procurement_id = record.get("procurement_id") or stable_id(
        "PROC", record.get("state"), record.get("project_unit"), record.get("procurement_reference"), procurement_date
    )
    aliases = load_aliases(data_dir)
    final_status = str(record.get("final_status") or "").strip().lower()
    approved = final_status in APPROVED_STATUSES

    procurement_row = {
        "procurement_id": procurement_id,
        "review_date": record["review_date"],
        "procurement_date": procurement_date,
        "financial_year": record.get("financial_year") or fy,
        "quarter": record.get("quarter") or q,
        "state": record.get("state", ""),
        "project_unit": record.get("project_unit", ""),
        "district": record.get("district", ""),
        "project_name": record.get("project_name", ""),
        "funding_partner": record.get("funding_partner", ""),
        "procurement_category": record.get("procurement_category", ""),
        "procurement_reference": record.get("procurement_reference", ""),
        "approved_budget_value": record.get("approved_budget_value", ""),
        "currency": record.get("currency", "INR"),
        "proposed_vendor": record.get("proposed_vendor", ""),
        "proposed_amount": record.get("proposed_amount", ""),
        "cpc_verdict": record.get("cpc_verdict", ""),
        "final_status": record.get("final_status", ""),
        "price_reasonableness_status": record.get("price_reasonableness_status", ""),
        "source_reference": record.get("source_reference", ""),
        "record_hash": record_hash(record),
        "last_updated": today,
    }

    proc_rows = upsert(read_csv(data_dir / "procurement_reviews.csv"), procurement_row, "procurement_id")
    item_rows = read_csv(data_dir / "item_catalog.csv")
    vendor_rows = read_csv(data_dir / "vendors.csv")
    quote_rows = [r for r in read_csv(data_dir / "item_quotes.csv") if r.get("procurement_id") != procurement_id]
    award_rows = [r for r in read_csv(data_dir / "awards.csv") if r.get("procurement_id") != procurement_id]

    stats = {"procurement_id": procurement_id, "items": 0, "quotes": 0, "awards": 0, "benchmark_awards": 0}

    for item_raw in record["items"]:
        item = normalize_item(item_raw, aliases)
        stats["items"] += 1
        item_rows = upsert(item_rows, {
            "item_id": item["item_id"],
            "normalized_item_name": item["normalized_item_name"],
            "item_category": item["item_category"],
            "canonical_unit": item["canonical_unit"],
            "specification_key": item["specification_key"],
            "standard_specification": item.get("specification", ""),
            "active": "Y",
            "notes": item.get("notes", ""),
            "last_updated": today,
        }, "item_id")

        for rank_index, quote in enumerate(item.get("quotes", []), start=1):
            vendor_name = (quote.get("vendor_name") or "").strip()
            if not vendor_name:
                raise ValueError(f"Missing vendor_name for item {item['normalized_item_name']}")
            vendor_id = quote.get("vendor_id") or stable_id("VEND", vendor_name)
            vendor_rows = upsert(vendor_rows, {
                "vendor_id": vendor_id,
                "vendor_name": vendor_name,
                "vendor_name_normalized": normalize_text(vendor_name),
                "states_served": quote.get("states_served", record.get("state", "")),
                "gstin_optional": quote.get("gstin_optional", ""),
                "pan_optional": quote.get("pan_optional", ""),
                "active": "Y",
                "notes": quote.get("vendor_notes", ""),
                "last_updated": today,
            }, "vendor_id")
            landed = parse_float(quote.get("landed_unit_rate")) or calc_landed_unit_rate(quote)
            quantity = parse_float(item.get("quantity"))
            quote_id = quote.get("quote_id") or stable_id("QUOTE", procurement_id, item["item_id"], vendor_id)
            quote_rows.append({
                "quote_id": quote_id,
                "procurement_id": procurement_id,
                "item_id": item["item_id"],
                "original_item_description": item_raw.get("original_item_description") or item_raw.get("item_name") or item["normalized_item_name"],
                "normalized_item_name": item["normalized_item_name"],
                "item_category": item["item_category"],
                "specification": item.get("specification", ""),
                "specification_key": item["specification_key"],
                "quantity": quantity,
                "quoted_unit": quote.get("quoted_unit") or item_raw.get("unit") or item["canonical_unit"],
                "canonical_unit": item["canonical_unit"],
                "vendor_id": vendor_id,
                "vendor_name": vendor_name,
                "quote_date": quote.get("quote_date", ""),
                "base_unit_rate": quote.get("base_unit_rate", ""),
                "gst_percent": quote.get("gst_percent", ""),
                "freight_per_unit": quote.get("freight_per_unit", ""),
                "installation_per_unit": quote.get("installation_per_unit", ""),
                "other_per_unit": quote.get("other_per_unit", ""),
                "discount_per_unit": quote.get("discount_per_unit", ""),
                "landed_unit_rate": landed,
                "evaluated_total": round(landed * quantity, 2) if quantity else quote.get("evaluated_total", ""),
                "responsiveness": quote.get("responsiveness", "Not assessed"),
                "numerical_rank": quote.get("numerical_rank", rank_index),
                "responsive_rank": quote.get("responsive_rank", ""),
                "negotiated": "Y" if bool_flag(quote.get("negotiated")) else "N",
                "negotiated_landed_unit_rate": quote.get("negotiated_landed_unit_rate", ""),
                "source_document": quote.get("source_document", ""),
                "benchmark_reference_only": "Y" if bool_flag(quote.get("benchmark_reference_only")) else "N",
                "last_updated": today,
            })
            stats["quotes"] += 1

        award = item.get("award") or {}
        if award:
            vendor_name = (award.get("vendor_name") or "").strip()
            vendor_id = award.get("vendor_id") or stable_id("VEND", vendor_name)
            if vendor_name:
                vendor_rows = upsert(vendor_rows, {
                    "vendor_id": vendor_id,
                    "vendor_name": vendor_name,
                    "vendor_name_normalized": normalize_text(vendor_name),
                    "states_served": record.get("state", ""),
                    "active": "Y",
                    "last_updated": today,
                }, "vendor_id")
            benchmark_eligible = approved and bool_flag(award.get("approved", True)) and bool_flag(award.get("benchmark_eligible", True))
            landed = parse_float(award.get("awarded_landed_unit_rate"))
            if not landed:
                landed = calc_landed_unit_rate({
                    "base_unit_rate": award.get("awarded_base_unit_rate"),
                    "gst_percent": award.get("gst_percent"),
                    "freight_per_unit": award.get("freight_per_unit"),
                    "installation_per_unit": award.get("installation_per_unit"),
                    "other_per_unit": award.get("other_per_unit"),
                    "discount_per_unit": award.get("discount_per_unit"),
                })
            qty = parse_float(award.get("awarded_quantity") or item.get("quantity"))
            award_id = award.get("award_id") or stable_id("AWARD", procurement_id, item["item_id"], vendor_id)
            award_rows.append({
                "award_id": award_id,
                "procurement_id": procurement_id,
                "item_id": item["item_id"],
                "normalized_item_name": item["normalized_item_name"],
                "item_category": item["item_category"],
                "specification": item.get("specification", ""),
                "specification_key": item["specification_key"],
                "canonical_unit": item["canonical_unit"],
                "awarded_quantity": qty,
                "vendor_id": vendor_id,
                "vendor_name": vendor_name,
                "award_date": award.get("award_date") or procurement_date,
                "awarded_base_unit_rate": award.get("awarded_base_unit_rate", ""),
                "gst_percent": award.get("gst_percent", ""),
                "freight_per_unit": award.get("freight_per_unit", ""),
                "installation_per_unit": award.get("installation_per_unit", ""),
                "other_per_unit": award.get("other_per_unit", ""),
                "awarded_landed_unit_rate": landed,
                "award_total": round(landed * qty, 2) if qty else award.get("award_total", ""),
                "currency": record.get("currency", "INR"),
                "cpc_verdict": record.get("cpc_verdict", ""),
                "final_status": record.get("final_status", ""),
                "benchmark_eligible": "Y" if benchmark_eligible else "N",
                "benchmark_exclusion_reason": "" if benchmark_eligible else (award.get("benchmark_exclusion_reason") or "Not finalized/approved for benchmark use"),
                "source_reference": record.get("source_reference", ""),
                "last_updated": today,
            })
            stats["awards"] += 1
            stats["benchmark_awards"] += int(benchmark_eligible)

    if not dry_run:
        write_csv(data_dir / "procurement_reviews.csv", PROCUREMENT_FIELDS, proc_rows)
        write_csv(data_dir / "item_catalog.csv", ITEM_FIELDS, item_rows)
        write_csv(data_dir / "vendors.csv", VENDOR_FIELDS, vendor_rows)
        write_csv(data_dir / "item_quotes.csv", QUOTE_FIELDS, quote_rows)
        write_csv(data_dir / "awards.csv", AWARD_FIELDS, award_rows)
        rebuild_master(data_dir)
    return stats


def main() -> None:
    parser = argparse.ArgumentParser(description="Append/upsert a finalized CPC review record into the master CSV data layer.")
    parser.add_argument("record", help="Path to review_record.json")
    parser.add_argument("--data-dir", default=str(DATA_DIR))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    with open(args.record, "r", encoding="utf-8") as f:
        record = json.load(f)
    stats = process_record(record, Path(args.data_dir), args.dry_run)
    print(json.dumps(stats, indent=2))

if __name__ == "__main__":
    main()
