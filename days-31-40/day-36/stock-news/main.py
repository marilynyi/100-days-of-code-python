import requests
import config
from twilio.rest import Client
from datetime import datetime, timedelta

STOCK_NAME = "AAPL"
COMPANY_NAME = "Apple"
TWILIO_NUMBER = config.twilio_number
VERIFIED_NUMBER = config.verified_number
ACCOUNT_SID = config.account_sid
AUTH_TOKEN = config.auth_token

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_NAME,
    "interval": "60min",
    "extended_hours": "false",
    "apikey": config.stock_api_key,
}

news_params = {
    "q": COMPANY_NAME,
    "searchIn": "title",
    "apiKey": config.news_api_key,
}

# Get stock price data from API
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = stock_response.json()
stock_hourly = stock_data["Time Series (60min)"]

# Get datetime for yesterday's closing hour
num_days_ago = 1
yday = datetime.now() - timedelta(days=num_days_ago)
yday = datetime.combine(yday, datetime.min.time())
yday = yday + timedelta(hours=15)

# Get datetime for day before yesterday's closing hour
num_days_ago = 2
two_days_ago = datetime.now() - timedelta(days=num_days_ago)
two_days_ago = datetime.combine(two_days_ago, datetime.min.time())
two_days_ago = two_days_ago + timedelta(hours=15)

# Instantiate datetimes to strings to pull from JSON
yday_str = str(yday)
two_days_ago_str = str(two_days_ago)

# Get closing prices for yesterday and the day before yesterday
yday_close = float(stock_hourly[yday_str]["4. close"])
two_days_ago_close = float(stock_hourly[two_days_ago_str]["4. close"])

difference = yday_close - two_days_ago_close

# Indicate positive or negative difference between closing days
# to use in text message header
up_down = None
if difference > 0:
    up_down = "🟢"
else:
    up_down = "🔻"
    
# Calculate percent difference between closing days
# to use in text message header
abs_diff = abs(difference)
percent_diff = round(abs_diff/yday_close * 100)

# If price difference is significant if greater than 1%
price_diff_is_sig = False

if percent_diff > 1:
    price_diff_is_sig = True

# Text three relevant company articles if stock price difference > 5%    
if price_diff_is_sig:
    # Get company news data from API
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()["articles"]
    three_articles = news_data[:3]
    
    formatted_articles = [f"{STOCK_NAME}: {up_down}{percent_diff}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
 
    client = Client(ACCOUNT_SID, AUTH_TOKEN)  
     
    # Send each article as a separate message 
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )
        
    print(message.status) 
 