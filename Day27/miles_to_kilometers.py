from tkinter import *


window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=50)



#Row 0

miles_entry = Entry(width=7)
miles_entry.grid(column=1,row=0)


miles_label = Label(text='Miles')
miles_label.grid(column=2,row=0)
miles_label.config(padx=20)

#Row 1
op_label = Label(text="is equal to")
op_label.grid(column=0,row=1)

km_ouptut = Label(text="0")
km_ouptut.grid(column=1, row=1)
km_ouptut.config(padx=20)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

#Row 2
calculate_btn = Button(text="Calculate")
calculate_btn.grid(column=1, row=2)
def calculate():
	km = float(miles_entry.get()) * 1.6
	km_ouptut['text'] = f"{km}"
calculate_btn.config(command=calculate)

window.mainloop()

