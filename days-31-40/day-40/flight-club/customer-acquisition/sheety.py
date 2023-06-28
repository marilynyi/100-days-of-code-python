import requests
import sys
sys.path.append('..')
from config import config

SHEETY_USERS_ENDPOINT = config.sheety_users_endpoint
SHEETY_BEARER_AUTH = config.sheety_bearer_auth

def post_new_row(first_name, last_name, email):

    headers = {
        "Authorization": f"Bearer {SHEETY_BEARER_AUTH}",
        "Content-Type": "application/json",
    }

    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }

    response = requests.post(url=SHEETY_USERS_ENDPOINT, headers=headers, json=body)
    response.raise_for_status()
    print(response.text)