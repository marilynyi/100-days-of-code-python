import requests
import datetime as dt
from pytz import timezone

CITY_LAT = 39.863510
CITY_LNG = -105.041122

parameters = {
    "lat": CITY_LAT,
    "lng": CITY_LNG,
    "formatted": 0 # 1 is default
}    

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise_utc = data["results"]["sunrise"].replace("T"," ").replace("+00:00","")
sunrise_utc = dt.datetime.strptime(sunrise_utc, "%Y-%m-%d %H:%M:%S")
sunrise_mt = sunrise_utc.astimezone(timezone('US/Mountain')).replace(tzinfo=None)
sunrise_mt = sunrise_mt - dt.timedelta(hours=6)

sunset_utc = data["results"]["sunset"].replace("T"," ").replace("+00:00","")
sunset_utc = dt.datetime.strptime(sunset_utc, "%Y-%m-%d %H:%M:%S")
sunset_mt = sunset_utc.astimezone(timezone('US/Mountain')).replace(tzinfo=None)
sunset_mt = sunset_mt - dt.timedelta(hours=6)

print(f"Sunrise (MT): {sunrise_mt}")
print(f"Sunset (MT): {sunset_mt}")

time_utc = str(dt.datetime.now(timezone('UTC')).replace(microsecond=0)).replace("+00:00","")
time_utc = dt.datetime.strptime(time_utc, "%Y-%m-%d %H:%M:%S")
time_mt = time_utc.astimezone(timezone('US/Mountain')).replace(tzinfo=None)
time_mt = time_mt - dt.timedelta(hours=6)

print(f"Current (MT): {time_mt}")

