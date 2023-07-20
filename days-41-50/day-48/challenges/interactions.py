from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "/Users/marilynyi/Development/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Find number of articles
article_element = driver.find_element("css selector", "#articlecount a")
num_articles = article_element.text

print(num_articles)

# driver.close()
driver.quit()