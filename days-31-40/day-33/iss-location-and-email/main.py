import requests
import datetime as dt
from pytz import timezone
import smtplib
import time
import config

CITY_LAT = config.lat
CITY_LNG = config.lng

MY_EMAIL = config.email
PASSWORD = config.app_password

def is_iss_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])

    if (CITY_LAT - 5) <= iss_lat <= (CITY_LAT + 5) and (CITY_LNG - 5) <= iss_lng <= (CITY_LNG + 5):
        return True

def is_night():
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

    time_utc = str(dt.datetime.now(timezone('UTC')).replace(microsecond=0)).replace("+00:00","")
    time_utc = dt.datetime.strptime(time_utc, "%Y-%m-%d %H:%M:%S")
    time_mt = time_utc.astimezone(timezone('US/Mountain')).replace(tzinfo=None)
    time_mt = time_mt - dt.timedelta(hours=6)

    if time_mt >= sunset_mt or time_mt <= sunrise_mt:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, 
                            to_addrs=MY_EMAIL,
                            msg="Subject:Look Up!\n\nThe ISS is above you in the sky."
                            )

