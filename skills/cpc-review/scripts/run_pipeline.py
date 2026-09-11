#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
OUTPUTS = ROOT / "outputs"


def run(cmd):
    print("+", " ".join(str(x) for x in cmd))
    subprocess.run([str(x) for x in cmd], check=True)


def main():
    p = argparse.ArgumentParser(description="CPC procurement intelligence pipeline")
    p.add_argument("record")
    p.add_argument("--finalize", action="store_true", help="Append/update master data after CPC review is finalized")
    p.add_argument("--skip-excel", action="store_true")
    args = p.parse_args()
    OUTPUTS.mkdir(exist_ok=True)
    comparison_json = OUTPUTS / "latest_history_comparison.json"
    comparison_md = OUTPUTS / "latest_history_comparison.md"
    run([sys.executable, SCRIPTS / "compare_history.py", args.record, "--json-output", comparison_json, "--markdown-output", comparison_md])
    if args.finalize:
        run([sys.executable, SCRIPTS / "update_master.py", args.record])
        if not args.skip_excel:
            run([sys.executable, SCRIPTS / "build_excel.py"])
    else:
        print("Historical comparison completed. Master data not changed because --finalize was not supplied.")

if __name__ == "__main__":
    main()
