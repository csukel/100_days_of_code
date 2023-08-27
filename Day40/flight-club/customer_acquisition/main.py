from user_store import UserStore
import os
from google_api import GoogleCloud

gc = GoogleCloud()
user_store = UserStore(gc)

welcome_msg = """
Welcome to Louca's Flight Club
We find the best flight deals and email you.
"""



while True:
	os.system('cls')
	print(welcome_msg)
	user_store.sign_up()
	

	keep_signing = input("Do you want to sign up (Yes/No) ? ")
	if keep_signing == "No":
		break

# print(user_store.users)
# user_store.load_users()

# print(user_store.users[0])