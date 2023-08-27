import requests
TOKEN = "abc1234lostylianou"
USERNAME = "csukel91"
pixela_uri = "https://pixe.la/"
graph_endpoint = f"{pixela_uri}v1/users/{USERNAME}/graphs"

header_param = {
	"X-USER-TOKEN": TOKEN
}

body_data = {
	"id" : "graph1",
	"name" : "Cycling Graph",
	"unit" : "Km",
	"type" : "float",
	"color" : "ajisai"
}

res = requests.post(url=graph_endpoint, headers=header_param, json=body_data)
#{'message': 'Success.', 'isSuccess': True}
res.raise_for_status()
print(res.json())