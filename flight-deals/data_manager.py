import requests

SHEETY_ENDPOINT = "https://api.sheety.co/d42b229f6c9e703db55afd8fb8e50bef/flightDeals/prices"
class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"],
                    "lowestPrice": city["lowestPrice"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)