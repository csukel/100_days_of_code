import requests
from datetime import datetime
TOKEN = "abc1234lostylianou"
USERNAME = "csukel91"
GRAPHID = "graph1"
pixela_uri = "https://pixe.la/"
today = datetime.now().strftime("%Y%m%d")
graph_endpoint = f"{pixela_uri}v1/users/{USERNAME}/graphs/{GRAPHID}/{today}"

header_param = {
	"X-USER-TOKEN": TOKEN
}


request_data = {
	"quantity": "47.30"
}

res = requests.put(url=graph_endpoint, headers=header_param, json=request_data)
#{'message': 'Success.', 'isSuccess': True}
res.raise_for_status()
print(res.json())
