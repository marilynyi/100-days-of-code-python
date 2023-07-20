import requests
from datetime import datetime
from config import config

APP_ID = config.app_id
API_KEY = config.api_key

AUTH_TOKEN = config.auth_token

GENDER = config.gender
WEIGHT_KG = config.weight_kg
HEIGHT_CM = config.height_cm
AGE = config.age

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

bearer_headers = {
    "Authorization": f"Bearer {AUTH_TOKEN}"
}

exercise_post_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = config.sheet_endpoint

input_exercise = input("What did you do today? ")

exercise_params = {
    "query": input_exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
        
}

response = requests.post(url=exercise_post_endpoint, json=exercise_params, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%m/%d/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    
sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)
print(sheet_response.text)