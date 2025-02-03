import requests
import datetime as dt
#How you get data from an API

MY_LAT = 23.211178
MY_LONG = -47.524784

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# #Give an HTTP code - response.status_code
# # 2xx is an ok return
#
# #Get the data from request
# data = response.json()["iss_position"]["longitude"]
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# coordinate = (latitude,longitude)
# response.raise_for_status()

parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
}

#Code with parameters in url https://api.sunrise-sunset.org/json?lat=23.211178&lng=-47.524784
response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")
sunset = data["results"]["sunset"].split("T")[1].split(":")

#Get the hour with the formatted 0 to 12 am or pm and dividing the string until get the hour
# print(sunrise.split("T")[1].split(":")[0])
time_now = dt.datetime.now()



