import requests, os, dotenv
from twilio.rest import Client

dotenv.load_dotenv()

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN= os.getenv("AUTH_TOKEN")

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN

MY_LAT = os.getenv("MY_LAT")
MY_LNG = os.getenv("MY_LNG")
MY_API_KEY = os.getenv("MY_API_KEY")

params = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "cnt": 4,
    "appid": MY_API_KEY,

}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour in weather_data["list"]:
    condition =  hour["weather"][0]["id"]
    if int(condition) < 700:
        will_rain = True
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='+12707173309',
            body="It's going to rain, bring the umbrella",
            to='+886903199009'
        )
        print(message.sid)

        break


