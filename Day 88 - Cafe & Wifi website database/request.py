import os
import requests

class RequestCafePlaces:
    def __init__(self):
        self.API_KEY = os.environ.get("Google_API_KEY")
        self.keyword = str('kawiarnia')

    def send_request(self, geolocation):
        LAT, LNG = float(geolocation[0]), float(geolocation[1])
        location = f'{LAT},{LNG}'

        self.params = {
            'keyword': self.keyword,
            'location': location,
            'radius': 10000,
            'key': self.API_KEY,
            'types': ['restaurant', 'cafe', 'establishment']
        }

        response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json', params=self.params)
        response.raise_for_status()
        data = response.json()
        return data
    
# request_cafe = RequestCafePlaces()
# request_cafe.send_request((50.26489189999999, 19.0237815))