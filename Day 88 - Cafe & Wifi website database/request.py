import os
from requests_cache import CachedSession, SQLiteCache
from time_format import format_weekday_text
import textwrap

current_dir = os.path.dirname(__file__)
cache_path = os.path.join(current_dir, '.cache', 'http_cache.sqlite')

backend = SQLiteCache(cache_path)  # could've also split the databases on APIs' requests
session = CachedSession(expire_after=60*60*24*29, backend=backend)

class RequestCafePlaces:

    def __init__(self):
        self.API_KEY = os.environ.get("Google_API_KEY")
        self.keyword = 'kawiarnia'


    def nearby_search(self, geolocation):
        LAT, LNG = geolocation[0], geolocation[1]
        location = f'{LAT},{LNG}'

        self.nearby_search_params = {
            'key': self.API_KEY,
            'keyword': self.keyword,
            'location': location,
            'radius': 5000,
            'types': ['restaurant', 'cafe', 'establishment'],
            'fields': 'id'
        }

        response = session.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json', params=self.nearby_search_params)
        print(f'\nnearby_search cache key: {response.cache_key} \nIs cached: {response.from_cache} \nExpires at: {response.expires}')
        nearby_search_data = response.json()

        return nearby_search_data


    def place_details(self, place_id):
        self.place_details_params = {
            'key': self.API_KEY,
            'place_id': place_id
        }
        response = session.get('https://maps.googleapis.com/maps/api/place/details/json', params=self.place_details_params)
        print(f'\nplace_details cache key: {response.cache_key} \nIs cached: {response.from_cache} \nExpires at: {response.expires}')
        place_details_data = response.json()

        return place_details_data


    def query_results(self, geolocation):
        list_of_nearby_places = []
        nearby_search_data = self.nearby_search(geolocation)
        
        for business in nearby_search_data['results']:  # change to normal later

            place_details_data = self.place_details(business['place_id'])['result']
            place_id = business['place_id']
            name =  textwrap.fill(business['name'], 36).split('\n')[0]
            rating = business['rating']
            user_ratings_total = business['user_ratings_total']
            address = business['vicinity']
            phone_number = place_details_data.get('formatted_phone_number', 'Not available')
            website = place_details_data.get('website', 'Not available')

            opening_hours = place_details_data.get('current_opening_hours', 'Not available')
            if opening_hours != 'Not available':
                opening_hours = opening_hours['weekday_text']
                weekday_info = format_weekday_text(opening_hours)


            list_of_nearby_places.append(
                {
                    'place_id': place_id,
                    'name': name,
                    'rating': rating,
                    'user_ratings_total': user_ratings_total,
                    'address': address,
                    'opening_hours': weekday_info,
                    'phone_number': phone_number,
                    'website': website,
                }
            )

        return list_of_nearby_places

