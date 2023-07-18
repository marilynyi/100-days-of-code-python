from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Prevent browser from closing automatically after program run
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = "/Users/marilynyi/Development/chromedriver"
driver = webdriver.Chrome(options=chrome_options ,service=Service(chrome_driver_path))

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Select an element and type in it
search = driver.find_element("name", "search")
search.send_keys("Python")

# Select the first element in the dropdown list and press Enter again
search_button = driver.find_element("xpath", '//*[@id="searchform"]/div/button')
search_button.click()

# driver.close()
# driver.quit()