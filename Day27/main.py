# import tkinter
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(side="top")

my_label["text"] = "My text"
my_label.config(text="New Text")

#Button
def button_clicked():
	my_label["text"] = "Button got clicked!"

button = Button(text="Click Me", command=button_clicked)
button.pack()

#Entry
input = Entry()
input.pack()
def print_input_text():
	print(input.get())
	my_label['text'] = input.get()

button2 = Button(text="Print", command=print_input_text)
button2.pack()


window.mainloop()