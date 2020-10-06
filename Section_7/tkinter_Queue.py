"""
A visual representation of a queue
"""

import tkinter
import Queues
from tkinter import messagebox


# Constants
FONT11, FONT10, FONT9 = ("comfortaa", 11), ("comfortaa", 10), ("comfortaa", 9)

# Other variables
size = 0


# Setup
window = tkinter.Tk()

title = tkinter.Label(master=window, text="Size:", font=FONT11)
title.grid(column=0, row=0, padx=10, pady=10)

addEntry = tkinter.Entry(master=window, font=FONT10)
addEntry.grid(column=0, row=1, padx=10, pady=10)


def continue_():
	s = addEntry.get()
	if s != "" and s.isnumeric():
		global size
		size = s
		window.destroy()

	else:
		messagebox.showerror(title="Bad input", message="Please enter only a number")


submitButton = tkinter.Button(master=window, text="Submit", command=continue_, font=FONT9)
submitButton.grid(column=0, row=2, padx=10, pady=10)

window.mainloop()

# Queue setup
queue = Queues.Linear(size=int(size))

# Main window
window = tkinter.Tk()

title = tkinter.Label(master=window, text=":: Queue Abstraction ::", font=FONT11)
title.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

addLabel = tkinter.Label(master=window, text="To add:", font=FONT10)
addLabel.grid(column=0, row=1, padx=10, pady=10)

addEntry = tkinter.Entry(master=window, font=FONT10)
addEntry.grid(column=0, row=2, padx=10, pady=10)


def add():
	item = addEntry.get()
	if item != "":
		try:
			queue.enQueue(item)
		except IndexError as e:
			messagebox.showerror(title="", message=e)
		finally:
			queueOutput.config(text="\n".join(i if i else "" for i in queue.queue))
			queueOutput.update_idletasks()


addButton = tkinter.Button(master=window, text="Add", command=add, font=FONT10)
addButton.grid(column=0, row=3, padx=10, pady=10)

removeLabel = tkinter.Label(master=window, text="To remove:", font=FONT10)
removeLabel.grid(column=0, row=4, padx=10, pady=10)


def remove():
	try:
		queue.deQueue()
	except IndexError as e:
		messagebox.showerror(title="", message=e)
	finally:
		queueOutput.config(text="\n".join(i if i else "" for i in queue.queue))
		queueOutput.update_idletasks()


removeButton = tkinter.Button(master=window, text="Remove", command=remove, font=FONT10)
removeButton.grid(column=0, row=6, padx=10, pady=10)

queueOutput = tkinter.Label(master=window, text="", font=FONT10, width=40)
queueOutput.grid(column=1, row=1, rowspan=4, padx=10, pady=10)

window.mainloop()
