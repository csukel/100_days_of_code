import requests
import datetime as dt
import pandas

API_KEY = "3jEmEP_xXf9WjL6jTghlcrWRLTEfS6GH"
BASE_URI = "https://api.tequila.kiwi.com/"
LOCATION_ENDPOINT = f"{BASE_URI}locations/query"
SEARCH_ENDPOINT = f"{BASE_URI}v2/search"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.header = {"accept": "application/json", "apikey": API_KEY}

    def query_locations(self, **kwargs):
        query_params = {}
        term = kwargs.get("term")
        locale = kwargs.get("locale") or "en-US"
        location_types = kwargs.get("location_types")
        limit = kwargs.get("limit") or 10
        active_only = kwargs.get("active_only") or "true"

        query_params["locale"] = locale
        query_params["limit"] = limit
        query_params["active_only"] = active_only

        if term:
            query_params["term"] = term

        if location_types:
            query_params["location_types"] = location_types

        res: requests.Response = requests.get(
            url=LOCATION_ENDPOINT, headers=self.header, params=query_params
        )
        res.raise_for_status()
        return res.json()

    def search_flights(self, **kwargs):
        today = dt.datetime.now()
        tomorrow = today + dt.timedelta(days=1)
        after_6_months = today + pandas.DateOffset(months=6)
        query_params = {}
        query_params["curr"] = "GBP"
        query_params["vehicle_type"] = "aircraft"
        query_params["limit"] = kwargs.get("limit") or 10
        query_params["fly_from"] = "city:LON"
        query_params["fly_to"] = f"city:{kwargs.get('fly_to')}"
        query_params["max_stopovers"] = 0  # direct flight
        query_params["date_from"] = self._format_date(tomorrow)
        query_params["date_to"] = self._format_date(after_6_months)
        query_params['flight_type'] = "round"
        query_params["nights_in_dst_from"] = 7
        query_params["nights_in_dst_to"] = 28

        res: requests.Response = requests.get(
            uri=SEARCH_ENDPOINT, headers=self.header, params=query_params
        )
        res.raise_for_status()

        return res.json()

    def _format_date(date: dt.datetime) -> str:
        return date.strftime("%d/%m/%Y")
