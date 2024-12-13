import requests, os, dotenv, sys, datetime, math
from future.backports.datetime import timedelta
from twilio.rest import Client
from xlwings.constants import directions

dotenv.load_dotenv()

MY_API_KEY = os.getenv("MY_API_KEY")
MY_NEWS_API = os.getenv("MY_NEWS_API")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = ACCOUNT_SID
auth_token = AUTH_TOKEN

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": MY_API_KEY,
}
response = requests.get(url="https://www.alphavantage.co/query", params=params)
response.raise_for_status()
data = response.json()

try:
    stock_data = data['Time Series (Daily)']
    today = datetime.datetime.today()
except KeyError:
    print("The API calls is reached the limit today.")
    sys.exit()


def get_stock_data(stock):
    stock_price_list = []

    # Original function, find the value of the keys
    # while len(stock_price) < 2:
    #     # Formatting with the strftime()
    #     format_today = day.strftime("%Y-%m-%d")
    #     if format_today in stock:
    #         stock_price_list.append(stock[format_today])
    #     day = day + timedelta(days=-1)

    # Translate data to a useful list
    stock_price_list = [value for (key, value) in stock.itmes()]
    return stock_price_list


def price_gap_high(stock_list):
    yesterday = stock_list[0]
    yesterday_price = float(yesterday["4. close"])
    before_yesterday = stock_list[1]
    before_yesterday_price = float(before_yesterday["4. close"])
    gap = yesterday_price - before_yesterday_price
    gap_percentage = (gap / yesterday_price) * 100

    direction = "-"
    if gap > 0:
        direction = "🔺"
    elif gap < 0:
        direction = "🔻"

    if abs(gap_percentage) > 2:
        return True, gap, direction
    else:
        return False, gap, direction


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news():
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": MY_NEWS_API,
        "pageSize": 3,
        "page": 1
    }

    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
    news_data = news_response.json()
    article_list = [f"""Headlines: {article["title"]}\n
                    Brief: {article["description"]}\n"""
                    for article in news_data["articles"]]
    return article_list


## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
def send_sms(contents, direction, gap):
    client = Client(account_sid, auth_token)
    sms_content_list = [f"\n{STOCK}: {direction} {gap}%\n{content}" for content in contents]

    for sms in sms_content_list:
        print(sms)

    # message = client.messages.create(
    #     from_='+12707173309',
    #     body=content,
    #     to='+886903199009'
    # )
    # print(message.sid)


stock_price = get_stock_data(stock_data)
stock_status = price_gap_high(stock_price)
if stock_status[0]:
    stock_news = get_news()
    send_sms(stock_news, stock_status[1], stock_status[2])

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
