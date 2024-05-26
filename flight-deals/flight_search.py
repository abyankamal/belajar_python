import requests
from datetime import date, timedelta
import pprint
from flight_data import FlightData

#FOR TOKEN
API_KEY = "Idk7TOrkXj5ZPeSPXZ6GltJPo2qtWQ1i"
API_SECRET = "Mxui0WwhAIr2WZB0"
AMADEUS_AUTH_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
BODY_TOKEN = {
    "grant_type":"client_credentials",
    "client_id":API_KEY,
    "client_secret":API_SECRET,
}
HEADER_TOKEN = {
    "Content-Type": "application/x-www-form-urlencoded"
}
#FOR IATA CODE
CITY_SEARCH_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

#FOR FLIGHT SEACH
URL= "https://test.api.amadeus.com/v2/shopping/flight-dates"
ORIGIN_CITY = "LONDON"

days_after = (date.today() + timedelta(days=30)).isoformat()

class FlightSearch:
    def __init__(self):
        self.TOKEN = ""

    def get_token(self):
        response = requests.post(AMADEUS_AUTH_ENDPOINT, data=BODY_TOKEN, headers=HEADER_TOKEN)
        self.TOKEN = response.json()["access_token"]
        return self.TOKEN

    def get_destination_code(self, city_name):
        PARAMS = {
            "keyword": [city_name],
        }
        headers = {
            "Authorization": f"Bearer {self.get_token()}"
        }
        response = requests.get(url=CITY_SEARCH_ENDPOINT, params=PARAMS, headers=headers)
        data = response.json()
        code = data["data"][0]["iataCode"]
        return code

    def get_flight(self, city):
        PARAMS = {
            "originLocationCode": "LON",
            "destinationLocationCode": f"{city}",
            "departureDate": f"{days_after}",
            "adults": 2,
            "nonStop": "true",
        }
        headers = {
            "Authorization": f"Bearer {self.get_token()}"
        }
        response = requests.get(url=URL, params=PARAMS, headers=headers)
        data = response.json()
        pprint.pprint(data)
        flight_data = FlightData(
            price=data["data"][0]["price"]["total"],
            origin_city=ORIGIN_CITY,
            origin_airport=data["data"][0]["origin"],
            destination_city=city,
            destination_airport=data["data"][0]["destination"],
            out_date=data["data"][0]["departureDate"],
            return_date=data["data"][0]["returnDate"])
        return flight_data


#Sample data from get_flight function:
# pprint.pprint({'data': [{'type': 'flight-date', 'origin': 'LGW', 'destination': 'JFK', 'departureDate': '2024-09-09', 'returnDate': '2024-09-23', 'price': {'total': '353.98'}, 'links': {'flightDestinations': 'https://test.api.amadeus.com/v1/shopping/flight-destinations?origin=LON&departureDate=2024-05-19,2024-11-15&oneWay=false&duration=7,28&nonStop=true&viewBy=DATE', 'flightOffers': 'https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=LON&destinationLocationCode=NYC&departureDate=2024-09-09&returnDate=2024-09-23&adults=1&nonStop=true'}}]})
