

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import tkinter.font
import math

import os

from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
r = tk.Tk()
r.geometry('1200x800')
r.title("Math APPS")








"""Convert a Decimal Number to a Binary Number."""


def decimal_to_binary(num: int) -> str:

    """
    Convert an Integer Decimal Number to a Binary Number as str.
    >>> decimal_to_binary(0)
    '0b0'
    >>> decimal_to_binary(2)
    '0b10'
    >>> decimal_to_binary(7)
    '0b111'
    >>> decimal_to_binary(35)
    '0b100011'
    >>> # negatives work too
    >>> decimal_to_binary(-2)
    '-0b10'
    >>> # other floats will error
    >>> decimal_to_binary(16.16) # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: 'float' object cannot be interpreted as an integer
    >>> # strings will error as well
    >>> decimal_to_binary('0xfffff') # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: 'str' object cannot be interpreted as an integer
    """

    if isinstance(num, float):
        raise TypeError("'float' object cannot be interpreted as an integer")
    if isinstance(num, str):
        raise TypeError("'str' object cannot be interpreted as an integer")

    if num == 0:
        return "0b0"

    negative = False

    if num < 0:
        negative = True
        num = -num

    binary: list[int] = []
    while num > 0:
        binary.insert(0, num % 2)
        num >>= 1

    if negative:
        binarynum = "-0b" + "".join(str(e) for e in binary)
        return binarynum
    binarynum = "0b" + "".join(str(e) for e in binary)
    #ans= tk.Label(r, text=binarynum)
    #ans.grid(row=6, column=1)
    lboxx2.insert(END, binary)
   
    return binarynum

                    

def from_entry(num):

    try:
        num = int(en1.get())
        lboxx1.insert(END, num)
        print(num)
        decimal_to_binary(num)
    # except block 
    except ValueError as ex:
        print(ex)   
    




def clearlist():
    lboxx1.delete(0, END)
    lboxx2.delete(0, END)



##num333 = tk.StringVar()
##num444 = tk.StringVar()
##numout33 = tk.StringVar()
##numout44 = tk.StringVar()
##vvv1 = tk.StringVar()
##vdiv1 = tk.StringVar()
label1 = tk.Label(r, text=" Input Int Base10 Decimal:")
label1.grid(row=1, column=2)
#tk.Label(r, text="Input R2:").grid(row=1, column=0)
#tk.Label(r, text="Vin for Vdiv").grid(row=2, column=0)
en1 = tk.Entry(r, bd=10, bg="wheat")
en1.grid(row=1, column=1)
#en2 = tk.Entry(r, bg="sky blue").grid(row=2, column=1)
lboxx1 = tk.Listbox(r, bd=10, bg="cyan2")
lboxx1.grid(row=10, column=2)
lboxx2 = tk.Listbox(r, bd=10, bg="light green", width=40)
lboxx2.grid(row=10, column=3)

##tk.Entry(r, textvariable=vvv1, bg="yellow").grid(row=2, column=1)
##lboxx1 = tk.Listbox(r, height=20)
##lboxx1.grid(row=6,  column=2)
##lboxx2 = tk.Listbox(r, height=20)
##lboxx2.grid(row=6,  column=1)
b1 = tk.Button(r, text="Convert", command=lambda: from_entry(en1.get())) 
b1.grid(row=5, column=0)
b2 = tk.Button(r, text="Clear", command=clearlist)
b2.grid(row=6, column=0) 
##b3 = tk.Button(r, text="Clear", command=clearlist1)
##b3.grid(row=7, column=0)
##num1234 = tk.StringVar()
##num4567 = tk.StringVar()
##num7891 = tk.StringVar()
##num1112 = tk.StringVar()
##vvv2 = tk.StringVar()
##num9999 = tk.StringVar()
##num8888 = tk.StringVar()
##num7777 = tk.StringVar()
##num6666= tk.StringVar()
##
##vdiv2 = tk.StringVar()
##tk.Label(r, text=" Input R).grid(row=0, column=5)
##tk.Entry(r, textvariable=num4567, bg="yellow").grid(row=1, column=5)
##tk.Entry(r, textvariable=num7891, bg="yellow").grid(row=2, column=5)
##tk.Entry(r, textvariable=num1112, bg="yellow").grid(row=3, column=5)
##tk.Entry(r, textvariable=vvv2, bg="yellow").grid(row=4, column=5)
##lb8 = tk.Listbox(r, height=20)
##lb8.grid(row=6,  column=7)
##lb10 = tk.Listbox(r, height=20)
##lb10.grid(row=6,  column=6)
##b2 = tk.Button(r, text="Calculate 4 Resistor", command=gen2)
##b2.grid(row=6, column=5)
##b4 = tk.Button(r, text="Clear", command=clearlist2)
##b4.grid(row=7, column=5)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
r.mainloop()

