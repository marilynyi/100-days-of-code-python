import requests
import pandas as pd
import config
from twilio.rest import Client

# As of June 2023, the free tier of OpenWeather includes only one forecast: 3-hour Forecast 5 days
# We adapt the 12-hour hourly forecast in the assignment to forecast every 3 hours for the next 12 hrs


API_KEY = config.api_key
TWILIO_NUMBER = config.twilio_number
VERIFIED_NUMBER = config.verified_number
ACCOUNT_SID = config.account_sid
AUTH_TOKEN = config.auth_token
LAT = config.lat
LON = config.lon
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "lat": LAT,
    "lon": LON,
    "units": "imperial",
    "appid": API_KEY,
}

# Pull from OpenWeather 3-hour forecast API
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
print(response.status_code)

# View pprint structure on jsonviewer.stack.hu
weather_data = response.json()

will_rain = False

weather_slice = weather_data["list"][:5]
# print(weather_slice)

# Rain condition is ID < 700
# Source: https://openweathermap.org/weather-conditions

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
                        .create(
                            body="It's going to rain today. Remember to bring an ☔️",
                            from_=TWILIO_NUMBER,
                            to=VERIFIED_NUMBER
                        )
    print(message.status)
        