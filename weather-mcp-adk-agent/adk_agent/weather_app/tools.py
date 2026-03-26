import requests

def get_weather(city: str):
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geo = requests.get(geo_url).json()

    if "results" not in geo:
        return {"error": "City not found"}

    lat = geo["results"][0]["latitude"]
    lon = geo["results"][0]["longitude"]

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    data = requests.get(weather_url).json()

    return data["current_weather"]


def get_calendar():
    return {
        "9AM": "busy",
        "11AM": "free",
        "2PM": "free",
        "4PM": "busy",
        "6PM": "free"
    }
