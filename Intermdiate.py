import requests
from langchain.tools import tool

@tool
def weather_tool(city: str) -> str:
    """Fetches current weather for a given city using Open-Meteo API."""
    try:
        # Pehle city -> latitude/longitude find karne ke liye Open-Meteo geocoding API
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        geo_resp = requests.get(geo_url).json()
        if "results" not in geo_resp:
            return "City not found."
        
        lat = geo_resp["results"][0]["latitude"]
        lon = geo_resp["results"][0]["longitude"]

        # Weather API call
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_resp = requests.get(weather_url).json()
        temp = weather_resp["current_weather"]["temperature"]
        wind = weather_resp["current_weather"]["windspeed"]

        return f"🌡 Temperature: {temp}°C | 💨 Wind Speed: {wind} km/h"
    except Exception as e:
        return f"Error: {str(e)}"

# 🔹 Test
print(weather_tool.run("pune"))
