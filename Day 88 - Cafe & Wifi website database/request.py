import os
from requests_cache import CachedSession, SQLiteCache

backend = SQLiteCache('.cache/http_cache.sqlite')
session = CachedSession(expire_after=60*60*24*29, backend=backend)

class RequestCafePlaces:
    def __init__(self):
        self.API_KEY = os.environ.get("Google_API_KEY")
        self.keyword = str('kawiarnia')

    def nearby_search(self, geolocation):
        LAT, LNG = geolocation[0], geolocation[1]
        location = f'{LAT},{LNG}'

        self.nearby_search_params = {
            'key': self.API_KEY,
            'keyword': self.keyword,
            'location': location,
            'radius': 10000,
            'types': ['restaurant', 'cafe', 'establishment'],
            'fields': 'id'
        }

        response = session.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json', params=self.nearby_search_params)
        print(f'nearby_search key: {response.cache_key} \nIs cached: {response.from_cache} \nExpires at: {response.expires}')
        nearby_search_data = response.json()
        return nearby_search_data
    
    def place_details(self, place_id):
        self.place_details_params = {
            'key': self.API_KEY,
            'place_id': place_id
        }
        response = session.get('https://maps.googleapis.com/maps/api/place/details/json', params=self.place_details_params)
        print(f'place_details key: {response.cache_key} \nIs cached: {response.from_cache} \nExpires at: {response.expires}')
        place_details_data = response.json()
        return place_details_data



# TESTING
request_cafe = RequestCafePlaces()


# # NEARBY_SEARCH
# nearby_search_data = request_cafe.nearby_search((50.26489189999999, 19.0237815))
# for business in nearby_search_data['results']:
#     print(business['place_id'])


# PLACE_DETAILS
place_details_data = request_cafe.place_details('ChIJec0jSTrOFkcR_FSBdytaZZI')
print(place_details_data)


# # TEST IF CACHED
# print(session.cache.contains('0ae94cb83e13f6a9'))
# print(session.cache.urls())
