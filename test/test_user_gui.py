"""
Module Purpose: Tests the GUI interface
Author: Xicheng Yin, 249508610, xyin@algomau.ca; Parth Sathiya, 259662610, psathiya@algomau.ca
Date: 2025-03-15
"""
import unittest
from src.user_gui import RiskAssessmentApp


class TestUI(unittest.TestCase):
    """Unit tests for the GUI interface."""

    def test_ui_display(self):
        """Test if the GUI interface is displayed correctly"""
        app = RiskAssessmentApp()

        # verify the default values are not empty
        self.assertNotEqual(app.entry_snow.get(), "") 
        self.assertNotEqual(app.entry_wind.get(), "")

        # verify the title is displayed
        self.assertIn("Driving Risk Evaluation", app.label_title._text)

        app.destroy()

    def test_ui_interaction(self):
        """Test if the user input is interacted correctly"""
        app = RiskAssessmentApp()

        # clear the default values and set new values
        app.entry_snow.delete(0, 'end')
        app.entry_snow.insert(0, "1.5")

        app.entry_wind.delete(0, 'end')
        app.entry_wind.insert(0, "25")

        # simulate the button click
        app.evaluate_risk()

        # verify the result is updated
        self.assertIn("Risk Evaluation Results", app.label_result._text)

        app.destroy()


if __name__ == "__main__":
    unittest.main()
