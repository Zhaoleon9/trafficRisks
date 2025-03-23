"""
Module Purpose: Tests for the fuzzy logic risk assessment system 
Author: Boyuan Zhang, 249454830, bzhang@algomau.ca; Parth Patel, 249452120, ppatel@algomau.ca
Date: 2025-03-22
"""
import unittest
from src.fuzzy_logic import myFuzzy


class TestFuzzyLogic(unittest.TestCase):
    """Unit tests for the fuzzy logic risk assessment system."""

    def test_low_risk(self):
        """Test case: Low snowfall and low wind should yield a low risk."""
        risk = myFuzzy(2, 0.1)
        self.assertGreaterEqual(risk, 0)
        self.assertLessEqual(risk, 30)

    def test_moderate_risk(self):
        """Test case: Moderate snowfall and moderate wind should yield a moderate risk."""
        risk = myFuzzy(10, 0.5)
        self.assertGreaterEqual(risk, 30)
        self.assertLessEqual(risk, 70)

    def test_high_risk(self):
        """Test case: High snowfall and high wind should yield a high risk."""
        risk = myFuzzy(30, 1.0)
        self.assertGreaterEqual(risk, 70)
        self.assertLessEqual(risk, 100)

    def test_extreme_snow(self):
        """Test case: Extreme snowfall should trigger high risk."""
        risk = myFuzzy(5, 15)
        self.assertGreaterEqual(risk, 70)

    def test_extreme_wind(self):
        """Test case: Extreme wind should trigger high risk."""
        risk = myFuzzy(50, 0.3)
        self.assertGreaterEqual(risk, 70)

    def test_invalid_input(self):
        """Test case: Negative values should return -1."""
        risk = myFuzzy(-1, -1)
        self.assertEqual(risk, -1)

    def test_boundary_conditions(self):
        """Test boundary conditions"""
        # zero value test
        self.assertGreaterEqual(myFuzzy(
            0, 0), 0, "Zero value input should return a valid risk value")

        # minimum value test
        self.assertGreaterEqual(myFuzzy(
            0.1, 0.1), 0, "Minimum value input should return a valid risk value")

        # maximum value test
        self.assertGreaterEqual(myFuzzy(
            100, 20), 0, "Maximum value input should return a valid risk value")

        # negative value test
        self.assertEqual(myFuzzy(-1, 0), -1,
                         "Negative value input should return -1")
        self.assertEqual(myFuzzy(0, -1), -1,
                         "Negative value input should return -1")

        print("Boundary conditions test passed!")


if __name__ == "__main__":
    unittest.main()
