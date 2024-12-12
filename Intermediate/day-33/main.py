import datetime

import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()["iss_position"]
# longitude = data["longitude"]
# latitude = data["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)

MY_LONGITUDE = 25.11404
MY_LATITUDE = 121.523016

parameters = {
    "lng": MY_LONGITUDE,
    "lat": MY_LATITUDE,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
now = datetime.datetime.now().hour
print(sunrise, sunset)