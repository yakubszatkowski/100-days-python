# API Authentication, Sending SMS, Environment Variables
import os
import requests
from twilio.rest import Client

account_sid = 'AC02bf2822bb9d5f8590efac3d1ef0ee4a'
auth_token = os.environ.get('D35_sms_auth_token')

api_key = os.environ.get('D35_api_key')  # didn't use because key need verification that takes couple hours
angela_key = '69f04e4613056b159c2761a9d9e664d2'
onecall_api_key = 'b239ad6816f4e09d41069588e7ac2d80'
LAT = 50.31
LON = 19.07
# Site to view json of weather in my city (Czeladź)
# https://api.openweathermap.org/data/2.5/weather?lat=50.31&lon=19.07&appid=8502980a28e764d307f29c248c637b32
# https://api.openweathermap.org/data/2.5/onecall?lat=50.31&lon=19.07&appid=b239ad6816f4e09d41069588e7ac2d80
# Wrong API results in 401 code means - unauthorized

parameters = {
    'lat': LAT,
    'lon': LON,
    'appid': onecall_api_key,
    'exclude': 'current,minutely,daily'
}
# Url below is API endpoint
response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
weather_data = response.json()['hourly']

# Will it be raining in next 12 hours?
will_rain = False
for data in weather_data[:12]:
    if data['weather'][0]['id'] < 700:
        will_rain = True

# Sending sms
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to='+48737168406',
        from_='+19705121521',
        body='Weź parasolkę ☂')
    print(message.status)
