from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "/Users/marilynyi/Development/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get("https://python.org")

# Find element by name
search_bar = driver.find_element("name", "q")
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))
print("-"*30)

# Find element by class
python_logo = driver.find_element("class name", "python-logo")
print(python_logo.size)
print("-"*30)

# Find element by CSS selector
documentation_link = driver.find_element("css selector", ".documentation-widget a")
print(documentation_link.text)
print("-"*30)

# Find element by xpath
bug_link = driver.find_element("xpath", '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)
print("-"*30)

# driver.close()
driver.quit()