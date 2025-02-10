import requests
from environs import Env
import datetime as dt

env = Env()
env.read_env()
today = dt.datetime.now()

USERNAME = "jpcalsavara"
TOKEN=env.str("PIXELA_TOKEN")
GRAPH_ID = "graph1"
#Function to learn how to format date https://www.w3schools.com/python/python_datetime.asp
DATE = today.strftime("%Y%m%d")


pixela_endpoint = "https://pixe.la/v1/users"

#Create a user by using post method in an API
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes",
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

##POST CASE - Create a graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id":"graph1",
    "name":"Programming Graph",
    "unit":"minutes",
    "type":"float",
    "color":"sora",
}

#Like a key but send separate from parameters
headers = {
    "X-USER-TOKEN": TOKEN
}
#
# response = requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(response)

##POST CASE - Create PIXEL

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_params ={
    "date": DATE,
    "quantity": input("How many minutes did you study programming? "),
}

response = requests.post(url=pixel_endpoint,json=pixel_params,headers=headers)
print(response.text)

##PUT CASE - Uptade Pixel

# put_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"
#
# put_pixel_params ={
#     "quantity": "30"
# }
#
# response = requests.put(url=put_pixel_endpoint,json=put_pixel_params,headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"


response = requests.delete(url=delete_pixel_endpoint,headers=headers)
print(response.text)