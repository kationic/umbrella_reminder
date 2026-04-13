import requests
from twilio.rest import Client
import os

LATITUDE = 51.588187
LONGITUDE = -0.042389
API_KEY = os.environ.get("OPENWEATHER_API_KEY") 
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
INTERVAL = 4
ACCOUNT_SID= os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN= os.environ.get("TWILIO_AUTH_TOKEN")
MY_NUMBER= os.environ.get("MY_PHONE_NUMBER")

PARAMS = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "cnt": INTERVAL
}

response = requests.get(OWM_ENDPOINT, params=PARAMS)
response.raise_for_status()

weather_data = response.json()

count=0
will_rain = False
for instance in weather_data["list"]:
    if instance["weather"][0]["id"] <700:
        will_rain = True
    else:
        continue
    count += 1

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        from_="+447426933513",
        to=MY_NUMBER,
        body = "Bring an ☂️ today!"
    )
    print(message.sid)
