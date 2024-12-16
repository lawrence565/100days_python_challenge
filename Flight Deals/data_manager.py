import requests, os, dotenv

dotenv.load_dotenv()

SHEETY_AUTH_KEY = os.getenv("SHEETY_TOKEN")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    headers = {
        "Authorization": SHEETY_AUTH_KEY
    }

    response = requests.get("https://api.sheety.co/854cce0fe880b4c4f9f6005261c20228/flightDeals/prices", headers=headers)
    response.raise_for_status()
    print(response.json())