from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "/Users/marilynyi/Development/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get("https://www.amazon.com/dp/B098WVKF19/ref=pd_bxgy_img_sccl_1/131-6645546-7932634")
price_text = driver.find_element("class name", "a-offscreen")
print(price_text.get_attribute("innerHTML"))

# driver.close()
driver.quit()