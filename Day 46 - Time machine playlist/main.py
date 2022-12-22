import os
import spotipy
from pprint import pprint
import requests
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

URL = 'https://www.billboard.com/charts/hot-100/'
answer = input('Which year do you want to travel to?: (YYYY-MM-DD')
year = int(answer[0:4])

response = requests.get(URL+answer)
billboard_website = response.text
soup = BeautifulSoup(billboard_website, 'html.parser')
song_titles = soup.select(selector='li.lrv-u-width-100p h3#title-of-a-story')
song_list = [data.getText().strip() for data in song_titles]

spotify_id = os.environ.get('D46_spotify_if')  # miss-clicked should've been id instead of if
spotify_secret = os.environ.get('D46_spotify_secret')
spotify_redirect_URI = 'https://example.com'
scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_id, client_secret=spotify_secret,
                                               redirect_uri=spotify_redirect_URI, scope=scope))
user_id = sp.current_user()['id']

song_uris = []

for song_name in song_list:
    song_data = sp.search(q=f'track:{song_name} year:{year}', type='track', limit=1, market='US')
    try:
        uri = song_data['tracks']['items'][0]['uri']
    except IndexError:
        pass
    else:
        song_uris.append(uri)

playlist = sp.user_playlist_create(user_id, f'{answer} billboard 100 playlist', public=False)
playlist_id = playlist['id']
sp.playlist_add_items(playlist_id, song_uris)
