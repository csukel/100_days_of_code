from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
	password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
	password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

	random.shuffle(password_list)

	password = "".join(password_list)

	entry_password.delete(0, END)
	entry_password.insert(0, password)
	pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
	website = entry_website.get()
	username = entry_username.get()
	password = entry_password.get()

	if not website:
		messagebox.showwarning(title="Invalid data", message="Please provide a valid website")
		entry_website.focus()
		return

	if not username:
		messagebox.showwarning(title="Invalid data", message="Please provide a valid username")
		entry_username.focus()
		return

	if not password:
		messagebox.showwarning(title="Invalid data", message="Please provide a valid password")
		entry_password.focus()
		return

	# proceed = messagebox.askokcancel(title=website, 
	# 							  message=f"These are the details entered: \nEmail: {username}"\
	# 									f"\nPassword: {password} \nIs it ok to save?")
	
	# if proceed:
	#save password to file
	try:
		with open("Day29/password-manager-start/data.json", "r") as file:
			# file.write(f"{website} | {username} | {password}\n")
			data = json.load(file)
	except:
		data = {}

	with open("Day29/password-manager-start/data.json", "w") as file:
		data.update({website: {
				"email" : username,
				"password": password
			}})
		json.dump(data, file, indent=4)
		#reset website and passowrd fields
		entry_website.delete(0, END)
		entry_password.delete(0, END)
		messagebox.showinfo("Info","Password stored successfully.")

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
	query = entry_website.get()

	try:
		with open("Day29/password-manager-start/data.json", "r") as file:
			# file.write(f"{website} | {username} | {password}\n")
			data = json.load(file)
	except:
		data = {}

	website = data.get(query)

	if website is None:
		message = "No match found."
	else:
		message = f"Email: {website.get('email')}\nPassword: {website.get('password')}"

	messagebox.showinfo(f"{query}", message)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Passord Manager")
window.config(padx=50, pady=50)

#Logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="Day29/password-manager-start/logo.png")
canvas.create_image(100, 100, image= logo_img)
canvas.grid(column=1, row=0)

#Form

#1.Website
lbl_wwebsite = Label(text="Website:")
lbl_wwebsite.grid(column=0, row=1)

entry_website = Entry(width=25)
entry_website.grid(column=1, row=1)
entry_website.focus()

btn_search = Button(text="Search", width=15)
btn_search.grid(column=2, row=1)
btn_search.config(command=search)

#2.Email/Username
lbl_username = Label(text="Email/Username:")
lbl_username.grid(column=0, row=2)

entry_username = Entry(width=45)
entry_username.insert(0, "loukkis91@gmail.com")
entry_username.grid(column=1, columnspan=2, row=2)

#3.Password
lbl_password = Label(text="Password:")
lbl_password.grid(column=0, row=3)

entry_password = Entry(width=26)
entry_password.grid(column=1, row=3)

btn_gen_pass = Button(text="Generate Password")
btn_gen_pass.grid(column=2, row=3)
btn_gen_pass.config(command=generate_password)

#4.Add
btn_add = Button(text="Add", width=40)
btn_add.grid(column=1, columnspan=2, row=4)
btn_add.config(command=save_password)

window.mainloop()
