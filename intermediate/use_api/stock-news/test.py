import requests
import datetime as dt
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

day = dt.datetime.now().date() - dt.timedelta(days=1)
news_parameters = {
        "apiKey": "78bd991862ab401dacca05cf031e99d4",
        "q": COMPANY_NAME,
        "from": day,
        "to": day,
        "sortBy": "popularity",
        "language": "en",
        "pageSize": 3,

    }

connection_news = requests.get(NEWS_ENDPOINT, params=news_parameters)
connection_news.raise_for_status()
data_news = connection_news.json()["articles"]

articles_data = [f"Headline: {article['title']}\nBrief:{article['description']}" for article in data_news]

percentage_difference = 5
if percentage_difference >0:
    final_mensage = [f"{STOCK}: 🔺{percentage_difference}%\n{article} "for article in articles_data]
else:
    final_mensage = [f"{STOCK}: 🔻{percentage_difference}%\n{article} "for article in articles_data]
for message in final_mensage:
    print(message)