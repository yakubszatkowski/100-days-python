# google sheet: https://docs.google.com/spreadsheets/d/1hstsd-4wgTkc8-hVL4DeCSlVsiwpPgdWnaE7oe87S7s/edit#gid=0
import requests
import os
from datetime import datetime

activity = input('Which exercises you\'ve done? ')
GENDER = 'male'
WEIGHT = 72
HEIGHT = 171
AGE = 28

nutritionix_app_id = os.environ.get('D38_nutritionix_id')
nutritionix_key = os.environ.get('D38_nutritionix_key')
nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
headers = {
    'x-app-id': nutritionix_app_id,
    'x-app-key': nutritionix_key,
}
post_body = {
    'query': activity,
    'gender': GENDER,
    'weight_kg': WEIGHT,
    'height_cm': HEIGHT,
    'age': AGE
}
response_exercise = requests.post(url=nutritionix_endpoint, json=post_body, headers=headers)
exercises = response_exercise.json()['exercises']
# os.environ.get('D38_bearer_token')
headers = {
    'Authorization': f'Bearer {os.environ["D38_bearer_token"]}'  # difference between environ[] and environ.get()
}
sheety_username = os.environ.get('D38_sheety_username')
sheety_endpoint = f'https://api.sheety.co/{sheety_username}/kopiaMyWorkouts/workouts'
for exercise in exercises:
    sheety_body = {
        'workout': {
            'date': datetime.now().strftime('%d/%m/%Y'),
            'time': datetime.now().strftime('%H:%M:%S'),
            'exercise': exercise['user_input'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
        }
    }
    response_sheety = requests.post(url=sheety_endpoint, json=sheety_body, headers=headers)
    print(response_sheety.text)
