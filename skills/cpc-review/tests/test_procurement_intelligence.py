import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from common import fy_quarter, calc_landed_unit_rate, stable_id
from compare_history import flag_for_variance


class ProcurementIntelligenceTests(unittest.TestCase):
    def test_financial_year_quarter(self):
        self.assertEqual(fy_quarter("2026-04-01"), ("2026-27", "Q1"))
        self.assertEqual(fy_quarter("2026-09-11"), ("2026-27", "Q2"))
        self.assertEqual(fy_quarter("2027-02-10"), ("2026-27", "Q4"))

    def test_landed_rate(self):
        q = {"base_unit_rate":100,"gst_percent":18,"freight_per_unit":5,"installation_per_unit":2,"other_per_unit":1,"discount_per_unit":3}
        self.assertAlmostEqual(calc_landed_unit_rate(q), 122.46, places=2)

    def test_stable_id(self):
        self.assertEqual(stable_id("VEND", "Vendor A"), stable_id("VEND", " vendor-a "))

    def test_variance_flags_are_review_signals(self):
        cfg = {"variance_flags_percent":{"review":10,"high":20,"critical":30}}
        self.assertEqual(flag_for_variance(5, cfg), "WITHIN_HISTORY_BAND")
        self.assertEqual(flag_for_variance(12, cfg), "REVIEW")
        self.assertEqual(flag_for_variance(25, cfg), "HIGH_REVIEW")
        self.assertEqual(flag_for_variance(35, cfg), "CRITICAL_REVIEW")
        self.assertEqual(flag_for_variance(None, cfg), "NO_BENCHMARK")

if __name__ == "__main__":
    unittest.main()
