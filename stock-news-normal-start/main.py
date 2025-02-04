import os

import requests
import datetime as dt
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do arquivo .env
TWILIO_ACCOUNT_SID=os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN=os.getenv("TWILIO_AUTH_TOKEN")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


day = dt.datetime.now().date() - dt.timedelta(days=1)

stock_parameters = {
    "apikey":"ZR81BF4J20QB3V84",
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "interval":"60min",
    # "extended_hours":"false",
}

connection_stocks=requests.get(STOCK_ENDPOINT,params=stock_parameters)
connection_stocks.raise_for_status()
data_stocks = connection_stocks.json()["Time Series (Daily)"]


stock_information = [value for (key, value) in data_stocks.items()]
yesterday_data = stock_information[0]
yesterday_closing_price = float(yesterday_data["4. close"])


day_before_yesterday_data = stock_information[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

price_difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
absolute_price_difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

percentage_difference = (absolute_price_difference/yesterday_closing_price)*100

if percentage_difference > 5:
    news_parameters = {
        "apiKey": "78bd991862ab401dacca05cf031e99d4",
        "qInTitle": COMPANY_NAME,
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

    percentage_difference = round(percentage_difference,2)
    if percentage_difference > 0:
        final_menssage = [f"{STOCK}: 🔺{percentage_difference}%\n{article} "for article in articles_data]
    else:
        final_menssage = [f"{STOCK}: 🔻{percentage_difference}%\n{article} "for article in articles_data]

    client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)

    for article in articles_data:
        message = client.messages.create(
            body=article,
            from="+12762765256",
            to="+5515996690551",
        )


