import requests

API_KEY = "983a2ee7861b6ff5340840f66b2c033a"  # openweather key
CITY = "Sault Ste. Marie"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

wind_speed = data["wind"]["speed"]  # wind speed
snow_precipitation = data.get("snow", {}).get("1h", 0)  # snow precipitation

print(f"Wind speed: {wind_speed} km/h, snow precipitation: {snow_precipitation}%")

/**
* Read and analysis the historical snow precipitation and wind speed
* 
*/
import pandas as pd
import numpy as np



