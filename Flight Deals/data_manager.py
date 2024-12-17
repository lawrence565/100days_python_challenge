import requests, os, dotenv
from typing import List
from requests.auth import HTTPBasicAuth

dotenv.load_dotenv()

# Global Constance
SHEETY_AUTH_KEY = os.getenv("SHEETY_TOKEN")
SHEETY_ENDPOINT = "https://api.sheety.co/f505c85ccf6b21da99164e646ed462cb/flightDeals"

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = []
        self.user_data = []
        self._authorization = f"Bearer {SHEETY_AUTH_KEY}"

    def get_destination_data(self) -> List:
        response = requests.get(url=f"{SHEETY_ENDPOINT}/prices", headers={"Authorization": self._authorization})
        response.raise_for_status()
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def get_user_data(self):
        response = requests.get(url=f"{SHEETY_ENDPOINT}/users", headers={"Authorization": self._authorization})
        response.raise_for_status()
        self.user_data = response.json()["users"]
        return self.user_data

    def update_iata_code(self):
        for city in self.destination_data:
            try:
                params = {
                    'price': {
                        'iataCode': city["iataCode"]
                    }
                }
                response = requests.put(
                    url=f"{SHEETY_ENDPOINT}/prices/{city['id']}",
                    headers={"Authorization": self._authorization},
                    json=params)
                response.raise_for_status()
            except KeyError as K:
                print("There are some problem about the data. Please try again", K)

    def update_lowest_price(self):
        for city in self.destination_data:
            try:
                params = {
                    'price': {
                        'lowestPrice': city["lowestPrice"]
                    }
                }
                response = requests.put(
                    url=f"{SHEETY_ENDPOINT}/prices/{city['id']}",
                    headers={"Authorization": self._authorization},
                    json=params)
                response.raise_for_status()
            except KeyError:
                print("There are some problem about the data. Please try again")

datamanager = DataManager()
# datamanager.get_destination_data()
# print(datamanager.destination_data)
datamanager.get_user_data()
print(datamanager.user_data)