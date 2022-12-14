import requests
import os

sheety_username = os.environ.get('D39_sheety_username')
sheety_pass = os.environ.get('D39_basicauth_pass')
sheety_endpoint = f'https://api.sheety.co/{sheety_username}/kopiaFlightDeals/prices'


# print(sheety_username + '\n' + sheety_pass + '\n' + sheety_endpoint)

class DataManager:
    def __init__(self):
        self.sheety_data = {}

    def get_data(self):
        sheety_get = requests.get(url=sheety_endpoint, auth=(sheety_username, sheety_pass))
        self.sheety_data = sheety_get.json()['prices']

    def put_IATA(self):
        for data in self.sheety_data:
            data_change = {
                'price': {
                    'iataCode': data['iataCode']
                }
            }
            sheety_put = requests.put(url=f'{sheety_endpoint}/{data["id"]}', auth=(sheety_username, sheety_pass),
                                      json=data_change)
            print(sheety_put.text)
