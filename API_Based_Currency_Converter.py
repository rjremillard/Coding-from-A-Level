import requests, tkinter
from tkinter import messagebox

"""
A currency converter, with a GUI, using the Alpha Vantage API
"""

# Constants
API_KEY = "PBH1WMPQAAII4484"


# Gets the rates
def get(from_: str, to: str, key: str):
	req = requests.get(
		"https:www.alphavantage.coquery?function=CURRENCY_EXCHANGE_RATE&from_currency=%s&to_currency=%s&apikey=%s"
		% (from_, to, key)
	)

	# Error checking
	if req.status_code == 200:
		return req.json()
	else:
		messagebox.showerror("Error", "%d Error in request" % req.status_code)
		return None


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


def pressed():
	resp = get(fromEntry.get(), toEntry.get(), API_KEY)

	try:
		# Get the info
		ref = resp["Realtime Currency Exchange Rate"]

		# Showing info
		messagebox.showinfo("%s → %s" % (fromEntry.get(), toEntry.get()), "\n".join("%s: %s" % (i, ref[i]) for i in ref))

	# If there is an error message
	except KeyError:
		messagebox.showerror("Error", resp["Error Message"])


submitButton = tkinter.Button(master=window, text="Submit", command=pressed)
submitButton.grid(column=0, row=3, pady=10)


def help_():
	messagebox.showinfo("Help", """
Common Currency Codes:
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


helpButton = tkinter.Button(master=window, text="Help", command=help_)
helpButton.grid(column=2, row=3, pady=10)

tkinter.mainloop()
