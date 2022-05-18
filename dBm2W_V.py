import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk

import math



f6 = tk.Tk()
f6.title("dBm to Watts, Vrms, Vpk, Vpk-pk")
def clearlb():
    lbox.delete(0, END)
def dBmtoW(*args):
    num11 = num1.get()
    num111 = float(num11)
    
    num2 = 10 ** (num111 / 20)
    num3 = float(num2) * 0.2236
    num4 = float(num3) * 1.414
    num5 = float(num4) * 2
    print(num111, num2, num3, num4, num5)
    lbox.insert(1, num11)
    lbox.insert(2, num2)
    lbox.insert(3, num3)
    lbox.insert(4, num4)
    lbox.insert(5, num5)
    

    lbox2.insert(1, "dBm")
    lbox2.insert(2, "Watts")
    lbox2.insert(3, "Volts RMS")
    lbox2.insert(4, "Volts Peak")
    lbox2.insert(5, "Volts PK-PK")
   
    return

num1 = tk.StringVar()
e3 = tk.Entry(f6, textvariable=num1, bg="yellow", font=("Arial", 8))
e3.grid(row=0, column=2)
e3.focus()
tk.Label(f6, text="dBm").grid(row=0, column=3)
btn2 = tk.Button(f6, text="Calculate", command=dBmtoW)
btn2.grid(column=1, row=1)
btn4 = tk.Button(f6, text="Clear", command=clearlb)
btn4.grid(column=1, row=2)
lbox = tk.Listbox(f6)
lbox.grid(column=2, row=3)


lbox2 = tk.Listbox(f6)
lbox2.grid(column=3, row=3)



