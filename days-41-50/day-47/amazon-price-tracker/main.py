import cloudscraper
import smtplib
import logging
import config
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.CRITICAL)

# Amazon's recognition of automated access is blocking frequent requests via the 'requests' module.
# We use the 'cloudscraper' module instead.
scraper = cloudscraper.create_scraper()

# SMTP Auth to send email notification
EMAIL = config.email
PASSWORD = config.password

#----- Step 1/2: Use BeautifulSoup to Scrape the Product Price -----#

PRODUCT_URL = "https://www.amazon.com/dp/B098WVKF19/ref=pd_bxgy_img_sccl_1/131-6645546-7932634" 
PRODUCT_PRICE_THRESHOLD = 150

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = scraper.get(PRODUCT_URL, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(class_="a-offscreen").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
logging.debug(price_as_float)

name = soup.find(id="productTitle", class_="a-size-large product-title-word-break").getText().strip()
logging.debug(name)

#----- Step 2/2: Email Alert When Price Below Desired Value -----#

if price_as_float < float(PRODUCT_PRICE_THRESHOLD*1.0):
    
    message = f"Subject:Amazon Deal Alert!\
            \n\nProduct: {name}\
            \nDesired Price: ${PRODUCT_PRICE_THRESHOLD}\
            \nCurrent Price: ${price_as_float}"
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(EMAIL, PASSWORD)
    connection.sendmail(from_addr=EMAIL, 
                        to_addrs=EMAIL,
                        msg = f"{message}".encode("utf-8")
                        )