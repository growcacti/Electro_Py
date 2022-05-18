import tkinter as tk
from tkinter import ttk
from tkinter import *
import math





f1 = tk.Tk()

def clearlist1():
    lboxx1.delete(0, END)
    lboxx2.delete(0, END)


def calculation():

    try:
        num1 = float(x.get())
        num2 = float(y.get())
        cb1 = n.get()
        cb2 = n2.get()
        if cb1 == "Volts" and cb2 == "Amps":
            num3 = float(num1) / float(num2)
            num4 = float(num1) * float(num2)
            str1 =  "Ohms"
            str2 = "Watts"
        elif cb1 == "Volts" and cb2 == "Ohms":
             num3 = float(num1) / float(num2)
             num4 = float(num1) * float(num1) / float(num2)
             str1 = "Amps"
             str2 = "Watts"
        elif cb1 == "Volts" and cb2 == "Watts":
             num3 = float(num1) * float(num1) / float(num2)
             str1 = "Ohms"
             num4 = float(num2) / float(num1)
             str2 = "Amps"
        elif cb1 == "Amps" and cb2 == "Ohms":
             num3 = float(num1) * float(num2)
             str1 = "Volts"
             num4 = float(num1) * float(num1) / float(num2)
             str2 = "Watts"
        elif cb1 == "Watts" and cb2 == "Amps":
             num3 = float(num1) / float(num2) ** 2
             str1 = "Ohms"
             num4 = float(num1) / float(num2)
             str = "Volts"
        elif cb1 == "Watts" and cb2 == "Volts":
             num3 = float(num1) * float(num1) / float(num2)
             str1 = "Ohms"
             num4 = float(num2) / float(num1)
        elif cb1 == "Watts" and cb2 == "Ohms":
             num3 = math.sqrt(float(num1) / float(num2))
             str1 = "Amps"
             num4 =  math.sqrt(float(num1) * float(num2))
             str2 ="Volts"
        elif cb1 == "Amps" and cb2 == "Watts":
             num3 = float(num2) / float(num1) ** 2
             str1 = "Ohms"
             num4 = float(num2) / float(num1)
             str = "Volts"
        elif cb1 == "Amps" and cb2 == "Amps":
             num3 = 1
             str1 = "Amps"
             num4 = 1
             str2 = "Amps"
 
        elif cb1 == "Volts" and cb2 == "Volts":
             num3 = 1
             str1 = "Volts"
             num4 = 1
             str2 = "Volts"

        elif cb1 == "Amps" and cb2 == "Volts":
             num3 = float(num1) / float(num2)
             num4 = float(num1) * float(num2)
             str1 =  "Ohms"
             str2 = "Watts"
        else:
             num3 = num4

        print(num3)
        print(num4)
        print(str1)
        print(str2)
        lboxx1.insert(1, num3)
        lboxx1.insert(2, num4)
        lboxx2.insert(1, str1)
        lboxx2.insert(2, str2)
    except Exception as ex:
         print(ex)
         result = 'error'
         return

x = tk.StringVar()
y = tk.StringVar()
options1 = ["Volts ", "Watts", "Amps"]
options2 = ["Amps", "Ohms", "Volts"]
n = ttk.Combobox(f1, values=options1, font=("Arial", 8))
n.set("Volts")
n.grid(row=1, column=2)
n2 = ttk.Combobox(f1, values=options2, font=("Arial", 8))
n2.set("Ohms")
n2.grid(row=2, column=2)
x = tk.Entry(f1, bg="yellow", font=("Arial", 8))
x.grid(row=1, column=1)
y = tk.Entry(f1, bg="yellow", font=("Arial", 8))
y.grid(row=2, column=1)
btn1 = tk.Button(f1, text="calculate", bg = 'cyan', font=("Arial", 8), command=calculation)
btn1.grid(row=3, column=1)
btn1 = tk.Button(f1, text="Clear Answers", bg = 'light green', font=("Arial", 8), command=clearlist1)
btn1.grid(row=3, column=0)

lboxx1 =Listbox(f1)
lboxx1.grid(row=4, column=1)
lboxx2 =Listbox(f1)
lboxx2.grid(row=4, column=2)


