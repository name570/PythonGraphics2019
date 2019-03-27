#!/usr/bin/env python3
'''
Пример для первой лекции про TkInter

Закрытие окошка в постинтерактивном режиме
'''

from tkinter import *
import random

def randomcolor():
    colorsymbols = "ABCDEF0123456"
    color = "#"
    for c in range(6):
        color += random.choice(colorsymbols)
    return color

def add_button():
    def colorize():

        But["background"] = randomcolor()
        But["foreground"] = randomcolor()
        Lab["background"]  = randomcolor()
        Lab["foreground"] = randomcolor()

    c,r = root.size()

    root.rowconfigure(r + 1, weight = 0)

    But = Button(root, text = "Random color", command = colorize)
    But.grid(row = r + 1,column = 0,sticky = E+W+S+N)
    Lab = Label(root, text = "My Label")
    Lab.grid(row = r + 1, column = 1, sticky = E+W+S+N)


TKroot = Tk()
TKroot.title("Hello")

root = Frame(TKroot)
root.place(relx = 0, rely = 0, relheight = 1, relwidth = 1)

root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 1)
root.rowconfigure(0, weight = 0)
root.rowconfigure(1, weight = 0)


Butt = Button(root, text = "Add", command = add_button)
Butt.grid(row = 0, column =0, sticky = E+W+S+N)

Exit = Button(root, text = "Exit", command = root.quit)
Exit.grid(row = 0, column = 1, sticky = E+W+S+N)

# Txt = Label(root, text="This is a label", bg="PeachPuff")
# Txt.grid(row=1, column=0, columnspan=2, sticky=E+W+N)

TKroot.mainloop()
print("Done")

