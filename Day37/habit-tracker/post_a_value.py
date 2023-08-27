import requests
from datetime import datetime

TOKEN = "abc1234lostylianou"
USERNAME = "csukel91"
GRAPHID = "graph1"
pixela_uri = "https://pixe.la/"
graph_endpoint = f"{pixela_uri}v1/users/{USERNAME}/graphs/{GRAPHID}"

header_param = {"X-USER-TOKEN": TOKEN}

today = datetime.now().strftime("%Y%m%d")


request_data = {"date": today, "quantity": "65.34"}


res = requests.post(url=graph_endpoint, headers=header_param, json=request_data)
# {'message': 'Success.', 'isSuccess': True}
res.raise_for_status()

