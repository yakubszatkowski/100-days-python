import os
import requests

class RequestCafePlaces:
    def __init__(self):
        self.API_KEY = os.environ.get("Google_API_KEY")
        self.keyword = str('kawiarnia')

    def nearby_search(self, geolocation):
        LAT, LNG = float(geolocation[0]), float(geolocation[1])
        location = f'{LAT},{LNG}'

        self.nearby_search_params = {
            'key': self.API_KEY,
            'keyword': self.keyword,
            'location': location,
            'radius': 10000,
            'types': ['restaurant', 'cafe', 'establishment']
        }

        response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json', params=self.nearby_search_params)
        response.raise_for_status()
        data = response.json()
        return data
    
    def place_details(self, place_id):
        self.place_id = place_id
        
        self.place_details_params = {
            'key': self.API_KEY,
            'place_id': self.place_id
        }

        response = requests.get('https://maps.googleapis.com/maps/api/place/details/json', params=self.place_details_params)
        response.raise_for_status()
        data = response.json()
        return data


# testing
request_cafe = RequestCafePlaces()
data = request_cafe.place_details('ChIJZxoVH0jOFkcRZFxRPHusTbE')
print(data)