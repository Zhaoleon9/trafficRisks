# Driving Risk Evaluation System

A weather-based driving risk assessment tool that evaluates potential driving risks based on current snow precipitation and wind speed conditions.

## Overview

This application uses fuzzy logic to analyze current weather conditions and historical climate data to provide a risk assessment for driving. It is specifically designed for Sault Ste. Marie but can be adapted for other locations.

## Installation

Install required packages:
  ```
  pip install customtkinter numpy pandas scikit-fuzzy requests
  ```


## Usage

### Running the Application

Navigate to the source directory and run the user interface script:

> Do not run it in your VScode intergrated terminal. Run it in a independent terminal outside the vscode.

```
cd src
python user_gui.py
```

The application will:

1. Fetch current weather data for Sault Ste. Marie
2. Display the current snow precipitation and wind speed
3. Allow you to modify these values if needed
4. Calculate and display the driving risk as a percentage

## Interpreting Results

0-30%: Low driving risk
30-70%: Moderate driving risk
70-100%: High driving risk

## Testing

```
cd test
python test_fuzzy_logic.py
python test_climate_data_analysis.py
python test_request_weather_info.py
```