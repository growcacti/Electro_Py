

import tkinter as tk
from tkinter import ttk
from tkinter import *
import math


root = tk.Tk()


root.title("ElectroPy Length to Frequency, Converter JH Apps" )
root.geometry('600x500')

def clearlist():
    lboxx1.delete(0, END)
    lboxx2.delete(0, END)

def eunc(l, n, *args):
    try:
        print(float(l))
        if l == 0:
            lboxx1.insert(2, "undefined")
            lboxx2.insert(2,  "Infinite")
        else:
       
            if n == "m":
                 freqm =  299792458 / float(l)
                 lboxx1.insert(2, freqm)
                 lboxx2.insert(2,  "Hz")
                 MHz = freqm / 1000000
                 kHz = MHz * 1000
                 lboxx1.insert(3, kHz)
                 lboxx2.insert(3,  "kHz")
                 lboxx1.insert(4, MHz)
                 lboxx2.insert(4,  "MHz")
                 GHz = MHz /1000
                 lboxx1.insert(5, GHz)
                 lboxx2.insert(5,  "GHz")
                 

                


            elif n == "cm":
                cm = 100 * 299792458
                freqcm = cm / float(l) 
                lboxx1.insert(2, freqcm)
                lboxx2.insert(2,  "Hz")
                MHz = freqcm / 1000000
                GHz = MHz /1000
                kHz = MHz * 1000
                lboxx1.insert(3, kHz)
                lboxx2.insert(3,  "kHz")
                lboxx1.insert(4, MHz)
                lboxx2.insert(4,  "MHz")
                lboxx1.insert(5, GHz)
                lboxx2.insert(5,  "GHz")
                
               

            elif n == "mm":
                 mm = 1000 * 299792458
                 freqmm = mm / float(l)
                 lboxx1.insert(2, freqmm)
                 lboxx2.insert(2,  "Hz")
                 MHz = freqmm / 1000000
                 lboxx1.insert(3, MHz)
                 lboxx2.insert(3,  "MHz")
                 GHz = MHz /1000
                 lboxx1.insert(4, GHz)
                 lboxx2.insert(4,  "GHz")

                
            elif n == "inches":
                cm = 100 * 299792458
                inches = cm / 2.54
                freqinches = inches / float(l)
                lboxx1.insert(2, freqinches)
                lboxx2.insert(2,  "Hz")
                MHz = freqinches / 1000000
                lboxx1.insert(3, MHz)
                lboxx2.insert(3,  "MHz")
                GHz = MHz /1000
                lboxx1.insert(4, GHz)
                lboxx2.insert(4,  "GHz")



            elif n == "ft":
                m = 299792458
                ft = m * 3.28084
                freqft = ft / float(l)
                lboxx1.insert(2, freqft)
                lboxx2.insert(2,  "Hz")
                MHz = freqft / 1000000
                kHz = MHz * 1000
                lboxx1.insert(3, kHz)
                lboxx2.insert(3,  "kHz")
                lboxx1.insert(4, MHz)
                lboxx2.insert(4,  "MHz")
                GHz = MHz /1000
                lboxx1.insert(5, GHz)
                lboxx2.insert(5,  "GHz")
                
                

            elif n == "yd":
                m = 299792458
                ft = m * 3.28084
                yd = ft / 3
                freqyd = yd / float(l)
                lboxx1.insert(2, freqyd)
                lboxx2.insert(2, "Hz")
                MHz = freqyd / 1000000
                kHz = MHz * 1000
                lboxx1.insert(3, kHz)
                lboxx2.insert(3,  "kHz")
          
                lboxx1.insert(4, MHz)
                lboxx2.insert(4,  "MHz")
                GHz = MHz /1000
                lboxx1.insert(5, GHz)
                lboxx2.insert(5,  "GHz")
                
              
     
        
    except ValueError as ex:
        print(ex)



l1 = tk.Label(root, text="Length", font=("Arial", 12))
l1.grid(row=0, column=2)
l3 = tk.Label(root, text="in", font=("Arial", 12))
l3.grid(row=0, column=3)
l = tk.Entry(root, bd=5, bg="cyan", font=("Arial", 8))
l.grid(row=1, column=2)
options = [ "m", "cm", "mm", "inches", "ft", "yd"]
n = ttk.Combobox(root, values=options, font=("Arial", 8))
n.grid(row=1, column=3)
n.set("m")    

lboxx1 = tk.Listbox(root, bd=5, bg="seashell")
lboxx1.grid(row=10, column=2)
lboxx2 = tk.Listbox(root, bd=5, bg="ivory")
lboxx2.grid(row=10, column=3)

calc_button = tk.Button(root, text='Calculate>>', bg="orange", bd=7,  font=("Arial Black", 12), command=lambda: eunc(l.get(), n.get()))
calc_button.grid(row=7, column=3)
b2 = tk.Button(root, text="Clear", bg="light blue", bd=7, command=clearlist)
b2.grid(row=6, column=0)

li1 = tk.Label(root, text="This is full wavelength", font=("Arial", 12))
li1.grid(row=20, column=2)

root.mainloop()
