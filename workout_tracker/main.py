import requests
from environs import Env

env = Env()
env.read_env()

APP_ID = env.str("NUTRITIONIX_APP_ID")
APP_KEY = env.str("NUTRITIONIX_APP_KEY")

WEIGHT_KG = 71
HEIGHT_CM = 168
AGE = 18

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id":APP_ID,
    "x-app-key":APP_KEY
}

exercise_param ={
    "query":input("Tell me which exercise you did: "),
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint,json=exercise_param,headers=headers)
print(response.text)