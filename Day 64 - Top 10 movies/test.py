import requests
import os

api_key = os.environ.get('d64_api_key')
# new_movie_title = input()
parameters = {
    'api_key': api_key,
    'query': 'Matrix',
    'language': 'en-US',
    'page': 1,
    'include_adult': 'false',
}

response = requests.get(f'https://api.themoviedb.org/3/search/movie', params=parameters)
data = response.json()
movies = data['results']

for movie in movies:
    print(movie)

