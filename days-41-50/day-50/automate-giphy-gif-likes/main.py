import config
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level=logging.CRITICAL)

#------------------------------- USER INPUTS --------------------------------#

# Ask user if they want to sign in to their Giphy account
while True:
    giphy_account = input("Log in to Giphy? Enter Y or N: ").strip().lower()
    if giphy_account in ["y", "n"]:
        break
    print("Invalid input. Try again.\n")

# Ask user for search phrase
while True:
    SEARCH_FOR = input("What do you want to search for on Giphy? ").strip()
    if SEARCH_FOR != "":
        break
    print("Please provide a search phrase.\n")

# Specify how many GIFs to "swipe" through before stopping bot
while True:
    try:
        GIF_COUNT = int(input("How many GIFs? Enter a number: ").strip())
        break
    except ValueError: 
        print("Please provide a valid number.")
        pass

#-------------------------------- Pre-setup ---------------------------------#

# Create list of hash tags
include_hashtags = ["#" + word for word in SEARCH_FOR.split(" ")]
include_hashtags.append(f"#{SEARCH_FOR}")
logging.critical(f"{include_hashtags=}")

# Account credentials
EMAIL = config.email
PASSWORD = config.password

# Set number of sleep seconds
SLEEP_SECONDS = 3

#----------------------------- Browser settings -----------------------------#

# Prevent browser from closing automatically after program run
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Instantiate Chrome WebDriver
chrome_driver_path = "/Users/marilynyi/Development/chromedriver"
driver = webdriver.Chrome(options=chrome_options, service=Service(chrome_driver_path))

# Preset browser window size
driver.set_window_size(1080, 1200)

#------------- Logging in to Giphy and navigating to GIFs page --------------#

# If user wants to sign in to Giphy 
if giphy_account == "y":
    
    # Open and load generic URL
    # Logging in to Giphy takes you to your channel automatically
    driver.get("https://giphy.com/")

    time.sleep(SLEEP_SECONDS)
    
    try:
        # Close the 'Privacy Policy' banner (if it exists) covering the Login button
        close_button = driver.find_element("css selector", ".CloseButton-sc-ecivd4")
        close_button.click()
        time.sleep(SLEEP_SECONDS)
        
        # Click 'Login' button to redirect to login page
        login_button = driver.find_element("css selector", ".Username-sc-xgchsp")
        login_button.click()
        time.sleep(5)
    except NoSuchElementException:
        # Click 'Login' button to redirect to login page
        login_button = driver.find_element("css selector", ".Username-sc-xgchsp")
        login_button.click()
        time.sleep(SLEEP_SECONDS)

    # Fill in email address
    email = driver.find_element("name", "email")
    email.send_keys(EMAIL)

    # Fill in password
    password = driver.find_element("name", "password")
    password.send_keys(PASSWORD)

    # Press 'Log in' button
    log_in_button = driver.find_element("css selector", ".Button-sc-nzk41b")
    log_in_button.click()

    time.sleep(SLEEP_SECONDS)
    
    # Types user input in Search bar
    search_field = driver.find_element("name", "search")
    search_field.send_keys(SEARCH_FOR)
    search_field.send_keys(Keys.RETURN)

    time.sleep(SLEEP_SECONDS)

    # If user input was blank, go to all trending gifs
    if SEARCH_FOR.strip() == "":
        all_trending_gifs = driver.find_element("css selector", ".SeeAll-sc-1k96td4")
        all_trending_gifs.click()
    
    time.sleep(SLEEP_SECONDS)

# Else if user wants to continue as a guest Giphy user
else:
    # Open and load specified URL
    driver.get(f"https://giphy.com/search/{SEARCH_FOR}")
    
time.sleep(SLEEP_SECONDS)

#-------------------------- Going to GIF-only page --------------------------#

# Click on first GIF in the list
first_gif = driver.find_element("css selector", ".giphy-grid picture img")
first_gif.click()
    
time.sleep(SLEEP_SECONDS)

#---------------------- Adding to Favorite collection -----------------------#

for n in range(GIF_COUNT):
    
    logging.critical(f"Viewing GIF #{n+1}.")
    
    # Find GIF hash tags and add to list
    hash_tags = driver.find_elements("css selector", ".TagsContainer-sc-1i1183u a h3")
    
    gif_tags = []
    for tag in hash_tags:
        tag_text = tag.text
        if tag_text != "" and tag_text != "...":
            gif_tags.append(tag_text)
        
    logging.critical(gif_tags)

    # Count occurrence of split phrase words in image gif tags
    count = 0
    for hashtag in include_hashtags[:-1]:
        if hashtag in gif_tags:
            count += 1
            
    logging.critical(f"{count=} out of {len(include_hashtags[:-1])}")

    # Click Favorite button if gif tags have:
    #   if image is not already favorited
    #   and
    #   one or both of the following:
    #       (1) the initial search word
    #       (2) all of the words split from the initial search phrase
    try:
        gif_already_favorited = driver.find_element("css selector", ".FavoriteContainer-sc-rjzgpb .bgrYln")
        print("GIF already favorited. Skipped.")
    except NoSuchElementException:
        if count == len(include_hashtags[:-1]) or include_hashtags[-1] in gif_tags:
            favorite_button = driver.find_element("css selector", ".FavoriteContainer-sc-rjzgpb")
            favorite_button.click()
            print(f"GIF #{n+1} added to Favorites.")
        else:
            print(f"GIF #{n+1} skipped.")

    time.sleep(SLEEP_SECONDS)
    
    # Stay on last GIF page when terminating bot
    if n == GIF_COUNT-1:
        break

    # Go to next GIF
    try:
        # Close the 'Privacy Policy' banner (if it exists) covering the Login button
        close_button = driver.find_element("css selector", ".CloseButton-sc-ecivd4")
        close_button.click()
        time.sleep(SLEEP_SECONDS)
        
        # Go to next GIF
        right_arrow_button = driver.find_element("css selector", ".ss-navigateright")
        right_arrow_button.click()
        print("Going to next GIF.")
    except NoSuchElementException:
        # Go to next GIF
        right_arrow_button = driver.find_element("css selector", ".ss-navigateright")
        right_arrow_button.click()  
        print("Going to next GIF.")

    time.sleep(SLEEP_SECONDS)

# Print in terminal once bot is stopped
print("Explored all GIFs. Bot has stopped.")

# Close browser
driver.quit()