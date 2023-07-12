import config
import time
import logging
import requests
from pprint import pformat
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

logging.basicConfig(level=logging.CRITICAL)

def print_log_details(variable):
    if LOGGING_STATUS == True:
        logging.critical(variable) if LOGGING_STATUS == True else logging.disable(variable)
    
# Set to True to print logging details
LOGGING_STATUS = True
     
#-----------------------------------------------------------------------------------------------------------#
# Program Requirement #1: Use BeautifulSoup/Requests to scrape all the listings from the Zillow web address
#-----------------------------------------------------------------------------------------------------------#

ZILLOW_URL = config.zillow_url

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(ZILLOW_URL, headers=headers)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

#-----------------------------------------------------------------------------------------------------------#
# Program Requirement #2: Create a list of links for all the listings you scraped
#-----------------------------------------------------------------------------------------------------------#

property_link_elements = soup.select(".property-card-data a")

property_links = []
for link in property_link_elements:
    property_link = link.get("href")
    if "http" in property_link:
        property_links.append(property_link)
    else:
        property_links.append(f"https://www.zillow.com{property_link}")

print_log_details(pformat(property_links)) 

#-----------------------------------------------------------------------------------------------------------#
# Program Requirement #3: Create a list of prices for all the listings you scraped
#-----------------------------------------------------------------------------------------------------------#

property_price_elements = soup.select(".photo-cards li span")

property_prices = []
for price in property_price_elements:
    property_price = price.getText()
    # Select only first span element which is the price
    if "$" in property_price:
        # If price string has string "/mo"
        if "/" in property_price:
            property_price = property_price.split("/")[0]
            property_prices.append(property_price)
        # If price string has number of bedrooms
        elif "+" in property_price:
            property_price = property_price.split("+")[0]
            property_prices.append(property_price)
    
print_log_details(property_prices) 

#-----------------------------------------------------------------------------------------------------------#
# Program Requirement #4: Create a list of addresses for all the listings you scraped
#-----------------------------------------------------------------------------------------------------------#

property_address_elements = soup.select(".property-card-data address")

property_addresses = []
for address in property_address_elements:
    property_address = address.getText()
    # If address is delineated from name by the "|" separator
    if "|" in property_address:
        property_address = property_address.split("|")[-1].strip()
    # If address is delineated from name by the "," separator
    else:
        property_address = property_address.split(", ", 1)[-1].strip()
    property_addresses.append(property_address)
    
print_log_details(pformat(property_addresses)) 

#-----------------------------------------------------------------------------------------------------------#
# Program Requirement #5: Use Selenium to fill in the form you created.
# Each listing should have its price/address/link added to the form.
# You will need to fill in a new form for each new listing.
#-----------------------------------------------------------------------------------------------------------#

options = Options()

# Uncomment to prevent browser from closing automatically after program run
# options.add_experimental_option("detach", True)

# Disable DevTools message popping up on Windows
options.add_experimental_option('excludeSwitches', ['enable-logging'])

DRIVER_PATH = config.chrome_driver_path

driver = webdriver.Chrome(options=options, service=Service(DRIVER_PATH))    

# Preset browser window size
driver.set_window_size(810, 890)    

for address, price, link in zip(property_addresses, property_prices, property_links):

    # Go to Google form
    google_form = driver.get("https://docs.google.com/forms/d/1kxqmrdsl4yFVj8EyPi6b7fneRWXr2IbHyPrFxkguvrs")
    time.sleep(1)
    
    # Find input fields for address, price, and link
    address_input = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    
    # Fill in form fields
    address_input.send_keys(address)
    time.sleep(.1)
    price_input.send_keys(price)
    time.sleep(.1)
    link_input.send_keys(link)
    time.sleep(.5)
    
    # Submit the form
    submit_button = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()
    time.sleep(1)
    
driver.quit()
    