"""
Module Purpose: Computes the driving risk based on snow precipitation and wind speed 
wind speed and snow precipitation 
Author: Lin Zhao, 249416700, lizhao@algomau.ca
Date: 2025-03-22
"""
import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl

# Define risk ranges for snow and wind speed, then get memberships
# value from historycal data
# the numbers below are adjusted from results
SNOW_PER_S_A, SNOW_PER_S_B, SNOW_PER_S_C = 0.0, 0.25, 0.3
SNOW_PER_M_A, SNOW_PER_M_B, SNOW_PER_M_C = 0.3, 0.5, 0.9
SNOW_PER_H_A, SNOW_PER_H_B, SNOW_PER_H_C = 0.95, 1, 1
IGNORE_ZERO_SNOW = True

WIND_PER_S_A, WIND_PER_S_B, WIND_PER_S_C = 0.0, 0.0, 0.5
WIND_PER_M_A, WIND_PER_M_B, WIND_PER_M_C = 0.3, 0.5, 0.7
WIND_PER_H_A, WIND_PER_H_B, WIND_PER_H_C = 0.6, 1, 1
# reference numbers
# snow-> 0: 0.1, 0.25: 0.2, 0.5: 0.3, 0.75: 0.725, 1: 9.3 -> 
# wind-> 0: 0.0, 0.25: 7.0, 0.5: 11.0, 0.75: 16.0, 1: 36.0 -> 0,7,11; 7,

TRAFFIC_RISKS_S_A, TRAFFIC_RISKS_S_B, TRAFFIC_RISKS_S_C = 0, 0, 20
TRAFFIC_RISKS_M_A, TRAFFIC_RISKS_M_B, TRAFFIC_RISKS_M_C = 10, 40, 60
TRAFFIC_RISKS_H_A, TRAFFIC_RISKS_H_B, TRAFFIC_RISKS_H_C = 50, 100, 100

def myFuzzy(windSpeed, snowPrecip):
    """
    Computes the driving risk based on snow precipitation and wind speed
    """
    if (windSpeed < 0) or (snowPrecip < 0):
        return -1
    # Define fuzzy variables
    snow = ctrl.Antecedent(np.arange(0, 10, 0.1), "snow")
    wind = ctrl.Antecedent(np.arange(0, 36, 1), "wind")
    risk = ctrl.Consequent(np.arange(0, 101, 1), "risk")

    # Get historical climate data
    from climate_data_analysis import ClimateData
    cd = ClimateData()

    # Define fuzzy membership functions for snow
    snow["low"] = fuzz.trimf(snow.universe, [0, 0, 3])
    snow["moderate"] = fuzz.trimf(snow.universe, [2, 5, 8])
    snow["high"] = fuzz.trimf(snow.universe, [7, 10, 10])
    # Define fuzzy membership functions for wind speed
    wind["low"] = fuzz.trimf(wind.universe, [0, 0,  cd.get_wind_proportion(WIND_PER_S_C)])
    wind["moderate"] = fuzz.trimf(wind.universe, [cd.get_wind_proportion(WIND_PER_M_A), cd.get_wind_proportion(WIND_PER_M_B), cd.get_wind_proportion(WIND_PER_M_C)])
    wind["high"] = fuzz.trimf(wind.universe, [cd.get_wind_proportion(WIND_PER_H_A), 36, 36])

    # Define fuzzy membership functions for risk
    risk["low"] = fuzz.trimf(risk.universe, [TRAFFIC_RISKS_S_A, TRAFFIC_RISKS_S_B, TRAFFIC_RISKS_S_C])
    risk["moderate"] = fuzz.trimf(risk.universe, [TRAFFIC_RISKS_M_A, TRAFFIC_RISKS_M_B, TRAFFIC_RISKS_M_C])
    risk["high"] = fuzz.trimf(risk.universe, [TRAFFIC_RISKS_H_A, TRAFFIC_RISKS_H_B, TRAFFIC_RISKS_H_C])

    # Define fuzzy rules
    # defines rule for risk "high" - if snow or wind is high
    rule_high = ctrl.Rule(wind["high"] | snow["high"], risk["high"])
    # defines rule for risk "moderate" - if snow or wind is moderate and not high
    rule_moderate = ctrl.Rule((wind["moderate"] | snow["moderate"]) & ~(wind["high"] | snow["high"]), risk["moderate"])
    # defines rule for risk "low" - if snow and wind is low
    rule_low = ctrl.Rule(~(wind["high"] | snow["high"] | wind["moderate"] | snow["moderate"]), risk["low"])

    # Create fuzzy control system
    risk_ctrl = ctrl.ControlSystem([rule_high, rule_moderate, rule_low])
    risk_simulation = ctrl.ControlSystemSimulation(risk_ctrl)

    # Set input values
    risk_simulation.input["snow"] = snowPrecip
    risk_simulation.input["wind"] = windSpeed

    # Compute fuzzy logic result
    try:
        risk_simulation.compute()
        risk_value = risk_simulation.output.get('risk', -1)
        return risk_value
    except Exception:
        return -1  # Return -1 in case of an error

def main():
    """
    Testing
    """
    from climate_data_analysis import ClimateData
    cd = ClimateData()
    # for i in range(0, 101, 5):
    #     print(f"{i}% Snow precipitation: {cd.get_snow_proportion(i/100):.2f}-> {i}% Wind Speed: {cd.get_wind_proportion(i/100):.2f}")
    print("-" * 80)
    for i in range(0, 201, 20):
        for j in range(1, 41, 5):
            print(f"Snow: {i/10} mm, Wind: {j} km/h -> Risk: {myFuzzy(j, i/10):.2f}%")
    print(myFuzzy(50, 0.3))
    print(f"Snow: {1} mm, Wind: {1} km/h -> Risk: {myFuzzy(1, 1):.2f}%")
if __name__ == "__main__":
    main()