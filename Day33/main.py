import requests
from datetime import datetime

MY_LAT = 35.185566
MY_LONG = 33.382275

res = requests.get("http://api.open-notify.org/iss-now.json")
data = res.json()
print(data)

iss_position = data["iss_position"]
lat = float(iss_position["latitude"])
long = float(iss_position["longitude"])

print(f"ISS Position Latitude {lat} / Longitude {long}")
print(f"My Position Latitude {MY_LAT} / Longitude {MY_LONG}")

# res = requests.get("http://api.open-notify.org/is-now.json")
# res.raise_for_status()

parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}

res = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
res.raise_for_status()
data = res.json()
# print(data)

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(f"Sunrise is at {sunrise} and sunset at {sunset}.")

now = datetime.now()

if (
    MY_LAT - 5 < lat < MY_LAT + 5
    and MY_LONG - 5 < long < MY_LONG + 5
    and (sunset <= now.hour or sunrise <= now.hour)
):
    print("Sending email")
