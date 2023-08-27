import pandas
from flight_search import FlightSearch

class DataManager:
	#This class is responsible for talking to the Google Sheet.
	
	def __init__(self) -> None:
		self.flight_deals_data : pandas.DataFrame = pandas.read_csv("Day39/flight-deals-start/flight_deals.csv")

	def getData(self) -> pandas.DataFrame:
		return self.flight_deals_data
	
	def load_city_codes(self, fs: FlightSearch):
		df_without_code = self.getData()[self.getData()['IATA Code'].isna()]
		df_with_code = self.getData()[self.getData()['IATA Code'].notna()]
		for i, row in df_without_code.iterrows():
			city = row['City']
			data = fs.query_locations(term=city,location_types="city")
			for location in data['locations']:
				if location['name'] == city and location['code'] is not None:
					itacode = location['code']
					df_without_code.at[i, 'IATA Code'] = itacode
					# print(f"City {city} / IATA Code {itacode}")
					break
		df = pandas.concat([df_with_code, df_without_code])
		self.flight_deals_data = df