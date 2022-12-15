# https://docs.google.com/spreadsheets/d/1-IX5xYzCXwkaCIvxxaSqCmXO3E4DoqaIWXFkXU3eOYg/edit#gid=0
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_managment = DataManager()
data_managment.get_data()
sheet_data = data_managment.sheety_data
flight_search = FlightSearch()
notification = NotificationManager()
travel_from = 'LON'

empty_row = True
for row in sheet_data:
    if row['iataCode'] == "":
        row['iataCode'] = flight_search.return_IATA(row["city"])
        empty_row = False

if not empty_row:
    data_managment.put_IATA()

for destination in sheet_data:
    flight = flight_search.check_flights(travel_from, destination["iataCode"])
    pound = '£'.encode('utf-8')
    # link = f'\nhttps://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.' \
    #        f'{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}'
    link = f'https://www.google.com/travel/flights?q=Flights%20to%20{flight.destination_airport}%20from%20' \
           f'{flight.destination_airport}%20on%20{flight.out_date}%20through%20{flight.return_date}'
    msg = f'Only {pound}{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} ' \
          f'to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} ' \
          f'to {flight.return_date}. {link}'
    # print(destination['lowestPrice'])
    try:  # different approach >if flight is none: >continue
        # also another if with += rest of msg would work
        if destination['lowestPrice'] > flight.price and flight.stop_overs == 1:
            notification.send(message=f'{msg}\n\nFlight has {flight.stop_overs} stop overs, via {flight.via_city}.')
        elif destination['lowestPrice'] > flight.price:
            notification.send(message=msg)
    except AttributeError:
        continue
