import config
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level=logging.CRITICAL)

EMAIL = config.email
PASSWORD = config.password
LINKEDIN_PAGE = config.linkedin_page

# Prevent browser from closing automatically after program run
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chrome_driver_path = "/Users/marilynyi/Development/chromedriver"
driver = webdriver.Chrome(options=chrome_options, service=Service(chrome_driver_path))

# Preset browser window size
driver.set_window_size(1080, 1200)

#-------------------- Signing in to LinkedIn --------------------#

# Fetch job page with custom filter settings
driver.get(LINKEDIN_PAGE)

# Click 'Sign in' to go to login page
sign_in = driver.find_element("link text", "Sign in")
sign_in.click()

time.sleep(5)

# Fill in email
email = driver.find_element("name", "session_key")
email.send_keys(EMAIL)

# Fill in password
password = driver.find_element("name", "session_password")
password.send_keys(PASSWORD)

# Click 'Sign in' button
sign_in = driver.find_element("xpath", '//*[@id="organic-div"]/form/div[3]/button')
sign_in.click()

time.sleep(5)

#-------------------- Automating Easy Apply --------------------#

job_posts = driver.find_elements("css selector", ".job-card-list")

for post in job_posts:
    
    # Click on job post
    post.click()
    time.sleep(5)
    
    # Click 'Easy Apply' button
    apply_button = driver.find_element("css selector", ".jobs-s-apply button")
    apply_button.click()
    time.sleep(5)

    # Submit application if 'Submit application' button is on first application page
    try:
        # Press the 'Submit application' button
        submit_button = driver.find_element("link text", "Submit application")    
        submit_button.click()
        time.sleep(5)   
        
        # Press the exit button when confirmation window pops up
        exit_button = driver.find_element("css selector", ".artdeco-modal_dismiss")
        exit_button.click()
        print("Application sent.")
        
    # Otherwise, cancel and discard application
    except NoSuchElementException:
        
        # Press the exit button
        exit_button = driver.find_element("css selector", ".artdeco-modal_dismiss")
        exit_button.click()
        time.sleep(5)       
        
        # Press the 'Discard' button to confirm leaving the application without saving
        discard_button = driver.find_element("css selector", ".artdeco-modal__confirm-dialog-btn")
        discard_button.click()
        print("Application discarded.")
        time.sleep(5)