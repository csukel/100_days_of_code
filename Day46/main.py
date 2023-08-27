from datetime import datetime
from bs4 import BeautifulSoup
import lxml
import requests

BASE_URI = "https://www.billboard.com/charts/hot-100/"

date_format = "%Y-%m-%d"
while True:
	date = input("Which year do you want to travel? Type the date in this format YYYY-MM-DD: ")
	try:
		bool(datetime.strptime(date, date_format))
		break
	except ValueError:
		print("Wrong input. Please try again.")

res = requests.get(f"{BASE_URI}{date}")
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

songs = soup.select(selector="li>h3.c-title")
song_titles = [song.getText().replace('\n','').replace('\t','') for song in songs]
print(song_titles)
# print(len(song_titles))