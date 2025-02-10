import requests
from environs import Env
from pprint import pprint
from requests.auth import HTTPBasicAuth

env = Env()
env.read_env()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._user = env.str("SHEETY_USERNAME")
        self._password = env.str("SHEETY_PASSWORD")
        self.prices_endpoint = env.str("SHEETY_PRICES_ENDPOINT")
        self.users_endpoint = env.str("SHEETY_USERS_ENDPOINT")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        data = requests.get(url= self.prices_endpoint)
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
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint)
        data = response.json()
        # See how Sheet data is formatted so that you use the correct column name!
        # pprint(data)
        # Name of spreadsheet 'tab' with the customer emails should be "users".
        self.customer_data = data["users"]
        return self.customer_data