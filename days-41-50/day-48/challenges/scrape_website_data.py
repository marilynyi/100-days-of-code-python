from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pprint import pprint

chrome_driver_path = "/Users/marilynyi/Development/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get("https://python.org")

# Find event times
event_times = driver.find_elements("css selector", ".event-widget time")
# for time in event_times:
#     print(time.text)
# print("-"*30)

# Find event names
event_names = driver.find_elements("css selector", ".event-widget li a")
# for name in event_names:
#     print(name.text)

events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

pprint(events)

# driver.close()
driver.quit()