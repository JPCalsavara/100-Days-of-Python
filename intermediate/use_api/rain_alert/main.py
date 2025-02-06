import requests
from twilio.rest import Client
from environs import Env

env = Env()
env.read_env()# Carrega as variáveis do arquivo .env

key = env.str("OPENWEATHER_API_KEY")
account_sid = env.str("TWILIO_ACCOUNT_SID")
auth_token = env.str("TWILIO_AUTH_TOKEN")

url = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lon": -47.524784,
    "lat": -23.211178,
    "appid": key,
    "cnt": 4,
    "units": "metric",
    "lang": "pt"
}

response = requests.get(url, params=parameters)
if response.status_code == 200:
    weather_data = response.json()
else:
    print(f"Erro na requisição: {response.status_code}")

will_rain = False
for index in range(0, 4):
    weather_code = weather_data["list"][index]["weather"][0]["id"]
    if int(weather_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="Vai chover hoje. Lembre-se de levar um guarda-chuva!",
        to="whatsapp:+5515996690551"
    )
    print(message.sid)
