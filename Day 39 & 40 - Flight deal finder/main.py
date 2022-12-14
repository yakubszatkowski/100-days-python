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
    print(destination['lowestPrice'])
    if destination['lowestPrice'] > flight.price:
        notification.send(message=f'Only {flight.price} pounds to fly from {flight.origin_city}-{flight.origin_airport}'
                                  f' to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} '
                                  f'to {flight.return_date}."')

