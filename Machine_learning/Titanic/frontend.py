"""A model to predict who would survive the titanic"""

import tkinter
import backend

from tkinter import messagebox


# --- Constants ---
FONT10 = ("comfortaa", 10)
FONT11 = ("comfortaa", 11)
PADS = {"padx": 10, "pady": 10}


# --- Tkinter GUI ---
window = tkinter.Tk()
window.title = "Who Will Survive?"

# Title
title = tkinter.Label(master=window, text="Titanic - who will survive?", font=FONT11)
title.grid(column=2, columnspan=5, row=0, **PADS)

# Left (User input)
titleL = tkinter.Label(master=window, text="User Input", font=FONT10)
titleL.grid(column=0, columnspan=2, row=1, **PADS)

labelL0 = tkinter.Label(master=window, text="Pclass: ", font=FONT10)
labelL0.grid(column=0, row=2, **PADS)
entry0 = tkinter.Entry(master=window, font=FONT10)
entry0.grid(column=1, row=2, **PADS)
labelL1 = tkinter.Label(master=window, text="Name: ", font=FONT10)
labelL1.grid(column=0, row=3, **PADS)
entry1 = tkinter.Entry(master=window, font=FONT10)
entry1.grid(column=1, row=3, **PADS)
labelL2 = tkinter.Label(master=window, text="Sex: ", font=FONT10)
labelL2.grid(column=0, row=4, **PADS)
entry2 = tkinter.Entry(master=window, font=FONT10)
entry2.grid(column=1, row=4, **PADS)
labelL3 = tkinter.Label(master=window, text="Age: ", font=FONT10)
labelL3.grid(column=0, row=5, **PADS)
entry3 = tkinter.Entry(master=window, font=FONT10)
entry3.grid(column=1, row=5, **PADS)
labelL4 = tkinter.Label(master=window, text="SibSp: ", font=FONT10)
labelL4.grid(column=0, row=6, **PADS)
entry4 = tkinter.Entry(master=window, font=FONT10)
entry4.grid(column=1, row=6, **PADS)
labelL5 = tkinter.Label(master=window, text="Parch: ", font=FONT10)
labelL5.grid(column=0, row=7, **PADS)
entry5 = tkinter.Entry(master=window, font=FONT10)
entry5.grid(column=1, row=7, **PADS)
labelL6 = tkinter.Label(master=window, text="Fare: ", font=FONT10)
labelL6.grid(column=0, row=8, **PADS)
entry6 = tkinter.Entry(master=window, font=FONT10)
entry6.grid(column=1, row=8, **PADS)
labelL7 = tkinter.Label(master=window, text="Embarked: ", font=FONT10)
labelL7.grid(column=0, row=9, **PADS)
entry7 = tkinter.Entry(master=window, font=FONT10)
entry7.grid(column=1, row=9, **PADS)


def predict():
	entries = entry0.get(), entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get(), entry7.get()
	if all(map(len, entries)):
		pClass, name, sex, age, sibSp, parch, fare, embarked = entries
		# We know they're all there, check they're all acceptable
		if all(map(lambda x: x.isnumeric(), [pClass, age, sibSp, parch, fare]))\
				and all(map(lambda x: x.isalpha(), [name, sex, embarked])):
			pass
		else:
			messagebox.showerror("Invalid Input", "One, or more, inputs are of the wrong type\nPlease consult the input help")
	else:
		messagebox.showerror("Invalid Input", "One, or more, inputs are missing")


submit = tkinter.Button(master=window, text="Submit", command=predict, font=FONT10)
submit.grid(column=0, columnspan=2, row=10, **PADS)

tkinter.mainloop()
