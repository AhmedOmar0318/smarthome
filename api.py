# service/api.py
import requests

def haal_weer_op(lat=52.0907, lon=5.1214):

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "temperature_unit": "celsius",
        "windspeed_unit": "ms"
    }


    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        current = data.get("current_weather", {})
        if not current:
            print("Geen actuele weerdata beschikbaar.")
            return None

        temperatuur = current.get("temperature")

        return temperatuur

    except requests.RequestException as e:
        print(f"Fout bij ophalen van weerdata: {e}")
        return None
