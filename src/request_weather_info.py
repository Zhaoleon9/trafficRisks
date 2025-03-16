import requests

class Weather:
    API_KEY = "983a2ee7861b6ff5340840f66b2c033a"  # openweather key
    CITY = "Sault Ste. Marie"
    def __init__(self, city ="", api_key =""):
        
        if city=="":
            self.city = Weather.CITY
        else:
            self.city = city
        if api_key=="":
            self.api_key = Weather.API_KEY
        else:
            self.api_key = api_key
        
        self.url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric"
    
        try:
            self.response = requests.get(self.url)
            self.data = self.response.json()
            if not isinstance(self.data, (dict, list)):
                raise ValueError("Invalid JSON format: Expected dict or list.")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {self.url}: {e}")
            self.data = None
        except ValueError as e:
            print(f"Error parsing JSON response: {e}")
            self.data = None

    def get_wind_speed(self):
        try:
            return self.data.get("wind", {}).get("speed", 0)
        except (AttributeError, TypeError) as e:
            return 0

    def get_snow_precipitation(self):
        try:
            return self.data.get("snow", {}).get("1h", 0)
        except (AttributeError, TypeError) as e:
            return 0

def main():
    weather = Weather()
    print(f"Wind speed: {weather.get_wind_speed()} km/h, snow precipitation: {weather.get_snow_precipitation()} mm")
    #print(f"snow: 0: {weather.get_snow_(0)}, 0.25: {weather.get_snow_precipitation(0.25)}, 0.5: {weather.get_snow_precipitation(0.5)}, 0.75: {weather.get_snow_precipitation(0.75)}, 1: {weather.get_snow_precipitation(1)}" )

if __name__ == "__main__":
    main()
