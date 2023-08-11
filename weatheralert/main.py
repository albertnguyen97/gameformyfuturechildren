import requests

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/weather"

api_key = "50f74eeba210e987ac07455825d40484"

weather_params = {
    "lat": 21.027763,
    "lon": 105.834160,
    "appid": api_key
}

response = requests.get(OWN_Endpoint, params=weather_params)

data_weather = response.json()
if data_weather["weather"][0]["main"] == "Rain":
    print("Rain!!")