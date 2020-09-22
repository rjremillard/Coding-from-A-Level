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
textInput.grid(column=0, row=2, columnspan=2, rowspan=13, padx=10)

speakButton = tkinter.Button(master=win, text="Speak!", command=say)
speakButton.grid(column=0, row=16, columnspan=2, pady=10)

# speed
speedUp_ = tkinter.Button(master=win, text="Speed Up", command=speedUp)
speedUp_.grid(column=2, row=2, padx=10, columnspan=2)

speedDown_ = tkinter.Button(master=win, text="Speed Down", command=speedDown)
speedDown_.grid(column=2, row=3, padx=10, columnspan=2)

# common phrases
yes = tkinter.Button(master=win, text="Yes", command=lambda: say(inp="Yes"))
yes.grid(column=2, row=4, padx=10)

no = tkinter.Button(master=win, text="No", command=lambda: say(inp="No"))
no.grid(column=3, row=4, padx=10)

sorry = tkinter.Button(master=win, text="Sorry", command=lambda: say(inp="Sorry"))
sorry.grid(column=2, row=5, padx=10)

ty = tkinter.Button(master=win, text="Thank you", command=lambda: say(inp="Thank you"))
ty.grid(column=3, row=5, padx=10)

welcome = tkinter.Button(master=win, text="You're welcome", command=lambda: say(inp="You're welcome"))
welcome.grid(column=2, row=6, padx=10, columnspan=2)

present = tkinter.Button(master=win, text="Present", command=lambda: say(inp="Present"))
present.grid(column=2, row=7, padx=10, columnspan=2)

sir = tkinter.Button(master=win, text="Sir", command=lambda: say(inp="Sir"))
sir.grid(column=2, row=8, padx=10)

miss = tkinter.Button(master=win, text="Miss", command=lambda: say(inp="Miss"))
miss.grid(column=3, row=8, padx=10)

what = tkinter.Button(master=win, text="What?", command=lambda: say(inp="What?"))
what.grid(column=2, row=9, padx=10, columnspan=2)

wait = tkinter.Button(master=win, text="Wait", command=lambda: say(inp="Wait"))
wait.grid(column=2, row=10, padx=10, columnspan=2)

dumb = tkinter.Button(master=win, text="Dumb", command=lambda: say(inp="Dumb"))
dumb.grid(column=2, row=11, padx=10, columnspan=2)

excellent = tkinter.Button(master=win, text="Excellent", command=lambda: say(inp="Excellent"))
excellent.grid(column=2, row=12, padx=10, columnspan=2)

laugh = tkinter.Button(master=win, text="Haha", command=lambda: say(inp="Haha"))
laugh.grid(column=2, row=13, padx=10, columnspan=2)

tkinter.mainloop()
