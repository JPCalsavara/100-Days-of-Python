import requests
from twilio.rest import Client

key = "c8a50b06f7e76420358cd832678d81d9"
url = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "AC144391a5d3f0ffee80cadc3700787996"
auth_token = "f4791eacf4510dd6d6f07dc8337fcc0d"

parameters = {
    "lon": -47.524784,  # Longitude corrigida
    "lat": -23.211178,  # Latitude correta
    "appid": key,
    "cnt": 4,
    "units": "metric",  # Opcional, retorna temperatura em Celsius
    "lang": "pt"        # Opcional, retorna a resposta em português
}


response = requests.get(url, params=parameters)

if response.status_code == 200:
    weather_data = response.json()
    # print(weather_data)  # Exibe os dados recebidos
else:
    print(f"Erro na requisição: {response.status_code}")
    print(response.text)  # Mostra o erro retornado pela API

for index in range(0,4):
    weather_code = weather_data["list"][index]["weather"][0]["id"]
    if int(weather_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
      # messaging_service_sid='MGc16bbdcf1ee734a51768f7b5193d1c83',
      # body='Vai chover hoje. Lembre do guarda-chuva',
      # from_="+12762765256",
      # to="+55 15 99669 0551",
    from_="whatsapp:+14155238886",
    body="It's going to rain today. Remember to bring an umbrella",
    to="whatsapp:+5515996690551"
    )
    print(message.sid)
