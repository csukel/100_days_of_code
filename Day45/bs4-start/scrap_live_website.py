from bs4 import BeautifulSoup
import lxml
import requests

res = requests.get("https://news.ycombinator.com/")
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

anchor_titles = soup.select("span.titleline>a") #select the anchor tag that is below a span with class titleline
# print(anchor_titles)

for index, title in enumerate(anchor_titles):
	print(f"{index + 1}. {title.getText()}")
