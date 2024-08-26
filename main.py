import requests
from twilio.rest import Client
import os

# OPEN WEATHER API 
OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "PUT YOUR API KEY FROM OPEN WEATHER API HERE"

# TWILIO 
account_sid = "PUT YOUR ACCOUNT SID FROM TWILIO HERE"
auth_token = "PUT YOUR AUTH TOKEN FROM TWILIO HERE"

# THIS WEATHER PARAMS ARE SET FOR WARSAW
weather_params = {
    "lat": 52.229675,
    "lon": 21.012230,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OMW_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code =  hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messsSages.create(
        body="It's going to rain today. Remember to bring an umbrella ☔.",
        from_="PUT 'FROM PHONE NUMBER' HERE, FIND IT ON TWILIO PROJECT",
        to="PUT 'TO PHONE NUMBER' HERE, FIND IT ON TWILIO PROJCECT"
    )

    print(message.status)
