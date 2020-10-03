"""
An animation of the FDE cycle

Can translate following assembly: HLT, ADD, SUB, STA, LDA, INP, OUT

Opcode length:  4 bits
Operand length: 4 bits

Co-ords (for pygame):
	- AC    ::
	- ALU   ::
	- CU    ::
	- Registers:
		- PC    ::
		- MAR   ::
		- MDR   ::
		- CIR   ::
	- Memory:
		- 0b000 ::
		- ...

Binary was being annoying so I used decimal for the backend instead
"""

import pygame
import tkinter
from tkinter import messagebox


# Variables
FROM_ASSEMBLY = {"HLT": 0, "ADD": 1, "SUB": 2, "STA": 3, "LDA": 4, "INP": 5, "OUT": 6}
RAM = {0: (0, 0), 1: (0, 0), 2: (0, 0), 3: (0, 0), 4: (0, 0), 5: (0, 0), 6: (0, 0), 7: (0, 0), 8: (0, 0), 9: (0, 0),
							10: (0, 0), 11: (0, 0), 12: (0, 0), 13: (0, 0), 14: (0, 0), 15: (0, 0)}
FONT = ("Comfortaa", 10)
stop = False
BLACK = (0, 0, 0)

"""
------------------------------------
Tkinter window for imputing assembly
------------------------------------
"""


def help_():
	messagebox.showinfo("Help", "\
	Assembly Commands:\nHLT, ADD <>, SUB <>, STA <>, LDA <>, INP, OUT, where <> is the memory address in binary")


def submit():
	text = input_.get("1.0", "end").split("\n")

	# Max amount of memory
	if len(text) > 16:
		messagebox.showerror("Not enough memory", "Too many instructions have been entered, please enter less than 16")

	global RAM
	global stop
	address = 0
	for i in text:
		if len(i) < 3:
			if i != "":  # Little tkinter bypass
				messagebox.showerror("Incorrect instruction", "Instruction %s is not recognised" % i)
				stop = True  # So it doesn't run
				break

		elif i[:3] not in FROM_ASSEMBLY:
			messagebox.showerror("Incorrect instruction", "Instruction %s is not recognised" % i)
			stop = True  # So it doesn't run
			break

		else:
			RAM[address] = (FROM_ASSEMBLY[i[:3]], (int(i[4:], base=2) if i[3:] != "" else 0))
			address += 1

	if i == text[-1]:
		window.destroy()


# Setup window
window = tkinter.Tk()
window.title = "Assembly Input"

title = tkinter.Label(master=window, text="Assembly Input for FDE Program", font=FONT)
title.grid(column=0, row=0, columnspan=2)

inputLabel = tkinter.Label(master=window, text="Assembly Input:", font=FONT)
inputLabel.grid(column=0, row=1)

input_ = tkinter.Text(master=window, font=FONT)
input_.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

help__ = tkinter.Button(master=window, text="Help", command=help_, font=FONT)
help__.grid(column=0, row=3, pady=10)

submit_ = tkinter.Button(master=window, text="Submit", command=submit, font=FONT)
submit_.grid(column=1, row=3, pady=10)

tkinter.mainloop()


"""
------------------------------
Tkinter window for the runtime
------------------------------
"""

# Setup window
window = tkinter.Tk()

title = tkinter.Label(master=window, text="Step-by-step register output")
title.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

pcLabel = tkinter.Label(master=window, text="")
pcLabel.grid(column=0, row=1, padx=10, pady=10)

acLabel = tkinter.Label(master=window, text="")
acLabel.grid(column=1, row=1, padx=10, pady=10)

cirLabel = tkinter.Label(master=window, text="")
cirLabel.grid(column=2, row=1, padx=10, pady=10)

marLabel = tkinter.Label(master=window, text="")
marLabel.grid(column=3, row=1, padx=10, pady=10)

mdrLabel = tkinter.Label(master=window, text="")
mdrLabel.grid(column=0, row=2, padx=10, pady=10)

opcodeLabel = tkinter.Label(master=window, text="")
opcodeLabel.grid(column=1, row=2, padx=10, pady=10)

operandLabel = tkinter.Label(master=window, text="")
operandLabel.grid(column=2, row=2, padx=10, pady=10)

outLabel = tkinter.Label(master=window, text="")
outLabel.grid(column=3, row=2, padx=10, pady=10)

inLabel = tkinter.Label(master=window, text="Input:")
inLabel.grid(column=0, row=3, padx=10, pady=10)

inp = tkinter.Entry(master=window)
inp.grid(column=1, row=3, columnspan=2, padx=10, pady=10)

stepButt = tkinter.Button(master=window, text="Step")
stepButt.grid(column=3, row=3, padx=10, pady=10)

ramLabel = tkinter.Label(master=window, text="")
ramLabel.grid(column=0, row=4, columnspan=4, padx=10, pady=10)


# Main game loop
class Runtime:
	def __init__(self):
		# Variables for loop
		self.ac, self.pc, self.mar, self.mdr, self.cir = 0, 0, -1, 0, 0

	def update(self, stop_: bool):
		# Resetting
		opcode, operand = "", ""

		# Fetch
		self.mar = self.pc
		self.mdr = RAM[self.mar]
		self.pc += 1
		self.cir = self.mdr

		# Decode
		opcode, operand = self.cir[0], self.cir[1]

		# Execute
		if opcode == 0:  # HLT
			return True

		elif opcode == 1:  # ADD
			self.ac += RAM[operand]

		elif opcode == 2:  # SUB
			self.ac -= RAM[operand]

		elif opcode == 3:  # STA
			RAM[operand] = self.ac

		elif opcode == 4:  # LDA
			self.ac = RAM[operand]

		elif opcode == 5:  # INP
			self.ac = int(inp.get())  # Should be in binary

		elif opcode == 6:  # OUT
			outLabel.config(text="Output: %s" % bin(self.ac))
			outLabel.update()

		# Updating window
		pcLabel.config(text="PC: %d" % self.pc)
		pcLabel.update()

		acLabel.config(text="AC: %s" % bin(self.ac))
		acLabel.update()

		cirLabel.config(text="CIR: %s" % bin(self.cir))
		cirLabel.update()

		marLabel.config(text="MAR: %s" % bin(self.mar))
		marLabel.update()

		mdrLabel.config(text="MDR: %s" % bin(self.mdr))
		mdrLabel.update()

		opcodeLabel.config(text="Opcode: %s" % bin(opcode))
		opcodeLabel.update()

		operandLabel.config(text="Operand: %s" % bin(operand))
		operandLabel.update()

		ramLabel.config(text="RAM: %s" % ("%s: %s" % (bin(i), bin(RAM[i])) for i in RAM))
		ramLabel.update()

	print("Stopped")


def main_():
	global stop
	while not stop:
		stop = runtime.update(stop)


runtime = Runtime()

window.after(100, main_)

tkinter.mainloop()
