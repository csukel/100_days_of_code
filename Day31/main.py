from tkinter import *
import pandas
import random
import time

# ------------------ CONSTANSTS -------------------------------------------#
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
TITLE_X = 400
TITLE_Y = 150
WORD_X = 400
WORD_Y = 253

# ------------------ CONTROLLER -------------------------------------------#
def save_progress():
	global data
	data.to_csv("Day31/data/words_to_learn.csv", index=False)

def on_accept():
	global current_word, data
	row_idx = current_word.index[0]
	print(current_word)
	data = data[data.French != current_word.French.values[0]]
	print(len(data))
	save_progress()
	next_card()

def on_reject():
	save_progress()
	next_card()

def read_data():
	try:
		df = pandas.read_csv("Day31/data/words_to_learn.csv")
		print("Read data from words_to_learn.csv")
	except:
		df = pandas.read_csv("Day31/data/french_words.csv")
		print("Read data from french_words.csv")

	return df

def select_random_word():
	global data
	return data.iloc[[random.randint(0,len(data)-1)]]

def set_word(word, language):
	global id_title, id_word, current_word

	if language == "English":
		fill_color = "white"
	else:
		fill_color = "black"

	canvas.itemconfig(id_title, text=language, fill=fill_color)
	canvas.itemconfig(id_word, text=word[language].values[0], fill=fill_color)

	current_word = word

def next_card():
	global id_sleep
	canvas.itemconfig(id_card_background, image=img_card_front)
	word = select_random_word()
	set_word(word, "French")
	id_sleep = window.after(3000, flip_card, word )


def flip_card(word):
	set_word(word, "English")
	canvas.itemconfig(id_card_background, image=img_card_back)

# ------------------ UI SETUP -------------------------------------------#
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


#Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
img_card_back = PhotoImage(file="Day31/images/card_back.png")
img_card_front = PhotoImage(file="Day31/images/card_front.png")
id_card_background = canvas.create_image(400, 260, image=img_card_front)
id_title = canvas.create_text(TITLE_X, TITLE_Y, text="Title", font=TITLE_FONT)
id_word = canvas.create_text(WORD_X, WORD_Y, text="Word", font= WORD_FONT)
canvas.grid(column=0, columnspan=2, row=0)

#Button X
img_wrong = PhotoImage(file="Day31/images/wrong.png")
btn_negative = Button(image=img_wrong, highlightthickness=0, bg=BACKGROUND_COLOR)
btn_negative.grid(column=0, row=2)
btn_negative.config(command=on_reject)

#Button ✔
img_right = PhotoImage(file="Day31/images/right.png")
btn_positive = Button(image=img_right, highlightthickness=0, bg=BACKGROUND_COLOR)
btn_positive.grid(column=1, row=2)
btn_positive.config(command=on_accept)

data = read_data()
# Pick the first word
next_card()


window.mainloop()


