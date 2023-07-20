import requests
from config import config

SHEETY_PRICES_ENDPOINT = config.sheety_prices_endpoint
SHEETY_BEARER_AUTH = config.sheety_bearer_auth

headers = {
    "Authorization": f"Bearer {SHEETY_BEARER_AUTH}"
}

class DataManager:
    """This class is responsible for talking to the Google Sheet.
    """
    
    def __init__(self):
        self.destination_data = {}
    
    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data, headers=headers)
            print(response.text)