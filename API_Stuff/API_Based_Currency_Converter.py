from tkinter import messagebox

import requests
import tkinter

"""
A currency converter, with a GUI, using the Alpha Vantage API
"""

# Constants
API_KEY = "PBH1WMPQAAII4484"


# Functions

# Gets the rates
def get(key: str):
	from_, to = fromEntry.get(), toEntry.get()

	# If either from or to are empty
	if not from_ or not to:
		messagebox.showerror("Error", "Please enter values in the 'From' and 'To' fields")

		# Stops the rest from executing
		return None

	else:
		req = requests.get(
			"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=%s&to_currency=%s&apikey=%s"
			% (from_, to, key)
		)

		resp = req.json()

		# Error checking
		if req.status_code == 200:
			try:
				# Showing info
				return resp["Realtime Currency Exchange Rate"]

			# If there is an error message
			except KeyError:
				messagebox.showerror("Error", resp["Error Message"])
		else:
			messagebox.showerror("Error", "%d Error in request" % req.status_code)
			return None


# For the info button
def info():
	resp = get(API_KEY)
	messagebox.showinfo("Info", "\n".join("%s: %s" % (i[3:], resp[i]) for i in resp))


# For the convert button
def convert():
	resp, amount = get(API_KEY), amountEntry.get()

	# If amount field is empty
	if not amountEntry:
		messagebox.showerror("Error", "Please enter a value in the 'amount' field")

	else:
		messagebox.showinfo("Conversion", "%s %s = %s %.2f\nSee Info for more information" % (
			resp["1. From_Currency Code"], amount, resp["3. To_Currency Code"],
			float(amount) * float(resp["5. Exchange Rate"])
		))


# For the help button
def help_():
	messagebox.showinfo("Help", """Common Currency Codes:
	USD - U.S. dollar
	EUR - euro
	GBP - Great Britain pound (sterling)
	JPY - Japanese yen
	CHF - Swiss Franc
	AUD - Australian dollar  
	CAD - Canadian dollar
	CNY - China Yuan Renminbi
	NZD - New Zealand dollar
	INR - Indian rupee
	BZR - Brazilian Real
	SEK - Swedish Krona
	ZAR - South African Rand
	HKD - Hong Kong Dollar
	""")


# GUI
window = tkinter.Tk()

title = tkinter.Label(master=window, text="API-based Currency Converter")
title.grid(column=0, columnspan=3, row=0, pady=10)

fromLabel = tkinter.Label(master=window, text="From:")
fromLabel.grid(column=0, row=1, padx=10, pady=10)

fromEntry = tkinter.Entry(master=window)
fromEntry.grid(column=0, row=2, padx=10, pady=10)

midLabel = tkinter.Label(master=window, text="→")
midLabel.grid(column=1, row=2)

toLabel = tkinter.Label(master=window, text="To:")
toLabel.grid(column=2, row=1, padx=10, pady=10)

toEntry = tkinter.Entry(master=window)
toEntry.grid(column=2, row=2, padx=10, pady=10)

amountLabel = tkinter.Label(master=window, text="Amount:")
amountLabel.grid(column=0, row=3, padx=10, pady=10)

amountEntry = tkinter.Entry(master=window)
amountEntry.grid(column=2, row=3, padx=10, pady=10)

infoButton = tkinter.Button(master=window, text="Conversion info", command=info, width=15)
infoButton.grid(column=0, row=5, pady=10, columnspan=2)

convertButton = tkinter.Button(master=window, text="Convert", command=convert, width=30, height=2)
convertButton.grid(column=0, row=4, pady=10, columnspan=3)

helpButton = tkinter.Button(master=window, text="Help", command=help_, width=15)
helpButton.grid(column=2, row=5, pady=10)

tkinter.mainloop()
