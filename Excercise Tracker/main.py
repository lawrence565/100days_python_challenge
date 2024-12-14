import os, dotenv
import requests, datetime

dotenv.load_dotenv()

# Natural and Exercise
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
GENDER = "male"
WEIGHT_KG = 113
HEIGHT_CM = 183
AGE = 21
endpoint = "https://trackapi.nutritionix.com/"
NL_for_nutrients = "v2/natural/nutrients"
instant_endpoint = "/v2/search/instant"
NL_for_exercise = "v2/natural/exercise"

# Sheety API
SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
SHEET_TOKEN = os.getenv("SHEET_TOKEN")

def get_exercise_data():
    exercise_text = input("Tell me which exercise you did: ")
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
    }
    exercise_params = {
        "query": exercise_text,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }
    response = requests.post(url=f"{endpoint}{NL_for_exercise}", json=exercise_params, headers=headers)
    response.raise_for_status()
    data = response.json()["exercises"]

    return data

def post_a_row():
    now = datetime.datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")

    exercises = get_exercise_data()

    headers = {
        "Authorization": SHEET_TOKEN,
    }

    for exercise in exercises:
        print("Exercise")
        params = {
            "workout": {
                "date": date,
                "time": time,
                "exercise": exercise["name"].title(),
                "calories": exercise["nf_calories"],
                "duration": exercise["duration_min"],
            }
        }
        print(params)

        response = requests.post(url=SHEET_ENDPOINT, json=params, headers=headers)
        response.raise_for_status()
        print(response.text)

post_a_row()

# def test_url():
#     headers = {
#         "Authorization": SHEET_TOKEN,
#     }
#     response = requests.get("https://api.sheety.co/854cce0fe880b4c4f9f6005261c20228/myWorkouts/workouts", headers=headers)
#     response.raise_for_status()
#     print(response.json())
#
# test_url()