import requests
import config
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = config.username
TOKEN = config.token
GRAPH_ID = config.graph_id

# Instantiate authentication token as request header key
headers = {
    "X-USER-TOKEN": TOKEN
}

def create_account():
    """Create a Pixela account.
    
    Keyword arguments:
    None
    
    Specify username and authentication token in config.py file \
    before running this function.
    """
    
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)

def create_graph(graph_id: str):
    """Create a new graph.
    
    Keyword arguments:
    graph_id: str -- ID string with the validation rule: \
                     ^[a-z][a-z0-9-]{1,16}
    """
    
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

    graph_config = {
        "id": graph_id,
        "name": "Study Graph",
        "unit": "Hr",
        "type": "float",
        "color": "ajisai" # purple
    }

    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)

def add_pixel(is_today: bool, quantity: str, *args: int):
    """Add a new pixel to the graph.
    
    Keyword arguments:
    is_today: bool -- True if today, False otherwise
    quantity: str -- floating units written as a string
    *args: int -- if is_today is False, \
                    specify year, month, and day \
                    as three arguments separated by commas \
                    e.g., 2023, 6, 25
    """
    
    pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

    if is_today:
        today = datetime.now()
    else:
        today = datetime(year=args[0], month=args[1], day=args[2])

    pixel_add = {
        "date": today.strftime("%Y%m%d"),
        "quantity": quantity,
    }

    response = requests.post(url=pixel_creation_endpoint, json=pixel_add, headers=headers)
    print(response.text)

def update_pixel(year: int, month: int, day: int, quantity: str):
    """Update an existing pixel.
    
    Keyword arguments:
    year: int -- year of desired pixel to update
    month: int -- month of desired pixel to update
    day: int -- day of desired pixel to update
    quantity: str -- number of new units provided in string format
    """
    
    update_day = datetime(year=year, month=month, day=day)

    pixel_update = {
        "date": update_day.strftime("%Y%m%d"),
        "quantity": quantity
    }

    pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{update_day.strftime('%Y%m%d')}"
    response = requests.put(url=pixel_update_endpoint, json=pixel_update, headers=headers)
    print(response.text)
    
def delete_pixel(year: int, month: int, day: int):
    """Delete an existing pixel.
    
    Keyword arguments:
    year: int -- year of desired pixel to delete
    month: int -- month of desired pixel to delete
    day: int -- day of desired pixel to delete
    """
    
    delete_day = datetime(year=year, month=month, day=day)

    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{delete_day.strftime('%Y%m%d')}"
    response = requests.delete(url=delete_endpoint, headers=headers)
    print(response.text)

# ======================= Functions to use ======================= #
# See function docstrings for more info

# create_account()
# create_graph("graph1")
# update_pixel(2023, 6, 25, "9.0")
# delete_pixel(2023, 4, 1)
# add_pixel(0, "4", 2023, 4, 1) # if day other than today
# add_pixel(1, "4") # if today
