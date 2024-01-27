import os
import requests

API_KEY = os.environ.get("Google_API_KEY")
keyword = str('kawiarnia')
LAT, LNG = 50.318329, 19.070110
location = f'{LAT},{LNG}'

params = {
    'keyword': keyword,
    'location': location,
    'radius': 5000,
    'key': API_KEY
}

response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json', params=params)
response.raise_for_status()
data = response.json()
print(data)