import requests
from vonage import Auth, Vonage
from vonage_sms import SmsMessage, SmsResponse
import os

lat = 39.758949
long = -84.191605
owm_api_key = os.environ.get("OWM_API_KEY")
von_api_key = os.environ.get("VON_API_KEY")
api_secret = os.environ.get("API_SECRET")

data = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&cnt=4&appid={owm_api_key}")
data.raise_for_status()
intervals = data.json()["list"]

raining = False
for i in intervals:
    for condition in i["weather"]:
        if int(condition["id"]) < 700:
            raining = True
if raining:
    client = Vonage(Auth(api_key=von_api_key, api_secret=api_secret))
    message = SmsMessage(
        to="19377015358",
        from_="16265491364",
        text="Bring an Umbrella!",
    )

    response: SmsResponse = client.sms.send(message)
    print(response)
