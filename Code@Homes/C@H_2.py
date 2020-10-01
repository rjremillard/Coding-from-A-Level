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
----------------------------
Pygame GUI for the animation
----------------------------
"""

# Start pygame
pygame.init()
font = pygame.font.SysFont("comfortaa", 10)

# Setup window
screen = pygame.display.set_mode([1000, 750])

# Variables for loop
ac, pc, mar, mdr, cir = 0, 0, -1, 0, 0

# Main game loop
while not stop:
	# Resetting
	opcode, operand = "", ""

	# If exit pressed
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			stop = True

	# Fetch
	mar = pc
	mdr = RAM[mar]
	pc += 1
	cir = mdr

	# Decode
	opcode, operand = cir[0], cir[1]

	# Pygame window (L for label)
	Lac = font.render("Ac: %s" % bin(ac), 1, BLACK)
	screen.blit(Lac, (100, 100))

	# Execute
	if opcode == 0:  # HLT
		stop = True

	elif opcode == 1:  # ADD
		ac += RAM[operand]

	elif opcode == 2:  # SUB
		ac -= RAM[operand]

	elif opcode == 3:  # STA
		RAM[operand] = ac

	elif opcode == 4:  # LDA
		ac = RAM[operand]

	elif opcode == 5:  # INP
		ac = int(input("Input: "))  # Should be in binary

	elif opcode == 6:  # OUT
		print("Output: %d" % ac)

print("Stopped")
