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

res = requests.delete(url=graph_endpoint, headers=header_param)
#{'message': 'Success.', 'isSuccess': True}
res.raise_for_status()
print(res.json())

# curl -X DELETE https://pixe.la/v1/users/csukel91/graphs/graph1/20230910 -H 'X-USER-TOKEN:abc1234lostylianou'