import pygsheets
import os

USERPROFILE = os.environ['USERPROFILE']
class GoogleCloud():
	def __init__(self) -> None:
		self.client = pygsheets.authorize(client_secret=f'{USERPROFILE}/Desktop/google_api/client_secret_878415065998-srg907ckusb2q2aulomfvmqn4ahjhqtq.apps.googleusercontent.com.json')
