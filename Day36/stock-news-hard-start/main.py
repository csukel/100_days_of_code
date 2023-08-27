import requests
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""
## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yerstday's closing stock price.
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}
stock_res: requests.Response = requests.get(STOCK_ENDPOINT, parmas=stock_params)
stock_res.raise_for_status()

today = datetime.today()
yesterday = (today - timedelta(days=1)).strftime("%Y-%m-%d")
two_days_ago = (today - timedelta(days=2)).strftime("%Y-%m-%d")

stock_data = stock_res.json()

yesterday_close_stock = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
two_days_ago_close_stock = float(
    stock_data["Time Series (Daily)"][two_days_ago]["4. close"]
)

diff = yesterday_close_stock - two_days_ago_close_stock
change = diff / two_days_ago_close_stock

if abs(change) >= 5:
    if change > 0:
        change_str = f"🔺{change:.0%}"
    else:
        change_str = f"🔻{change:.0%}"

    print(change_str)
    print("Get the news")

    news_params = {
        "q": COMPANY_NAME,
        "from": yesterday,
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY,
    }
    news_res: requests.Response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_res.raise_for_status()
    articles = news_res.json()["articles"][:3]


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
# HINT 1: Think about using the Python Slice Operator
messages = [
    f"{STOCK}: {change_str}\nHeadline: {article['title']}\nBrief: {article['description']}"
    for article in articles
]
for msg in messages:
    print(f"{msg}\n")
# Send a separate message with each article's title and description to your phone number.
# HINT 1: Consider using a List Comprehension.


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
"""

