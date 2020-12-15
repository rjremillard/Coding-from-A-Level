"""
Form anagrams from phrase entered, uses the enchant library to check against the English (UK - sorry sir!) dictionary
Will give all possible anagrams then in a separate window and save to a file
Also, can take quite some time to run so be patient, STDOUT contains some runtime information
Also, keep phrases small as will throw a memory error if too large
"""

import tkinter
import enchant
import json

from tkinter import messagebox
from itertools import permutations

# Setup dictionary
dic = enchant.Dict("en_GB")

# Form window
win = tkinter.Tk()
win.name = "Anagram Maker"

title = tkinter.Label(master=win, text="Anagram Maker")
title.grid(column=0, row=0, padx=10, pady=10)

entryBox = tkinter.Entry(master=win)
entryBox.grid(column=0, row=1, padx=10, pady=10)


# Main function
def makeAnagram():
    anagrams = set()  # Avoids multiples
    phrase = entryBox.get().lower()
    if phrase:
        perms = list(permutations(phrase))
        lenPerms, lenPhrase = len(perms), len(phrase)
        for i in range(lenPerms):
            tmp = "".join(perms[i])
            print(
                f"\rTrying: {tmp}, {str(i).zfill(len(str(lenPerms)))} of {lenPerms} possible combinations tried [{round(i * 100 / lenPerms)}%]",
                end=""
            )
            if all(dic.check(word) for word in tmp.split()):
                anagrams.add(tmp)
            del tmp

        # Done!
        anagrams = list(anagrams)

        win2 = tkinter.Tk()
        win2.title = "Results"

        lstBox = tkinter.Listbox(master=win2)
        for i in range(len(anagrams)):
            lstBox.insert(i, anagrams[i])

        lstBox.pack()

        with open("anagrams.json", "w") as f:
            json.dump({
                "All anagrams": anagrams,
                "Length": len(anagrams)
            }, f)

        del anagrams, perms  # To clear memory quickly

    else:
        messagebox.showerror(message="Please enter a phrase first")


button = tkinter.Button(master=win, text="Submit", command=makeAnagram)
button.grid(column=0, row=2, padx=10, pady=10)

tkinter.mainloop()
