import requests
import os
import sys

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"{city}: {data['main']['temp']}°C, {data['weather'][0]['description']}")
    else:
        print(f"Failed to get weather: {response.status_code}, {response.text}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python weather.py <city>")
        sys.exit(1)
    get_weather(sys.argv[1])

###Project ##
