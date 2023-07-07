from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import logging

logging.basicConfig(level=logging.CRITICAL)

# Prevent browser from closing automatically after program run
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = "/Users/marilynyi/Development/chromedriver"
driver = webdriver.Chrome(options=chrome_options ,service=Service(chrome_driver_path))

# Preset browser window size
driver.set_window_size(1080, 720)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Starting game elements
cookie = driver.find_element("id", "cookie")
store = driver.find_elements("css selector", "#store div")
upgrade_names = []
for upgrade in store:
    upgrade_names.append(upgrade.get_attribute("id"))
    
# logging.critical(f"{upgrade_names=}")

# Define number of seconds between upgrade affordability checks
time_check_upgrade = time.time() + 5

# Define number of seconds before stopping bot
time_stop_bot = time.time() + 60 * 5

while time.time() < time_stop_bot:
    
    # Click the cookie
    cookie.click()

    # Check upgrade every 5 seconds
    if time.time() > time_check_upgrade:
        
        # Count current number of cookies
        money = driver.find_element("id", "money").text
        money = int(money.replace(",", ""))
        
        logging.critical(f"{money=}")    
        
        # Find upgrade price elements
        prices_text = driver.find_elements("css selector", "#store b")
        
        # Convert upgrade prices into integer values
        upgrade_prices = []
        for pt in prices_text:
            price_text = pt.text
            if price_text != "":
                price = int(price_text.split("-")[1].strip().replace(",", ""))
                upgrade_prices.append(price)
                
        # Create dictionary of upgrade names and prices 
        upgrades = {}
        for n in range(len(upgrade_prices)):
            upgrades[upgrade_prices[n]] = upgrade_names[n]
            
        # logging.critical(f"{upgrades=}")
            
        # Filter for affordable upgrades only
        affordable_upgrades = {}   
        for price, name in upgrades.items():
            if money > price:
                affordable_upgrades[price] = name
        
        # Find most expensive affordable upgrade
        price_buy_upgrade = max(affordable_upgrades)
        logging.critical(f"{price_buy_upgrade=}")
        
        # Click on most expensive affordable upgrade to buy
        name_buy_upgrade = affordable_upgrades[price_buy_upgrade]
        driver.find_element("id", name_buy_upgrade).click()
        logging.critical(f"{name_buy_upgrade=}")
        
        # Check again in 5 seconds
        time_check_upgrade = time.time() + 5 

# Print cookies per second after bot stops
cps_text = driver.find_element("id", "cps").text
cookies_per_second = float(cps_text.split(" ")[2])
print("-"*30)
print(f"Cookies per second: {cookies_per_second}")
        
# driver.close()
# driver.quit()