import requests
API_KEY = "5a37c79b9160340124c002d03c201880"
MY_LAT = 35.185566
MY_LONG = 33.382275

ONE_CALL = "https://api.openweathermap.org/data/3.0/onecall"
WEATHER = "https://api.openweathermap.org/data/2.5/weather"
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

parameters = {
	"lat" : MY_LAT,
	"lon" : MY_LONG,
	"appid" : API_KEY
}
res = requests.get(WEATHER, params=parameters)
res.raise_for_status()

data = res.json()
print(data)
