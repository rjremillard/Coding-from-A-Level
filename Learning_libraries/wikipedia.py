import wikipedia
import tkinter

# Constants
FONT11 = ("Comfortaa", 11)
FONT10 = ("Comfortaa", 10)

# Variables
search = ""

# Make window
win = tkinter.Tk()
win.title = "Wikipedia"

titleLabel = tkinter.Label(master=win, text="Time to search Wikipedia", font=FONT11)
titleLabel.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

searchLabel = tkinter.Label(master=win, text="Search for:", font=FONT10)
searchLabel.grid(column=0, row=1, padx=10, pady=10)

searchInp = tkinter.Entry(master=win)
searchInp.grid(column=1, row=1)


def enter() -> None:
	if searchInp.get():
		global search
		search = searchInp.get()

		win.destroy()


enterButt = tkinter.Button(master=win, text="Enter", font=FONT10, command=enter)
enterButt.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

win.mainloop()

# Search for what? win
win = tkinter.Tk()
win.title = "Wikipedia"

possible = wikipedia.search(search, suggestion=True)

for item in possible:
	item2 = item.strip(" ")
	locals()["%sLabel" % item2] = tkinter.Label(master=win, text=item)


	def get() -> None:
		pass


	locals()["%sButton" % item2] = tkinter.Button(master=win, text="Choose me", command=get)

	# TODO: Finish
