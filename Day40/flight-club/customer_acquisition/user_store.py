from user import User
from typing import List
from google_api import GoogleCloud
import pygsheets
import pandas

class UserStore():
	
	def __init__(self, gc: GoogleCloud) -> None:
		self.users : List(User) = []
		self.gc = gc
		self.flight_club_sheet : pygsheets.Spreadsheet = self.gc.client.open_by_key('1DX297TIvo7RHmlZnUMeVLbNKjAOrmRnQVp-Mqw5z4BQ')
		self.users_wrksheet : pygsheets.Worksheet = self.flight_club_sheet.worksheet('title','Users')
		self.users_df : pandas.Dataframe = self.users_wrksheet.get_as_df(has_header=True)


	def load_users(self) -> None:
		for i, row in self.users_df.iterrows():
			user = User(row['First Name'], row['Last Name'], row['Email'])
			self.add_user_to_list(user)

	def add_user(self, user: User) -> None:
		# Add to in memory list
		self.add_user_to_list(user)
		# Add to dataframe
		self.users_df.loc[len(self.users_df.index)] = user.to_list()
		# Update worksheet in google sheets
		self.users_wrksheet.set_dataframe(self.users_df, (1,1))

	def add_user_to_list(self, user: User) -> None:
		self.users.append(user)

	def find_user_by_email(self, email: str) -> User:
		return next(
			(user for user in self.users if user.email == email),
			None
		)
	
	def sign_up(self):
		first_name = input("What is your first name?\n")
		last_name = input("What is your last name?\n")
		email = input("What is your email?\n")

		user = User(first_name, last_name, email)
		self.add_user(user)