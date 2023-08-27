class User():
	def __init__(self, first_name, last_name, email) -> None:
		self.first_name = first_name
		self.last_name = last_name
		self.email = email

	def to_list(self):
		return [self.first_name, self.last_name, self.email]

	def __str__(self) -> str:
		return f"""
User Details
===============
First Name: {self.first_name}
Last Name: {self.last_name}
Email: {self.email}
==============

"""