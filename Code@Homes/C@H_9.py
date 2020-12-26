"""
Uses a GUI to play a coin flip game
50/50 chance of either a head or tails
Can: play, make account, see own past results, and see overall stats
Saves sha256 hash of passwords for security, and records are deleted from RAM after use
"""

# Imports
import tkinter
import random
import json

from tkinter import messagebox
from hashlib import sha256
from math import gcd

# Constants
FONT10 = ("Comfortaa", 10)
FONT11 = ("Comfortaa", 11)
FONT12 = ("Comfortaa", 12)

PADS = {"padx": 10, "pady": 10}


def getHash(string: str) -> str:
	"""Uses sha256 to generate a hash of the string passed"""
	hashObj = sha256(string.encode("UTF-8"))
	return hashObj.hexdigest()


# Sign-in window
signInWin = tkinter.Tk()
signInWin.name = "Sign in"
signedIn, uname = False, ""

# Labels, Entries, and Buttons
title = tkinter.Label(master=signInWin, text=".: Sign In or Make a New Account :.", font=FONT12)
title.grid(column=0, row=0, columnspan=4, **PADS)

# For existing users
label1 = tkinter.Label(master=signInWin, text="Existing User", font=FONT11)
label1.grid(column=0, row=1, columnspan=2, **PADS)

unameExistingL = tkinter.Label(master=signInWin, text="Username:", font=FONT10)
unameExistingL.grid(column=0, row=2, **PADS)

unameExistingE = tkinter.Entry(master=signInWin, font=FONT10)
unameExistingE.grid(column=1, row=2, **PADS)

passwdExistingL = tkinter.Label(master=signInWin, text="Password:", font=FONT10)
passwdExistingL.grid(column=0, row=3, **PADS)

passwdExistingE = tkinter.Entry(master=signInWin, font=FONT10)
passwdExistingE.grid(column=1, row=3, **PADS)


# Checks credentials then moves on
def checker():
	global uname
	uname, passwd = unameExistingE.get(), passwdExistingE.get()

	# If any entry given
	if uname and passwd:
		with open("C@H_9.json", "r") as f:
			records = json.load(f)
		try:
			record = records[uname]
			if record["passwd"] == getHash(passwd):
				global signedIn
				signedIn = True
				signInWin.destroy()
			else:
				messagebox.showerror(message="Incorrect password")

		except KeyError:
			messagebox.showerror(message="That username does not exist")

		del records

	else:
		messagebox.showerror(message="Both username and password are required")


existingSubmit = tkinter.Button(master=signInWin, command=checker, text="Submit", font=FONT10)
existingSubmit.grid(column=0, row=5, columnspan=2, **PADS)

# For new users
label2 = tkinter.Label(master=signInWin, text="New User", font=FONT11)
label2.grid(column=2, row=1, columnspan=2, **PADS)

unameNewL = tkinter.Label(master=signInWin, text="Username:", font=FONT10)
unameNewL.grid(column=2, row=2, **PADS)

unameNewE = tkinter.Entry(master=signInWin, font=FONT10)
unameNewE.grid(column=3, row=2, **PADS)

passwdNewL = tkinter.Label(master=signInWin, text="Password:", font=FONT10)
passwdNewL.grid(column=2, row=3, **PADS)

passwdNewE = tkinter.Entry(master=signInWin, font=FONT10)
passwdNewE.grid(column=3, row=3, **PADS)

passwdNewConfL = tkinter.Label(master=signInWin, text="Confirm Password:", font=FONT10)
passwdNewConfL.grid(column=2, row=4, **PADS)

passwdNewConfE = tkinter.Entry(master=signInWin, font=FONT10)
passwdNewConfE.grid(column=3, row=4, **PADS)


# Creates new account
def maker():
	global uname
	uname, passwd, passwdConf = unameNewE.get(), passwdNewE.get(), passwdNewConfE.get()

	if uname and passwd and passwdConf:
		if passwd == passwdConf:
			with open("C@H_9.json", "r") as f:
				records = json.load(f)

			try:
				tmp = records[uname]
				messagebox.showerror(message="An account with this username already exists")
				del tmp
			except KeyError:
				records[uname] = {"passwd": getHash(passwd), "heads": 0, "tails": 0}

				with open("C@H_9.json", "w") as f:
					json.dump(records, f)

				del passwd, passwdConf, records

				global signedIn
				signedIn = True

				signInWin.destroy()
		else:
			messagebox.showerror(message="The two passwords do not match")

	else:
		messagebox.showerror(message="Both username and password are required")


newSubmit = tkinter.Button(master=signInWin, text="Submit", command=maker, font=FONT10)
newSubmit.grid(column=2, row=5, columnspan=2, **PADS)

# Run window
signInWin.mainloop()


# Have to be signed in to continue
if not signedIn:
	quit()

# Game window
gameWin = tkinter.Tk()
gameWin.title = "Coin Game"

# Labels, Entries, and Buttons
title = tkinter.Label(master=gameWin, text=".: Coin Flip Game :.", font=FONT12)
title.grid(column=0, row=0, columnspan=4, **PADS)

# Game part
label1 = tkinter.Label(master=gameWin, text="Game", font=FONT11)
label1.grid(column=0, row=1, columnspan=2, **PADS)

resultsL = tkinter.Label(master=gameWin, text="", font=FONT10)
resultsL.grid(column=0, row=2, columnspan=2, **PADS)

numsE = tkinter.Entry(master=gameWin, font=FONT10)
numsE.grid(column=0, row=3, **PADS)


# Flips, adds score, and updates results
def flipper():
	num = numsE.get()

	if num:
		try:
			# Number stuff
			num = int(num)
			rand = random.random()
			heads = int(num * rand)
			tails = num - heads

			# Updates
			resultsL.config(text=f"Flips: {num}, Heads: {heads}, Tails: {tails}\nRandom number used: {rand}")
			resultsL.update_idletasks()

			with open("C@H_9.json", "r") as f:
				records = json.load(f)

			records[uname]["heads"] += heads
			records[uname]["tails"] += tails

			with open("C@H_9.json", "w") as f:
				json.dump(records, f)

			del records

		except ValueError:
			messagebox.showerror(message="Please only enter a number")

	else:
		messagebox.showerror(message="Please enter a number of flips")


flipB = tkinter.Button(master=gameWin, command=flipper, text="Flip", font=FONT10)
flipB.grid(column=1, row=3, **PADS)


# Personal stats
label2 = tkinter.Label(master=gameWin, text="Stats", font=FONT11)
label2.grid(column=2, row=1, **PADS)

statsL = tkinter.Label(master=gameWin, text="", font=FONT10)
statsL.grid(column=2, row=2, **PADS)


# Updates stats from file
def updater():
	with open("C@H_9.json", "r") as f:
		records = json.load(f)

	record = records[uname]
	heads, tails = record["heads"], record["tails"]
	del records, record

	# Calculate simplified ratio
	den = gcd(heads, tails)
	ratio = f"{int(heads / den)}:{int(tails / den)}"

	statsL.config(text=f"""
	Username: {uname}
	Heads: {heads}, Tails: {tails}
	Most Common: {"Tails" if tails > heads else "Heads"}
	Ratio: {ratio}
""")


updateB = tkinter.Button(master=gameWin, text="Update", command=updater, font=FONT10)
updateB.grid(column=2, row=3, **PADS)

gameWin.mainloop()
