"""A model to predict who would survive the titanic"""

import tkinter
import backend
import pandas
import re

from tkinter import messagebox


# --- Constants ---
FONT10 = ("comfortaa", 10)
FONT11 = ("comfortaa", 11)
PADS = {"padx": 10, "pady": 10}


# --- Get model ---
model = backend.makeModel()


# --- Tkinter GUI ---
window = tkinter.Tk()
window.title = "Who Will Survive?"

# Title
title = tkinter.Label(master=window, text="Titanic - who will survive?", font=FONT11)
title.grid(column=2, columnspan=5, row=0, **PADS)

# Left (User input)
titleL = tkinter.Label(master=window, text="User Input", font=FONT10)
titleL.grid(column=0, columnspan=2, row=1, **PADS)

labelL0 = tkinter.Label(master=window, text="pClass: ", font=FONT10)
labelL0.grid(column=0, row=2, **PADS)
entryL0 = tkinter.Entry(master=window, font=FONT10)
entryL0.grid(column=1, row=2, **PADS)
labelL1 = tkinter.Label(master=window, text="name: ", font=FONT10)
labelL1.grid(column=0, row=3, **PADS)
entryL1 = tkinter.Entry(master=window, font=FONT10)
entryL1.grid(column=1, row=3, **PADS)
labelL2 = tkinter.Label(master=window, text="sex: ", font=FONT10)
labelL2.grid(column=0, row=4, **PADS)
entryL2 = tkinter.Entry(master=window, font=FONT10)
entryL2.grid(column=1, row=4, **PADS)
labelL3 = tkinter.Label(master=window, text="age: ", font=FONT10)
labelL3.grid(column=0, row=5, **PADS)
entryL3 = tkinter.Entry(master=window, font=FONT10)
entryL3.grid(column=1, row=5, **PADS)
labelL4 = tkinter.Label(master=window, text="sibSp: ", font=FONT10)
labelL4.grid(column=0, row=6, **PADS)
entryL4 = tkinter.Entry(master=window, font=FONT10)
entryL4.grid(column=1, row=6, **PADS)
labelL5 = tkinter.Label(master=window, text="parch: ", font=FONT10)
labelL5.grid(column=0, row=7, **PADS)
entryL5 = tkinter.Entry(master=window, font=FONT10)
entryL5.grid(column=1, row=7, **PADS)
labelL6 = tkinter.Label(master=window, text="fare: ", font=FONT10)
labelL6.grid(column=0, row=8, **PADS)
entryL6 = tkinter.Entry(master=window, font=FONT10)
entryL6.grid(column=1, row=8, **PADS)
labelL7 = tkinter.Label(master=window, text="embarked: ", font=FONT10)
labelL7.grid(column=0, row=9, **PADS)
entryL7 = tkinter.Entry(master=window, font=FONT10)
entryL7.grid(column=1, row=9, **PADS)


def inputHelp():
	messagebox.showinfo(
		"Input Help",
		"""
pClass   :: The passenger's class (1-3)
name     :: The passenger's name
sex      :: The passenger's sex (male / female) (apologies to other sexes)
age      :: The passenger's age (0+)
sibSp    :: The number of siblings of the passenger, onboard (0+)
parch    :: The number of parents, grandparents, etc... of the passenger, onboard (0+)
fare     :: How much the passenger payed for the trip (0+)
embarked :: Where the passenger embarked (S/C/Q)
""")


def predict():
	entries = [entryL0.get(), entryL1.get(), entryL2.get(), entryL3.get(), entryL4.get(), entryL5.get(), entryL6.get(),
		entryL7.get()]
	if all(map(len, entries)):
		pClass, name, sex, age, sibSp, parch, fare, embarked = entries
		# We know they're all there, now check they're all acceptable
		if all(map(lambda x: x.isnumeric(), [pClass, age, sibSp, parch, fare]))\
				and all(map(lambda x: bool(re.match(r"[\w.]+", x)), [name, sex, embarked])):
			# Clean data
			try:
				sex = {"male": 0, "female": 1}[sex]
				embarked = {"S": 0, "C": 1, "Q": 2}[embarked]
			except KeyError:
				messagebox.showerror("Invalid Input", "Either `sex` or `embarked` aren't legal inputs\nPlease consult the input help")
			else:
				data = [[pClass, sex, age, sibSp, parch, fare, embarked]]
				prediction = model.predict(data)
				messagebox.showinfo("Prediction", f"Your passenger {'will' if prediction else 'wont'} survive ({prediction[0]}%)")
		else:
			messagebox.showerror("Invalid Input", "One, or more, inputs are of the wrong type\nPlease consult the input help")
	else:
		messagebox.showerror("Invalid Input", "One, or more, inputs are missing")


inpHelp = tkinter.Button(master=window, text="Input Help", command=inputHelp, font=FONT10)
inpHelp.grid(column=0, row=10, **PADS)
submit = tkinter.Button(master=window, text="Submit", command=predict, font=FONT10)
submit.grid(column=1, row=10, **PADS)

# Right (from file)


tkinter.mainloop()
