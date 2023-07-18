import config
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

#----------------------- Selenium browser settings -----------------------#

chrome_options = Options()

# Uncomment to prevent browser from closing automatically after program run
chrome_options.add_experimental_option("detach", True)

# Disable DevTools message popping up on Windows
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

CHROME_DRIVER_PATH = config.chrome_driver_path

#------------------------------- Pre-setup -------------------------------#

# Account credentials
USERNAME = config.instagram_username
PASSWORD = config.instagram_password

# Time buffers (in seconds)
SLEEP_BETWEEN = 2
SLEEP_PAUSE = 4
SLEEP_SHORT = 1

# Bot inputs
TARGET_PAGE = "chihuahuasfan"
FOLLOW_COUNT = 10

#-------------------------------- The Bot --------------------------------#

class InstaFollower:
    
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(options=chrome_options, service=Service(driver_path))
        
        # Preset browser window size
        self.driver.set_window_size(950, 825)

    def login(self):
        """Logs in to Instagram.
        """
        
        self.driver.get("https://instagram.com/accounts/login")
        
        time.sleep(SLEEP_BETWEEN)
        
        username = self.driver.find_element("name", "username")
        username.send_keys(USERNAME)

        time.sleep(SLEEP_SHORT)
        
        password = self.driver.find_element("name", "password")
        password.send_keys(PASSWORD)
        
        time.sleep(SLEEP_BETWEEN)
        
        password.send_keys(Keys.ENTER)
        
        time.sleep(SLEEP_PAUSE)
        
        # Dismiss pop-ups
        try:
            # Click 'Not Now' if Instagram asks if you want to save your login info
            login_save_dismiss = self.driver.find_element("css selector", ".x1i10hfl")
            login_save_dismiss.click()
            
            time.sleep(SLEEP_PAUSE)
            
            # Click 'Not Now' if Instagram asks if you want to turn on notifications
            notif_on_dismiss = self.driver.find_element("css selector", "._a9_1")
            notif_on_dismiss.click()
            
        except NoSuchElementException:
            pass
        
        time.sleep(SLEEP_BETWEEN)
    
    def find_followers(self):
        """Launches target Instagram's followers page.
        """
        
        self.driver.get(f"https://instagram.com/{TARGET_PAGE}")

        time.sleep(SLEEP_BETWEEN)
        
        # Click on followers
        follower_count = self.driver.find_elements("css selector", ".x78zum5 li")[1]
        follower_count.click()
        
        time.sleep(SLEEP_BETWEEN)

    def follow(self):
        """Scrolls through any Instagram page's list of followers and clicks the 'Follow' button if not already following or requested.
        """
    
        # Focus follower pop-up window
        follower_popup = self.driver.find_element("css selector", '._aano')
        time.sleep(SLEEP_BETWEEN)
        
        # Scroll through follower list and click 'Follow'
        scroll_height = 0   
        for num in range(1, FOLLOW_COUNT+1):
            follow_button = self.driver.find_element("xpath", 
                                                        f"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{num}]/div/div/div/div[3]/div/button")
            follow_button_text = self.driver.find_element("xpath", 
                                                        f"/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[{num}]/div/div/div/div[3]/div/button/div/div").text            

            # Skip if already followed or requested
            if follow_button_text == "Follow":
                follow_button.click()
                print(f"User #{num}/{FOLLOW_COUNT} followed.")
            elif follow_button_text == "Requested": 
                print(f"User #{num}/{FOLLOW_COUNT} already requested. Skipping.")
                pass
            elif follow_button_text == "Following":
                print(f"User #{num}/{FOLLOW_COUNT} already followed. Skipping. ")
                pass
            else:
                pass
            
            time.sleep(SLEEP_BETWEEN)
                       
            # Start scrolling up when there's one more visible follower in the list
            if num > 5:
                scroll_height += 60                
                self.driver.execute_script(f"arguments[0].scrollTo(0, {scroll_height})", follower_popup)
                time.sleep(SLEEP_BETWEEN)      

        # Close browser
        self.driver.quit()

#------------------------------ Run the bot ------------------------------#

insta_bot = InstaFollower(CHROME_DRIVER_PATH)
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()




