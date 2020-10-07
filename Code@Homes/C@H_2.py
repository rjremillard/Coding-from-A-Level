"""
Can translate following assembly: HLT (0), ADD (1), SUB (2), STA(3), LDA (4), INP (5), OUT (6)
Data opcode will be 7

Opcode length:  4 bits
Operand length: 4 bits

Binary was being annoying so I used decimal for the backend instead
"""


import tkinter
from tkinter import messagebox


# Variables
FROM_ASSEMBLY = {"HLT": 0, "ADD": 1, "SUB": 2, "STA": 3, "LDA": 4, "INP": 5, "OUT": 6}
RAM = {0: (0, 0), 1: (0, 0), 2: (0, 0), 3: (0, 0), 4: (0, 0), 5: (0, 0), 6: (0, 0), 7: (0, 0), 8: (0, 0), 9: (0, 0),
							10: (0, 0), 11: (0, 0), 12: (0, 0), 13: (0, 0), 14: (0, 0), 15: (0, 0)}
FONT = ("comfortaa", 10)
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
title.grid(column=1, row=0, columnspan=2, padx=10, pady=10)

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

stepLabel = tkinter.Label(master=window, text="")
stepLabel.grid(column=3, row=2, padx=10, pady=10)


def main_():
	global stop
	stop = runtime.update()
	if stop:
		window.quit()


stepButt = tkinter.Button(master=window, text="Step", command=main_)
stepButt.grid(column=1, row=3, columnspan=2, padx=10, pady=10)

ramLabel = tkinter.Label(master=window, text="")
ramLabel.grid(column=0, row=4, columnspan=4, padx=10, pady=10)


# Main game loop
def niceBinary(binary: any) -> str:
	if type(binary) is tuple:
		newBin = bin(binary[1])[2:]
	else:
		newBin = bin(binary)[2:]
	return ("0" * (4 - len(newBin))) + newBin


class Runtime:
	def __init__(self):
		# Variables for loop
		self.ac, self.pc, self.mar, self.mdr, self.cir = 0, 0, -1, 0, 0
		self.step, self.opcode, self.operand = 0, "", ""

	def update(self):
		# Fetch
		if self.step == 0:
			self.mar = self.pc
			self.mdr = RAM[self.mar]
			self.pc += 1
			self.cir = self.mdr

		# Decode
		if self.step == 1:
			self.opcode, self.operand = self.cir[0], self.cir[1]

		# Execute
		if self.step == 2:
			if self.opcode == 0:  # HLT
				return True

			elif self.opcode == 1:  # ADD
				self.ac = self.ac + RAM[self.operand][1]

			elif self.opcode == 2:  # SUB
				self.ac = self.ac - RAM[self.operand][1]

			elif self.opcode == 3:  # STA
				RAM[self.operand] = (7, self.ac)
				self.ac = 0

			elif self.opcode == 4:  # LDA
				self.ac = RAM[self.operand][1]

			elif self.opcode == 5:  # INP

				def sub(s):
					inp = inpEntry.get()

					if inp != "" and inp.isnumeric():
						s.ac = int(inp)  # Should be in binary
						inpWin.destroy()

				# Make new input window
				inpWin = tkinter.Tk()

				inpLabel = tkinter.Label(master=inpWin, text="Input:")
				inpLabel.grid(column=0, row=0, padx=10, pady=10)

				inpEntry = tkinter.Entry(master=inpWin)
				inpEntry.grid(column=1, row=0, padx=10, pady=10)

				submitButt = tkinter.Button(master=inpWin, text="Submit", command=lambda: sub(self))
				submitButt.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

			elif self.opcode == 6:  # OUT
				messagebox.showinfo(title="Output", message="Output: %s" % niceBinary(self.ac))

		# Updating window
		pcLabel.config(text="PC: %s" % niceBinary(self.pc))
		pcLabel.update_idletasks()

		acLabel.config(text="AC: %s" % niceBinary(self.ac))
		acLabel.update_idletasks()

		cirLabel.config(text="CIR: %s %s" % (niceBinary(self.cir[0]), niceBinary(self.cir[1])))
		cirLabel.update_idletasks()

		marLabel.config(text="MAR: %s" % niceBinary(self.mar))
		marLabel.update_idletasks()

		mdrLabel.config(text="MDR: %s %s" % (niceBinary(self.mdr[0]), niceBinary(self.mdr[1])))
		mdrLabel.update_idletasks()

		opcodeLabel.config(text="Opcode: %s" % (niceBinary(self.opcode) if self.opcode != "" else ""))
		opcodeLabel.update_idletasks()

		operandLabel.config(text="Operand: %s" % (niceBinary(self.operand) if self.operand != "" else ""))
		operandLabel.update_idletasks()

		stepLabel.config(text="Step: %s" % ("Fetch" if self.step == 0 else "Decode" if self.step == 1 else "Execute"))
		stepLabel.update_idletasks()

		ramLabel.config(text="RAM:\n" + ", ".join(("%s: %s %s" % (niceBinary(i), niceBinary(RAM[i][0]),
													niceBinary(RAM[i][1])) for i in RAM)))
		ramLabel.update_idletasks()

		self.step = (self.step + 1) % 3


runtime = Runtime()
tkinter.mainloop()
