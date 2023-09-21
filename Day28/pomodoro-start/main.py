from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
	global reps
	reps += 1
	work_sec = WORK_MIN * 60
	short_break_sec = SHORT_BREAK_MIN * 60
	long_break_sec = LONG_BREAK_MIN * 60

	#long break
	if reps % 8 == 0:
		count_down(long_break_sec)
		lbl_timer.config(text='Long Break', fg=RED)
	#Short break
	elif reps % 2 == 0:
		count_down(short_break_sec)
		lbl_timer.config(text='Short Break', fg=PINK)
	else:#work
		count_down(work_sec)
		lbl_timer.config(text='Work', fg=GREEN)

def reset_timer():
	global reps, timer
	reps = 0
	window.after_cancel(timer)
	lbl_timer.config(text="Timer", fg=GREEN)
	change_timer_text('%02d:%02d' % (0, 0))
	lbl_checked.config(text="")


def change_timer_text(text):
	canvas.itemconfig(timer_text, text=text)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def convert(seconds):
    min, sec = divmod(seconds, 60)
    return '%02d:%02d' % (min, sec)


def count_down(count):
	global timer
	change_timer_text(convert(count))
	if count >= 0:
		timer = window.after(1000, count_down, count - 1)
	else: 
		start_timer()
		if reps % 2 == 0:
			lbl_checked.config(text="✔"* (reps // 2))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#Timer
lbl_timer = Label(text="Timer",fg=GREEN, bg=YELLOW , font=(FONT_NAME, 50, "bold"))
lbl_timer.grid(column=1,row=0)

#Canvas with tomatoe image and timer value
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Day28/pomodoro-start/tomato.png")
canvas.create_image(100, 112, image= tomato_img)
timer_text = canvas.create_text(103, 125, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1,row=1)

#Button start
btn_start = Button(text="Start", font=(FONT_NAME, 12, "bold"), bg="white", highlightthickness=0)
btn_start.grid(column=0, row=2)
btn_start.config(command=start_timer)

#Button reset
btn_reset = Button(text="Reset", font=(FONT_NAME, 12, "bold"), bg="white", highlightthickness=0)
btn_reset.grid(column=2, row=2)
btn_reset.config(command=reset_timer)


#Checked label
lbl_checked = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14, "normal"))
lbl_checked.grid(column=1, row=3)



window.mainloop()