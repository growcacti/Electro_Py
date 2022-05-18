

import tkinter as tk
from tkinter import ttk
from tkinter import *
import math


root = tk.Tk()


root.title("ElectroPy Frequency to Meters, Feet Converter JH Apps" )
root.geometry('600x500')

def clearlist():
    lboxx1.delete(0, END)
    lboxx2.delete(0, END)

def eunc(l, n, *args):
    try:
        print(int(l))
        
    
       
        if n == "THz":
        
            a = str(int(l) * 1000000000000)
            print(a)

        elif n == "GHz":

            a = str(int(l) * 1000000000)
            print(a)

        elif n == "MHz":

            a = str(int(l) * 1000000)
            print(a)
        elif n == "kHz":

            a = str(int(l) * 1000)
            print(a)
        

        elif n == "Hz":
            a = l
            print(a)

        elif n == "mHz":
            a = str(int(l)  / 1000)
            print(a)

          
     
        
    except ValueError as ex:
        print(ex)


    tometers(a)
    

        

def tometers(a):
    meterf = 299792458 / float(a)
    cm = meterf * 100
    mm = meterf * 1000
    inches = cm / 2.54
    ft = float(meterf) * 3.28084
    yd = ft / 3
    print(meterf)
    lboxx1.insert(1, a)
    lboxx1.insert(2, meterf)
    lboxx1.insert(3, ft)
    lboxx1.insert(4, yd)
    lboxx1.insert(5, inches)
    lboxx1.insert(6, cm)
    lboxx1.insert(7, mm)
    lboxx2.insert(1, "Hz")
    lboxx2.insert(2, "m  Meters")
    lboxx2.insert(3, "ft  Feet")
    lboxx2.insert(4, "yards")
    lboxx2.insert(5, "inches")
    lboxx2.insert(6, "cm")
    lboxx2.insert(7, "mm")
    

l1 = tk.Label(root, text="Frequency", font=("Arial", 12))
l1.grid(row=0, column=2)
l3 = tk.Label(root, text="in", font=("Arial", 12))
l3.grid(row=0, column=3)
l = tk.Entry(root, bd=5, bg="cyan", font=("Arial", 8))
l.grid(row=1, column=2)
options = [ "THz", "GHz", "MHz", "kHz", "Hz", "mH"]
n = ttk.Combobox(root, values=options, font=("Arial", 8))
n.grid(row=1, column=3)
n.set("MHz")    

lboxx1 = tk.Listbox(root, bd=5, bg="seashell")
lboxx1.grid(row=10, column=2)
lboxx2 = tk.Listbox(root, bd=5, bg="ivory")
lboxx2.grid(row=10, column=3)

calc_button = tk.Button(root, text='Calculate>>', bg="orange", bd=7,  font=("Arial Black", 12), command=lambda: eunc(l.get(), n.get()))
calc_button.grid(row=7, column=3)
b2 = tk.Button(root, text="Clear", bg="light blue", bd=7, command=clearlist)
b2.grid(row=6, column=0)



root.mainloop()
