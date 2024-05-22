import requests
from twilio.rest import Client

OWM_URL = 'http://api.openweathermap.org/data/2.5/forecast'
API_KEY = "3ca248996ffd7afcb72533875d5a3cbd"
account_sid = "AC55d29c322eef608c27b7c26bcb1be6e8"
auth_token = 'bf7bb5876323747f8fdce999b379e8fe'
lat = -7.112330
lng = 107.883890
client = Client(account_sid, auth_token)

weather_params = {
    "lat": lat,
    "lon": lng,
    "appid": API_KEY,
    "cnt": 4,
}

will_rain = True
response = requests.get(OWM_URL, params=weather_params)
response.raise_for_status()
data = response.json()
print(data['list'][0]['weather'][0]['id'])
for hour_data in data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = False
if will_rain :
    message = client.messages.create(
        body="Hujan Bang, Tolong Bawa Payung",
        from_='+12097216352',
        to='+6289699501548'
    )
    print(message.status)
