# root/tests/test_subnet.py
"""Regression tests for IPv4 usable host calculation."""
import importlib.util
import pathlib
import unittest


MODULE_PATH = pathlib.Path(__file__).resolve().parents[1] / "subnet-calculator-simple.py"
spec = importlib.util.spec_from_file_location("subnet_calculator_simple", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class SubnetTests(unittest.TestCase):
    def test_regular_24(self):
        rows = module.subnet_details_for("192.0.2.10", 24)
        self.assertIn("192.0.2.1", rows[2])
        self.assertIn("192.0.2.254", rows[3])
        self.assertTrue(rows[4].endswith("254"))

    def test_point_to_point_31(self):
        rows = module.subnet_details_for("192.0.2.10", 31)
        self.assertIn("192.0.2.10", rows[2])
        self.assertIn("192.0.2.11", rows[3])
        self.assertTrue(rows[4].endswith("2"))

    def test_single_host_32(self):
        rows = module.subnet_details_for("192.0.2.10", 32)
        self.assertIn("192.0.2.10", rows[2])
        self.assertIn("192.0.2.10", rows[3])
        self.assertTrue(rows[4].endswith("1"))

    def test_bad_prefix(self):
        self.assertFalse(module.validate_cidr("33"))
        self.assertFalse(module.validate_cidr("invalid"))


if __name__ == "__main__":
    unittest.main()
