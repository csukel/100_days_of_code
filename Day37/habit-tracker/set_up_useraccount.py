import requests

pixela_uri = "https://pixe.la/"

pixela_users_endpoint = f"{pixela_uri}v1/users"


# Set up a user account 
create_user_data = {
	"token": "abc1234lostylianou",
	"username": "csukel91",
	"agreeTermsOfService": "yes",
	"notMinor" : "yes"
}
res = requests.post(url=pixela_users_endpoint, json=create_user_data )
#{'message': "Success. Let's visit https://pixe.la/@csukel91 , it is your profile page!", 'isSuccess': True}
res.raise_for_status()
data = res.json()
print(data)