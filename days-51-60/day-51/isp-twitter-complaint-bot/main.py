import config
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level=logging.CRITICAL)

#----------------------- Selenium browser settings -----------------------#

chrome_options = Options()

# Uncomment to prevent browser from closing automatically after program run
# chrome_options.add_experimental_option("detach", True)

# Disable DevTools message popping up on Windows
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

CHROME_DRIVER_PATH = config.chrome_driver_path

#------------------------------- Pre-setup -------------------------------#

# Speeds in ISP contract
PROMISED_DOWN = 1000
PROMISED_UP = 50

# Twitter login
TWITTER_HANDLE = config.twitter_handle
TWITTER_PASSWORD = config.twitter_password

# Seconds for Speedtest to get DL/UL speeds
SLEEP_RUN = 40

# Time buffer (in seconds) for transition between actions
SLEEP_SHORT = 2

#-------------------------------- The Bot --------------------------------#

class InternetSpeedTwitterBot:
    
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(options=chrome_options, service=Service(driver_path))
        self.down = 0
        self.up = 0

    def run_speedtest(self):
        """Runs speed test on Speedtest.net
        """
        
        self.driver.get("https://speedtest.net")

        # Preset browser window size
        self.driver.set_window_size(1080, 800)
        
        # Click the 'Go' Button
        self.go_button = self.driver.find_element("css selector", ".start-text")
        self.go_button.click()
        time.sleep(SLEEP_RUN)
        
        # If Speedtest.net phone ad pops up, dismiss
        try:
            self.dismiss_ad = self.driver.find_element("link text", "Back to test results")
            self.dismiss_ad.click()
        except NoSuchElementException:
            pass
        
        time.sleep(SLEEP_SHORT)
        
        # Find DL and UL speeds
        self.down = self.driver.find_elements("css selector", ".result-data-value")[0].text
        self.up = self.driver.find_elements("css selector", ".result-data-value")[1].text
        
        # Print speeds in terminal
        print(f"Down: {self.down}") 
        print(f"Up: {self.up}")  
    
    def send_tweet(self):
        """Sends tweet with down/up speed info
        """
        
        self.driver.get("https://twitter.com/login")

        time.sleep(SLEEP_SHORT)
        
        # Fill in username
        username = self.driver.find_element("xpath", "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        username.send_keys(TWITTER_HANDLE)
        time.sleep(SLEEP_SHORT)
        username.send_keys(Keys.ENTER)
        time.sleep(SLEEP_SHORT)
        
        try:
            # Enter phone number/username if prompted with additional verification
            verification = self.driver.find_element("xpath", '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            verification.send_keys(TWITTER_HANDLE)
            time.sleep(SLEEP_SHORT)
            verification.send_keys(Keys.ENTER)
            time.sleep(SLEEP_SHORT)
        
            # Fill in password
            password = self.driver.find_element("xpath", '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(TWITTER_PASSWORD)
            time.sleep(SLEEP_SHORT)
            password.send_keys(Keys.ENTER)
            
        except NoSuchElementException:
            # Fill in password
            password = self.driver.find_element("xpath", '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(TWITTER_PASSWORD)
            time.sleep(SLEEP_SHORT)
            password.send_keys(Keys.ENTER)
            
        time.sleep(SLEEP_SHORT)
        
        # Click 'Tweet' to open new tweet
        compose_tweet = self.driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        compose_tweet.click()
        time.sleep(SLEEP_SHORT)

        # Send tweet
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_box = self.driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_box.send_keys(tweet)
        time.sleep(SLEEP_SHORT)
        tweet_button = self.driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]')
        tweet_button.click()
        
        time.sleep(SLEEP_SHORT)
                
        # If Twitter pop-up shows up, dismiss
        try:
            twitter_popup = self.driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/div/div')
            twitter_popup.click()
        except NoSuchElementException:
            pass
        
        # Close browser
        time.sleep(SLEEP_SHORT)
        self.driver.quit()

#------------------------------ Run the bot ------------------------------#

tweet_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
tweet_bot.run_speedtest()
tweet_bot.send_tweet()




