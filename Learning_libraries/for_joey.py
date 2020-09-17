import pyttsx3
import tkinter

"""
For Joey to speak
"""

# settings
speed = 100

# functions


# for the speaking from the text box
def say(inp=None):
	# if something is passed
	if inp:
		text = inp
	else:
		text = textInput.get("1.0", tkinter.END)

	print("Saying:          %s" % text)

	# speaking
	engine = pyttsx3.init()
	engine.setProperty("rate", speed)

	engine.say(text)

	# run
	engine.runAndWait()
	engine.stop()


# change speed
def speedUp():
	global speed
	speed += 50

	print("Speed is now:    %d" % speed)


def speedDown():
	global speed
	speed -= 50
	if speed < 50:
		speed = 50

	print("Speed is now:    %d" % speed)


# outputs all commands
print("System log:")

# tkinter window
win = tkinter.Tk()

title = tkinter.Label(master=win, text=".: The Speech Machine :.")
title.grid(column=0, row=0, columnspan=3, pady=20)

subtitle = tkinter.Label(master=win, text="Custom Input")
subtitle.grid(column=0, row=1, columnspan=2)

textInput = tkinter.Text(master=win)
textInput.grid(column=0, row=2, columnspan=2, rowspan=10, padx=10)

speakButton = tkinter.Button(master=win, text="Speak!", command=say)
speakButton.grid(column=0, row=13, columnspan=2, pady=10)

# speed
speedUp_ = tkinter.Button(master=win, text="Speed Up", command=speedUp)
speedUp_.grid(column=2, row=2, padx=10)

speedDown_ = tkinter.Button(master=win, text="Speed Down", command=speedDown)
speedDown_.grid(column=2, row=3, padx=10)

# common phrases
yes = tkinter.Button(master=win, text="Yes", command=lambda: say(inp="Yes"))
yes.grid(column=2, row=4, padx=10)

no = tkinter.Button(master=win, text="No", command=lambda: say(inp="No"))
no.grid(column=2, row=5, padx=10)

tkinter.mainloop()
