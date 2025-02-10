import requests
from environs import Env
from pprint import pprint
from requests.auth import HTTPBasicAuth

env = Env()
env.read_env()

SHEET_TOKEN = env.str("SHEET_TOKEN")
URL = "https://api.sheety.co/8ef5eb6b682a3ffd693f688ef3eaeb5b/flightDealsJoãoCalsavara/prices"
HEADERS={
    "Authorization": f"Bearer {SHEET_TOKEN}",
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._user = env.str("SHEETY_USERNAME")
        self._password = env.str("SHEETY_PASSWORD")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}

    def get_destination_data(self):
        data = requests.get(url=URL,headers=HEADERS)
        print(data.text)
        self.destination_data = data.json()["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{URL}/{city['id']}",
                json=new_data
            )
            # print(response.text)