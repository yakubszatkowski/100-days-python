import requests
import os

api_key = os.environ.get('d64_api_key')

# 605
parameters = {
    'api_key': api_key,
}

response = requests.get(f'https://api.themoviedb.org/3/movie/{605}', params=parameters)
movie_info = response.json()

print(movie_info)
