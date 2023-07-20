from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Prevent browser from closing automatically after program run
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = "/Users/marilynyi/Development/chromedriver"
driver = webdriver.Chrome(options=chrome_options, service=Service(chrome_driver_path))

driver.set_window_size(800, 800)

driver.get("http://secure-retreat-92358.herokuapp.com/")

# Fill out first name
fname = driver.find_element("name", "fName")
fname.send_keys("Firstname")

# Fill out last name
lname = driver.find_element("name", "lName")
lname.send_keys("Lastname")

# Fill out email
email = driver.find_element("name", "email")
email.send_keys("first.last@gmail.com")

# Select the first element in the dropdown list and press Enter again
signup_button = driver.find_element("xpath", '/html/body/form/button')
signup_button.click()

# driver.close()
# driver.quit()