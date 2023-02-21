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
    title = movie['original_title']
    img_url = f'https://image.tmdb.org/t/p/w600_and_h900_bestv2/{movie["poster_path"]}'
    year = movie['release_date']
    description = movie['overview']
    movie_api_id = movie['id']
    print(title, movie_api_id)


