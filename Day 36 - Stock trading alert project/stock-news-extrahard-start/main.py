import os
import requests
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.environ.get('D36_stock_key')
NEWS_API_KEY = os.environ.get('D36_news_key')
account_sid = 'AC02bf2822bb9d5f8590efac3d1ef0ee4a'
auth_token = os.environ.get('D35_sms_auth_token')
# # STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# Other (smarter) way would be changing dictionary into list and getting
# hold of yesterday and day before yesterday data with [0] and [1]
yesterday = (datetime.today() - timedelta(1)).strftime('%Y-%m-%d')
two_days_ago = (datetime.today() - timedelta(2)).strftime('%Y-%m-%d')
parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'apikey': STOCK_API_KEY,
}
response = requests.get(url='https://www.alphavantage.co/query', params=parameters)
response.raise_for_status()
data = response.json()['Time Series (Daily)']
price_yesterday = float(data[yesterday]['4. close'])
price_two_days = float(data[two_days_ago]['4. close'])
change_percent = abs(round((price_yesterday - price_two_days)/price_two_days*100, 2))
non_abs_change = round((price_yesterday - price_two_days)/price_two_days*100, 2)

if non_abs_change >= 0:
    status = f'🔺{change_percent}%'
else:
    status = f'🔻{change_percent}%'

# # STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_parameters = {
    'apiKey': NEWS_API_KEY,
    'q': COMPANY_NAME
}
if change_percent > 1:
    news_response = requests.get(url='https://newsapi.org/v2/everything', params=news_parameters)
    news_response.raise_for_status()
    news = news_response.json()['articles'][:3]
    message = [f"Headline: {article['title']}\nBrief: {article['description']}\n\n" for article in news]
    message.insert(0, f'{STOCK}: {status}\n')
    final_msg = ''.join(message)
    # # STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to='+48737168406',
        from_='+19705121521',
        body=final_msg)
