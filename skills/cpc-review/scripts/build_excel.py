#!/usr/bin/env python3
"""Build the analyst-facing Excel register from Git-versioned CSV source tables.

Uses artifact_tool in ChatGPT/Work. CSV remains fully usable if artifact_tool is unavailable elsewhere.
"""
from __future__ import annotations
import csv
from pathlib import Path
from artifact_tool import SpreadsheetFile, Workbook

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUTPUT = ROOT / "outputs" / "CPC_Master_Procurement_Register.xlsx"
SHEETS = [
    ("Procurement Reviews", "procurement_reviews.csv"),
    ("Item Quotes", "item_quotes.csv"),
    ("Awards", "awards.csv"),
    ("Master Item History", "master_item_history.csv"),
    ("Item Catalog", "item_catalog.csv"),
    ("Vendors", "vendors.csv"),
    ("Item Aliases", "item_aliases.csv"),
]

def read_rows(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.reader(f))

def main():
    wb = Workbook.create()
    d = wb.worksheets.add("Dashboard")
    d.merge_cells("A1:H1")
    d.get_range("A1").values = [["DSC CPC Procurement Intelligence Register"]]
    d.get_range("A1:H1").format = {"fill":"#1F4E78","font":{"bold":True,"color":"#FFFFFF","size":16},"horizontal_alignment":"center","vertical_alignment":"center","row_height":28}
    d.get_range("A3:B7").values = [["KPI","Value"],["CPC reviews",0],["Vendor quote rows",0],["Finalized awards",0],["Benchmark-eligible awards",0]]
    d.get_range("A3:B3").format = {"fill":"#D9EAF7","font":{"bold":True},"horizontal_alignment":"center"}
    d.get_range("D3:F7").values = [["Historical comparison","Meaning","CPC use"],["WITHIN_HISTORY_BAND","<10% variance","Normal review"],["REVIEW",">=10%","Check reasons"],["HIGH_REVIEW",">=20%","Seek stronger validation"],["CRITICAL_REVIEW",">=30%","Validate thoroughly; not an automatic rejection"]]
    d.get_range("D3:F3").format = {"fill":"#D9EAF7","font":{"bold":True},"horizontal_alignment":"center"}
    d.get_range("D3:F7").format.wrap_text = True
    d.get_range("D:F").format.column_width = 24
    d.merge_cells("A9:H12")
    d.get_range("A9").values = [["CSV files are the source of truth. This workbook is generated for analysis. Historical rates are benchmark signals only; CPC must confirm specification, unit, quantity, freight, installation, tax, geography and timing before judging price."]]
    d.get_range("A9:H12").format.wrap_text = True
    counts = {}
    for sheet_name, csv_name in SHEETS:
        rows = read_rows(DATA / csv_name)
        sh = wb.worksheets.add(sheet_name)
        if rows:
            sh.get_range_by_indexes(0,0,len(rows),len(rows[0])).values = rows
            sh.get_range_by_indexes(0,0,1,len(rows[0])).format = {"fill":"#5B9BD5","font":{"bold":True,"color":"#FFFFFF"},"wrap_text":True,"vertical_alignment":"center"}
            sh.freeze_panes.freeze_rows(1)
            sh.get_range_by_indexes(0,0,max(len(rows),2),len(rows[0])).format.wrap_text = True
            sh.get_range_by_indexes(0,0,max(len(rows),2),len(rows[0])).format.autofit_columns()
        counts[csv_name] = max(len(rows)-1,0)
    d.get_range("B4:B6").values = [[counts["procurement_reviews.csv"]],[counts["item_quotes.csv"]],[counts["awards.csv"]]]
    awards = read_rows(DATA / "awards.csv")
    benchmark_count = 0
    if len(awards) > 1:
        idx = awards[0].index("benchmark_eligible")
        benchmark_count = sum(1 for r in awards[1:] if len(r) > idx and r[idx] == "Y")
    d.get_range("B7").values = [[benchmark_count]]
    d.get_range("A3:B7").format.autofit_columns()
    OUTPUT.parent.mkdir(exist_ok=True)
    SpreadsheetFile.export_xlsx(wb).save(str(OUTPUT))
    print(OUTPUT)

if __name__ == "__main__":
    main()
