import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

import math

def main(*args):

    """Runs the main GUI"""

    r = tk.Tk()

    r.title('JH Setup Calc')

    r.geometry('600x400')

   

 

    options = ["as_is", "milli", "micro", "nano", "pico"]

    n = ttk.Combobox(r, values=options, font=("Courier", 18))

    n.set("micro")

    n.grid(row=2, column=1)

    n2 = ttk.Combobox(r, values=options, font=("Courier", 18))

    n2.set("pico")

    n2.grid(row=8, column=1)
    
    l1 = tk.Label(r, text="Inductance Value", font=("Courier", 18))
    l1.grid(row=0, column=0)
    l = tk.Entry(r, bg="orange", font=("Courier", 18))

    l.grid(row=2, column=0)
    c1 = tk.Label(r, text="Capcitance Value", font=("Courier", 18))
    c1.grid(row=6, column=0)
    c = tk.Entry(r, bg="cyan", font=("Courier", 18))

    c.grid(row=8, column=0)

    calc_button = tk.Button(r, text='Next>>', font=("Courier", 18), command = lambda: combo_calc(l.get(), c.get(), n.get(), n2.get()))

    calc_button.grid(row=9, column=1)

  
def combo_calc(l, c, n, n2, *args):

    #Testing the passing arguements with print statement

    print(l)

    print(c)

    print(n)

    print(n2)

    #create new GUI window with title and set initial size

    p = tk.Tk()

    p.title('JH Resonance Calc')

    p.geometry('400x150')
    # conditions below to adjust entry by converting string to interger and divide by
    # by the value assoicated by the text from the combobox.
    # Could not convert the string to float, this failed.
    # It appears to must conver string to interger then to float.
    try:
        if n == "as_is":
                a = l 
        elif n == "milli":
                a = str(int(l)  / 1000) 
        elif n == "micro":
                a = str(int(l)  / 1000000)   
        elif n == "nano":
                a = str(int(l) / 1000000000) 
        elif n == "pico":
                a = str(int(l) / 1000000000000) 

        if n2 == "as_is":
                a2 = str(int(c) * 1)   
        elif n2 == "milli":
                a2 = str(int(c) / 1000)  
        elif n2 == "micro":
                a2 = str(int(c) / 1000000) 
        elif n2 == "nano":
                a2 = str(int(c) / 1000000000) 
        elif n2 == "pico":
                a2 = str(int(c) / 1000000000000)  
        else:
            return float(a), float(a2)
    except Exception:
        
        n == 1
        n2 == 1		
    print(a)
    print(a2)
    na = a
    na2 = a2
    ttrl = tk.Label(p, text="Engineering Notation Set", font=("Courier", 18))
    ttrl.grid(row=4, column=0)
    freq = tk.Button(p, text='Calculate Resonant Frequency', bg="light blue", command = lambda: freq_calc(float(a), float(a2)), font=("Courier", 12))
    freq.grid(row=8,column=0)
    na = tk.Label(p, text=na, font=("Courier", 18))
    na.grid(row=6, column=0)
    print(a, a2)
    na2 = tk.Label(p, text=na2, font=("Courier", 18))
    na2.grid(row=7,column=0)
    return na, na2, a, a2

def freq_calc(ll, cc):

    r = Tk()
    r.geometry('400x150')
    r.title('---Frequency  Final Answer---')
    llcc = float(ll) * float(cc)
    pi2 = math.pi * 2
    invfreq = math.sqrt(llcc) * pi2
    print(pi2)
    freq = 1 / float(invfreq)
    print(freq)
    kHz = freq / 1000
    Mhz = kHz / 1000
    a8 = kHz
    a10 = Mhz
    a4 = freq
    a4 = Label(r, text=freq, font=("Courier", 18))
    a4.grid(row=6, column=4)
    a6 = Label(r, text="Hz", font=("Courier", 18))
    a6.grid(row=6, column=5)
    a8 = Label(r, text=kHz, font=("Courier", 18))
    a8.grid(row=7, column=4)
    a9 = Label(r, text="kHz", font=("Courier", 18))
    a9.grid(row=7, column=5)
    a10 = Label(r, text=Mhz, font=("Courier", 18))
    a10.grid(row=9, column=4)
    a11 = Label(r, text="MHz", font=("Courier", 18))
    a11.grid(row=9, column=5)
    return a4, freq  

    r.mainloop()

main()

