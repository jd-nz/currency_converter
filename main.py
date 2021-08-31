import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
from functools import partial
from combobox_data import *
from convert import *

data = combobox_data()

master = tk.Tk()

master.title("tk")
master.geometry("")

#row0
tk.Label(master, text="Currency Converter").grid(row=0)

#row1
tk.Label(master, text="Select Currency").grid(row=1)

#row2
currency_1 = tk.StringVar()
entryCurrency = Combobox(master, values=data, textvariable=currency_1).grid(row=2)

#row3
tk.Label(master, text="Currency Amount").grid(row=3)

#row4
value = tk.StringVar()
entryValue = tk.Entry(master, textvariable=value).grid(row=4)

#row5
tk.Label(master, text="Select Currency").grid(row=5)

#row6
currency_2 = tk.StringVar()
entryCurrency = Combobox(master, values=data, textvariable=currency_2).grid(row=6)

#row7
convert = partial(convert, value, currency_1, currency_2)
button = tk.Button(master, text="Convert", command=convert).grid(row=7)

master.mainloop()