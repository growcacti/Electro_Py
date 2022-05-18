import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import tkinter.font
import math

import os

from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
 
root = tk.Tk()
root.geometry('800x300')
root.title("Electro PY JH APPS") 




def from_entry(num, base):
    
    try:
        num = int(en1.get())
        base = int(sp.get())
        lboxx1.insert(END, num)
        lboxx2.insert(END, base)
        print(num, base)
        decimal_to_any(num, base)
        
    # except block 
    except ValueError as ex:
        print(ex)
        



def decimal_to_any(num: int, base: int) -> str:
   
  
    """
    
    Convert a positive integer to another base as str.
    >>> decimal_to_any(0, 2)
    '0'
    >>> decimal_to_any(5, 4)
    '11'
    >>> decimal_to_any(20, 3)
    '202'
    >>> decimal_to_any(58, 16)
    '3A'
    >>> decimal_to_any(243, 17)
    'E5'
    >>> decimal_to_any(34923, 36)
    'QY3'
    >>> decimal_to_any(10, 11)
    'A'
    >>> decimal_to_any(16, 16)
    '10'
    >>> decimal_to_any(36, 36)
    '10'
    >>> # negatives will error
    >>> decimal_to_any(-45, 8)  # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    ValueError: parameter must be positive int
    >>> # floats will error
    >>> decimal_to_any(34.4, 6) # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: int() can't convert non-string with explicit base
    >>> # a float base will error
    >>> decimal_to_any(5, 2.5) # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: 'float' object cannot be interpreted as an integer
    >>> # a str base will error
    >>> decimal_to_any(10, '16') # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: 'str' object cannot be interpreted as an integer
    >>> # a base less than 2 will error
    >>> decimal_to_any(7, 0) # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    ValueError: base must be >= 2
    >>> # a base greater than 36 will error
    >>> decimal_to_any(34, 37) # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    ValueError: base must be <= 36
    """
    if isinstance(num, float):
        raise TypeError("int() can't convert non-string with explicit base")
    if num < 0:
        raise ValueError("parameter must be positive int")
    if isinstance(base, str):
        raise TypeError("'str' object cannot be interpreted as an integer")
    if isinstance(base, float):
        raise TypeError("'float' object cannot be interpreted as an integer")
    if base in (0, 1):
        raise ValueError("base must be >= 2")
    if base > 36:
        raise ValueError("base must be <= 36")
    # fmt: off
    ALPHABET_VALUES = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F',
                       '16': 'G', '17': 'H', '18': 'I', '19': 'J', '20': 'K', '21': 'L',
                       '22': 'M', '23': 'N', '24': 'O', '25': 'P', '26': 'Q', '27': 'R',
                       '28': 'S', '29': 'T', '30': 'U', '31': 'V', '32': 'W', '33': 'X',
                       '34': 'Y', '35': 'Z'}
    # fmt: on
    new_value = ""
    mod = 0
    div = 0
    while div != 1:
        div, mod = divmod(num, base)
        if base >= 11 and 9 < mod < 36:
            actual_value = ALPHABET_VALUES[str(mod)]
            mod = actual_value
        new_value += str(mod)
        div = num // base
        num = div
        
        if div == 0:
            lboxx3.insert(END, str(new_value[::-1]))
            return str(new_value[::-1])
            
        elif div == 1:
            new_value += str(div)
            
            lboxx3.insert(END, str(new_value[::-1]))
            return str(new_value[::-1])
       
    return new_value[::-1]

lboxx3 = tk.Listbox(root, bd=7)
lboxx3.grid(row=16, column=5)

if __name__ == "__main__":
    import doctest

    doctest.testmod()

    for base in range(2, 37):
        for num in range(1000):
            assert int(decimal_to_any(num, base), base) == num, (
                num,
                base,
                decimal_to_any(num, base),
                int(decimal_to_any(num, base), base) )
            lboxx3.delete(0, END)
            


def clearlist():
    lboxx1.delete(0, END)
    lboxx2.delete(0, END)
    lboxx3.delete(0, END)

def nothing():
    pass
label1 = tk.Label(root, text="Input Whole Number:")
label1.grid(row=2, column=1)
label1 = tk.Label(root, text="Select the Base (2-36):")
label1.grid(row=2, column=2)   
tk.Label(root, text=" Decimal to Selected Base Converter").grid(row=2, column=3)
en1 = tk.Entry(root, bg="wheat", bd=7)
en1.grid(row=5, column=1)
sp = tk.Spinbox(root, from_= 2, to = 36, increment=1, font=('sans-serif', 10))
sp.grid(row=5, column=2)               
               

lboxx1 = tk.Listbox(root, bd=7)
lboxx1.grid(row=16, column=3)
lboxx2 = tk.Listbox(root, bd=7)
lboxx2.grid(row=16, column=4)


b1 = tk.Button(root, text="Convert", bd=7, command=lambda: from_entry(en1.get(), sp.get())) 
b1.grid(row=20, column=1)
b2 = tk.Button(root, text="Clear", bd=7, command=clearlist)
b2.grid(row=20, column=2) 
b3 = tk.Button(root, text="feature", bd=7, command=nothing)
b3.grid(row=20, column=3) 

root.mainloop()
             
           
