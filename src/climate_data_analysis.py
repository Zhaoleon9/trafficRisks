"""
Module Purpose: Fetch historical climate data and offer functions for getting 
wind speed and snow precipitation 
Author: Lin Zhao, 249416700, lizhao@algomau.ca
Date: 2025-03-15
"""
import pandas as pd
import numpy as py  # Typo: should be `np` instead of `py`
import os

class ClimateData:
    """Handle historical climate data analysis, such as wind speed and precipitation."""

    HISTORIC_CLIMATE_DATA = f"../historical data/climate_hourly_SaultSteMarie.csv"
    CHARSET = f"ISO-8859-1"
    WIND_COL = f"Wind Spd (km/h)"
    SNOW_COL = f"Precip. Amount (mm)"
    
    # Get the absolute path of historical dataset
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
    FILE_PATH = os.path.join(BASE_DIR, HISTORIC_CLIMATE_DATA)

    def __init__(self):
        """Initializes ClimateData by reading a CSV file."""
        # Read the climate data file into a DataFrame
        try:
            self.cd = pd.read_csv(ClimateData.FILE_PATH, encoding = ClimateData.CHARSET)
        except Exception as e:
            print("Can not open file:", ClimateData.FILE_PATH, e)

    def get_wind_speed(self):
        """Gets the wind speed column from the dataset.

        Returns:
            pandas.Series: Wind speed values.
        """
        return self.cd[ClimateData.WIND_COL]
    
    def get_snow_precip(self):
        """Gets the snowfall precipitation column from the dataset.

        Returns:
            pandas.Series: Snowfall precipitation values.
        """
        return self.cd[ClimateData.SNOW_COL]
    
    def get_wind_proportion(self, portion):
        """Calculates a wind speed quantile.

        Args:
            portion (float): A value between 0 and 1 representing the quantile.

        Returns:
            float: The wind speed value at the given quantile, or 0 if input is invalid.
        """
        if portion <= 1 and portion >= 0:
            return self.cd[ClimateData.WIND_COL].quantile(portion)
        else:
            return 0

    def get_snow_proportion(self, portion, remove_zero=True):
        """Calculates a snow precipitation quantile.

        Args:
            portion (float): A value between 0 and 1 representing the quantile.
            remove_zero (bool, optional): If True, ignores zero snowfall values. Defaults to True.

        Returns:
            float: The snowfall value at the given quantile, or 0 if input is invalid.
        """
        if remove_zero and portion <= 1 and portion >= 0:
            return self.cd[self.cd[ClimateData.SNOW_COL] > 0][ClimateData.SNOW_COL].quantile(portion)
        elif not remove_zero:
            return self.cd[ClimateData.SNOW_COL].quantile(portion)
        else:
            return 0

def main():
    """for testing"""
    cliData = ClimateData()

    # Print wind and snow quantile values
    print(cliData.get_wind_proportion(0.12))
    print(cliData.get_snow_proportion(0.90, False))
    print(f"snow-> 0: {cliData.get_snow_proportion(0, False)}, 0.25: {cliData.get_snow_proportion(0.25, False)}, "
          f"0.5: {cliData.get_snow_proportion(0.5, False)}, 0.75: {cliData.get_snow_proportion(0.75)}, "
          f"1: {cliData.get_snow_proportion(1)}")
    print(f"wind-> 0: {cliData.get_wind_proportion(0)}, 0.25: {cliData.get_wind_proportion(0.25)}, "
          f"0.5: {cliData.get_wind_proportion(0.5)}, 0.75: {cliData.get_wind_proportion(0.75)}, "
          f"1: {cliData.get_wind_proportion(1)}")

if __name__ == "__main__":
    main()
