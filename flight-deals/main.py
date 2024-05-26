from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
import requests

#USE THIS TO CONVERT GBP TO USD in LINE 20
CURRENCY_CONVERSION_FACTOR = 1.27

datamanager = DataManager()
sheet_data = datamanager.get_data()
#FOR TESTING PURPOSES, SAVE sheet_data TO NOT WASTE API CALLS
# sheet_data_backup = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 300, 'id': 3}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}]

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        row["lowestPrice"] *= CURRENCY_CONVERSION_FACTOR
    datamanager.destination_data = sheet_data
    datamanager.update_destination_codes()

for city in sheet_data:
    flight_search = FlightSearch()
    flight = flight_search.get_flight(city["iataCode"])
    if float(flight.price) < city["lowestPrice"]:
        message = (f"Low price alert! Only ${flight.price} to fly from {flight.origin_city} {flight.origin_airport} to {city["city"]} {flight.destination_city}, "
                   f"from {flight.out_date} to {flight.return_date}.")
        nm = NotificationManager()
        nm.send_messages(message)