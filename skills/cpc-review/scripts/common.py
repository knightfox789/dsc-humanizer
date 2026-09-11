from __future__ import annotations

import csv
import hashlib
import json
import re
from datetime import date, datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"

PROCUREMENT_FIELDS = ["procurement_id","review_date","procurement_date","financial_year","quarter","state","project_unit","district","project_name","funding_partner","procurement_category","procurement_reference","approved_budget_value","currency","proposed_vendor","proposed_amount","cpc_verdict","final_status","price_reasonableness_status","source_reference","record_hash","last_updated"]
QUOTE_FIELDS = ["quote_id","procurement_id","item_id","original_item_description","normalized_item_name","item_category","specification","specification_key","quantity","quoted_unit","canonical_unit","vendor_id","vendor_name","quote_date","base_unit_rate","gst_percent","freight_per_unit","installation_per_unit","other_per_unit","discount_per_unit","landed_unit_rate","evaluated_total","responsiveness","numerical_rank","responsive_rank","negotiated","negotiated_landed_unit_rate","source_document","benchmark_reference_only","last_updated"]
AWARD_FIELDS = ["award_id","procurement_id","item_id","normalized_item_name","item_category","specification","specification_key","canonical_unit","awarded_quantity","vendor_id","vendor_name","award_date","awarded_base_unit_rate","gst_percent","freight_per_unit","installation_per_unit","other_per_unit","awarded_landed_unit_rate","award_total","currency","cpc_verdict","final_status","benchmark_eligible","benchmark_exclusion_reason","source_reference","last_updated"]
ITEM_FIELDS = ["item_id","normalized_item_name","item_category","canonical_unit","specification_key","standard_specification","active","notes","last_updated"]
VENDOR_FIELDS = ["vendor_id","vendor_name","vendor_name_normalized","states_served","gstin_optional","pan_optional","active","notes","last_updated"]
MASTER_FIELDS = ["award_id","procurement_id","procurement_date","financial_year","quarter","state","project_unit","funding_partner","procurement_reference","item_id","normalized_item_name","item_category","specification_key","canonical_unit","awarded_quantity","vendor_id","vendor_name","awarded_base_unit_rate","gst_percent","freight_per_unit","installation_per_unit","other_per_unit","awarded_landed_unit_rate","award_total","currency","cpc_verdict","benchmark_eligible","source_reference"]


def utc_today() -> str:
    return date.today().isoformat()


def normalize_text(value: Any) -> str:
    text = str(value or "").strip().lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def stable_id(prefix: str, *values: Any) -> str:
    payload = "|".join(normalize_text(v) for v in values)
    digest = hashlib.sha1(payload.encode("utf-8")).hexdigest()[:12].upper()
    return f"{prefix}-{digest}"


def record_hash(record: Dict[str, Any]) -> str:
    payload = json.dumps(record, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def parse_float(value: Any, default: float = 0.0) -> float:
    if value in (None, ""):
        return default
    if isinstance(value, (int, float)):
        return float(value)
    cleaned = str(value).replace(",", "").replace("₹", "").strip()
    try:
        return float(cleaned)
    except ValueError:
        return default


def bool_flag(value: Any) -> bool:
    return str(value or "").strip().lower() in {"y","yes","true","1","approved","finalized","finalised"}


def fy_quarter(date_text: str, start_month: int = 4) -> Tuple[str, str]:
    d = datetime.fromisoformat(date_text[:10]).date()
    fy_start = d.year if d.month >= start_month else d.year - 1
    financial_year = f"{fy_start}-{str(fy_start + 1)[-2:]}"
    shifted = (d.month - start_month) % 12
    quarter = f"Q{shifted // 3 + 1}"
    return financial_year, quarter


def read_csv(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, fields: List[str], rows: Iterable[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fields})


def upsert(rows: List[Dict[str, Any]], row: Dict[str, Any], key: str) -> List[Dict[str, Any]]:
    found = False
    output = []
    for existing in rows:
        if existing.get(key) == row.get(key):
            merged = dict(existing)
            merged.update({k: v for k, v in row.items() if v not in (None, "")})
            output.append(merged)
            found = True
        else:
            output.append(existing)
    if not found:
        output.append(row)
    return output


def load_config(data_dir: Path = DATA_DIR) -> Dict[str, Any]:
    with (data_dir / "comparison_config.json").open("r", encoding="utf-8") as f:
        return json.load(f)


def calc_landed_unit_rate(quote: Dict[str, Any]) -> float:
    base = parse_float(quote.get("base_unit_rate"))
    gst = parse_float(quote.get("gst_percent"))
    freight = parse_float(quote.get("freight_per_unit"))
    install = parse_float(quote.get("installation_per_unit"))
    other = parse_float(quote.get("other_per_unit"))
    discount = parse_float(quote.get("discount_per_unit"))
    return round((base - discount) * (1 + gst / 100.0) + freight + install + other, 4)


def load_aliases(data_dir: Path = DATA_DIR) -> Dict[str, Dict[str, str]]:
    aliases = {}
    for row in read_csv(data_dir / "item_aliases.csv"):
        key = normalize_text(row.get("alias"))
        if key:
            aliases[key] = row
    return aliases


def normalize_item(item: Dict[str, Any], aliases: Dict[str, Dict[str, str]]) -> Dict[str, Any]:
    result = dict(item)
    original = item.get("original_item_description") or item.get("item_name") or item.get("normalized_item_name") or ""
    alias = aliases.get(normalize_text(original))
    if alias:
        result.setdefault("normalized_item_name", alias.get("normalized_item_name"))
        result.setdefault("item_category", alias.get("item_category"))
        result.setdefault("canonical_unit", alias.get("canonical_unit"))
    result["normalized_item_name"] = (result.get("normalized_item_name") or original).strip()
    result["item_category"] = (result.get("item_category") or "Unclassified").strip()
    result["canonical_unit"] = (result.get("canonical_unit") or result.get("unit") or result.get("quoted_unit") or "UNSPECIFIED").strip()
    result["specification_key"] = (result.get("specification_key") or "UNSPECIFIED").strip()
    result["specification"] = (result.get("specification") or "").strip()
    result["item_id"] = result.get("item_id") or stable_id("ITEM", result["normalized_item_name"], result["canonical_unit"], result["specification_key"])
    return result
