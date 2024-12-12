import requests, smtplib, time, os, dotenv
from datetime import datetime

dotenv.load_dotenv()
MY_EMAIL = os.getenv("GMAIL_EMAIL")
MY_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
MY_LAT = 121.523016
MY_LONG = 25.11404
running = True

#Your position is within +5 or -5 degrees of the ISS position.
def detect_position():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    if iss_latitude - 5 < MY_LAT < iss_latitude + 5 and iss_longitude - 5 < MY_LONG < iss_longitude - 5:
        return True

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

def is_night():
    if time_now.hour < sunrise or time_now.hour > sunset:
        return True
    else:
        return False

while running:
    if detect_position() and is_night():
        try:
            with smtplib.SMTP("smtp.gmail.com") as conn:
                conn.starttls()
                conn.login(user=MY_EMAIL, password=MY_PASSWORD)
                conn.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs="5655566haha@gmail.com",
                    msg="Subject:LOOP UP for the ISS!!!\n\nThe ISS is passing the sky in night, loop up and find the ISS!!!")
            running = False
        except smtplib.SMTPException:
            print("There's problem with SMTP connection.")
    time.sleep(60)

while not running:
    time.sleep(8 * 60 * 60)
    running = True
