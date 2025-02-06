import requests
from environs import Env
import datetime as dt

env = Env()
env.read_env()

APP_ID = env.str("NUTRITIONIX_APP_ID")
APP_KEY = env.str("NUTRITIONIX_APP_KEY")
SHEET_TOKEN = env.str("SHEET_TOKEN")

WEIGHT_KG = 71
HEIGHT_CM = 168
AGE = 18

date = dt.datetime.now()
TODAY = date.strftime("%d/%m/%Y")
NOW = date.strftime("%X")

#NUTRIONIX API - https://trackapi.nutritionix.com/docs/#/default/post_v2_natural_exercise

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

nutri_response = requests.post(url=exercise_endpoint,json=exercise_param,headers=headers)
# print(nutri_response.json())
nutri_data = nutri_response.json()['exercises']
# print(nutri_data)

#SHEETY API - https://dashboard.sheety.co/projects/67a4ae2e7c36d479f76d144a

sheet_endpoint = "https://api.sheety.co/8ef5eb6b682a3ffd693f688ef3eaeb5b/myWorkoutsJoãoCalsavara/workouts"

headers={
    "Authorization": f"Bearer {SHEET_TOKEN}",
}
# request_sheet = requests.get(url=sheet_endpoint,headers=headers)
for exercise in nutri_data:
    sheet_json ={
        'workout':{
            "date": TODAY,
            "time": NOW,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    }

    response_sheet = requests.post(
        url=sheet_endpoint,
        json=sheet_json,
        headers=headers)
    print(response_sheet.text)