from bs4 import BeautifulSoup
import lxml
import requests

http_headers = {
	"User-Agent" : "Defined",
	"Accept-Language" : "en-GB,en-US;q=0.9,en;q=0.8",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	"sec-fetch-dest": "document",
	"sec-ch-ua-platform": "Windows",
	"Accept-Encoding" : "gzip, deflate, br"

}

res = requests.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1", headers=http_headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
price_tag = soup.select_one(selector="span.a-offscreen")
print(price_tag.getText())
