from bs4 import BeautifulSoup
import lxml
import requests


res = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

titles = soup.select(selector="h3[class='title']")
titles_text = ""
for title in reversed(titles):
	titles_text += f"{title.getText()}\n"

with open("Day45/top-100-movies/movies.txt", "w", encoding="utf-8") as file:
	file.write(titles_text)