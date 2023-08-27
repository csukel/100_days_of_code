#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

dm = DataManager()
fs = FlightSearch()

dm.load_city_codes(fs)
print(dm.getData())

# print(fs.query_locations(term='Paris',location_types="city"))

