import os
import requests
from flight_data import FlightData
from datetime import datetime, timedelta

today = datetime.today()
max_date = today + timedelta(6 * 30)

tequila_api_key = os.environ['D39_tequila_api_key']
tequila_endpoint = 'https://api.tequila.kiwi.com'
header = {
    'apikey': tequila_api_key
}


class FlightSearch:
    def return_IATA(self, city):
        parameters = {
            'term': city,
            'locale': 'en-US',
            'location_types': 'city',
            'limit': 10,
            'active_only': True,
        }
        response_code = requests.get(url=f'{tequila_endpoint}/locations/query', params=parameters, headers=header)
        code = response_code.json()['locations'][0]['code']
        return code

    def check_flights(self, origin_city_code, destination_city_code):
        parameters = {
            'fly_from': origin_city_code,
            'fly_to': destination_city_code,
            'date_from': today.strftime("%d/%m/%Y"),
            'date_to': max_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "GBP",
            "max_stopovers": 0,
        }
        response = requests.get(url=f"{tequila_endpoint}/v2/search", headers=header, params=parameters)
        try:
            data = response.json()['data'][0]
        except IndexError:
            parameters['max_stopovers'] = 2
            except_response = requests.get(url=f"{tequila_endpoint}/v2/search", headers=header, params=parameters)
            except_data = except_response.json()['data'][0]
            flight_data = FlightData(
                price=except_data['price'],
                origin_city=except_data['cityFrom'],
                origin_airport=except_data['flyFrom'],
                destination_city=except_data['cityTo'],
                destination_airport=except_data['flyTo'],
                out_date=except_data['route'][0]['local_departure'].split('T')[0],
                return_date=except_data['route'][-2]['local_departure'].split('T')[0],
                stop_overs=1,
                via_city=except_data['route'][0]['cityTo']
            )
            print(f'{flight_data.destination_city}: £{flight_data.price}')
            return flight_data
        else:
            flight_data = FlightData(
                price=data['price'],
                origin_city=data['route'][0]['cityFrom'],
                origin_airport=data['route'][0]['flyFrom'],
                destination_city=data['route'][0]['cityTo'],
                destination_airport=data['route'][0]['flyTo'],
                out_date=data['route'][0]['local_departure'].split('T')[0],
                return_date=data['route'][1]['local_departure'].split('T')[0]
            )
            print(f'{flight_data.destination_city}: £{flight_data.price}')
            return flight_data
