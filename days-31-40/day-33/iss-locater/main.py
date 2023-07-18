import requests

# response codes
# 1XX: hold on
# 2XX: successful
# 3XX: not permitted
# 4XX: error
# 5XX: server error

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)