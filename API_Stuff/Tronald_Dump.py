from tkinter import messagebox

import tkinter
import requests

"""
A cool GUI for interfacing with the Tronald Dump API
See https://www.tronalddump.io/ for more info
"""


# Functions

# For the random button
def random():
	req = requests.get("https://api.tronalddump.io/random/quote")
	data = req.json()

	# If there is data
	if data:
		try:
			messagebox.showinfo("Random tweet", data["value"])

		# If key value doesn't exist
		except KeyError:
			messagebox.showerror("Error", data)

	else:
		messagebox.showerror("Error", data)


# For the lookup button
def lookup():
	tag = tagEntry.get()

	# Url encode
	tag = tag.replace(" ", "%20")

	resp = requests.get("https://api.tronalddump.io/tag/%s" % tag)

	# If all good
	if resp.status_code == 200:
		data = resp.json()
		messagebox.showinfo(data["value"])
		print(data)

		# TODO: Fix this

	# If tag not found
	elif resp.status_code == 404:
		messagebox.showerror("Tag not found", resp.json()["message"])

	else:
		messagebox.showerror("Error", resp.json()["message"])


# GUI
window = tkinter.Tk()

title = tkinter.Label(master=window, text="Tronald Dump")
title.grid(column=0, row=0, columnspan=2, pady=10)

tagLabel = tkinter.Label(master=window, text="Tag:")
tagLabel.grid(column=0, row=1)

tagEntry = tkinter.Entry(master=window)
tagEntry.grid(column=0, row=2, padx=10)

tagButton = tkinter.Button(master=window, text="Submit", command=lookup)
tagButton.grid(column=0, row=3)

randomButton = tkinter.Button(master=window, text="Random", command=random, height=3, width=20)
randomButton.grid(column=1, row=2, padx=10)

pad = tkinter.Label(master=window, text="")
pad.grid(column=0, row=4, columnspan=2)

tkinter.mainloop()
