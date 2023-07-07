from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Prevent browser from closing automatically after program run
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = "/Users/marilynyi/Development/chromedriver"
driver = webdriver.Chrome(options=chrome_options ,service=Service(chrome_driver_path))

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Find an element and click on it

# Method 1: Add the click function
# article_element = driver.find_element("css selector", "#articlecount a")
# article_element.click()

# Method 2: Find element by link text
article_element = driver.find_element("link text", "Content portals")
article_element.click()

# driver.close()
# driver.quit()