import tkinter as tk
from tkinter import *
from tkinter import ttk
import math

r = tk.Tk()
r.geometry('1000x300')
r.title("Math APPS Octal to Decimal, Hex, & Binary")



lboxx3 = tk.Listbox(r, width=10)
lboxx3.grid(row=10, column=4)
lboxx4 = tk.Listbox(r, width=40)
lboxx4.grid(row=10, column=5)

                    

def from_entry(num):

    try:
        num = str(en1.get())
        
        lboxx1.insert(END, num)
        print(num)
        numstr = "num"
        oct_to_decimal(num)
        
    # except block 
    except ValueError as ex:
        print(ex)
        lboxx1.insert(END, ex)
    



def oct_to_decimal(oct_string: str) -> int:
    """
    Convert a octal value to its decimal equivalent

    >>> oct_to_decimal("12")
    10
    >>> oct_to_decimal(" 12   ")
    10
    >>> oct_to_decimal("-45")
    -37
    >>> oct_to_decimal("2-0Fm")
    Traceback (most recent call last):
    ...
    ValueError: Non-octal value was passed to the function
    >>> oct_to_decimal("")
    Traceback (most recent call last):
    ...
    ValueError: Empty string was passed to the function
    >>> oct_to_decimal("19")
    Traceback (most recent call last):
    ...
    ValueError: Non-octal value was passed to the function
    """
    oct_string = str(oct_string).strip()
    if not oct_string:
        raise ValueError("Empty string was passed to the function")
    is_negative = oct_string[0] == "-"
    if is_negative:
        oct_string = oct_string[1:]
    if not oct_string.isdigit() or not all(0 <= int(char) <= 7 for char in oct_string):
        raise ValueError("Non-octal value was passed to the function")
    decimal_number = 0
    for char in oct_string:
        decimal_number = 8 * decimal_number + int(char)
    if is_negative:
        decimal_number = -decimal_number
    dec = decimal_number
    lboxx3.insert(END, dec)
    lboxx4.insert(END, decimal_to_binary(dec))
    lboxx2.insert(END, decimal_to_hexadecimal(dec))
    return decimal_number

""" Convert Base 10 (Decimal) Values to Hexadecimal Representations """

# set decimal value for each hexadecimal digit
values = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "a",
    11: "b",
    12: "c",
    13: "d",
    14: "e",
    15: "f",
}


def decimal_to_hexadecimal(decimal: float) -> str:
    """
    take integer decimal value, return hexadecimal representation as str beginning
    with 0x
    >>> decimal_to_hexadecimal(5)
    '0x5'
    >>> decimal_to_hexadecimal(15)
    '0xf'
    >>> decimal_to_hexadecimal(37)
    '0x25'
    >>> decimal_to_hexadecimal(255)
    '0xff'
    >>> decimal_to_hexadecimal(4096)
    '0x1000'
    >>> decimal_to_hexadecimal(999098)
    '0xf3eba'
    >>> # negatives work too
    >>> decimal_to_hexadecimal(-256)
    '-0x100'
    >>> # floats are acceptable if equivalent to an int
    >>> decimal_to_hexadecimal(17.0)
    '0x11'
    >>> # other floats will error
    >>> decimal_to_hexadecimal(16.16) # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    AssertionError
    >>> # strings will error as well
    >>> decimal_to_hexadecimal('0xfffff') # doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    AssertionError
    >>> # results are the same when compared to Python's default hex function
    >>> decimal_to_hexadecimal(-256) == hex(-256)
    True
    """
    assert type(decimal) in (int, float) and decimal == int(decimal)
    decimal = int(decimal)
    hexadecimal = ""
    negative = False
    if decimal < 0:
        negative = True
        decimal *= -1
    while decimal > 0:
        decimal, remainder = divmod(decimal, 16)
        hexadecimal = values[remainder] + hexadecimal
    hexadecimal = "0x" + hexadecimal
    if negative:
        hexadecimal = "-" + hexadecimal
    
  
    return hexadecimal



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
        return "-0b" + "".join(str(e) for e in binary)

    return "0b" + "".join(str(e) for e in binary)
##if __name__ == "__main__":
##    from doctest import testmod
##
##    testmod()

def clearlist():
    lboxx1.delete(0, END)
    lboxx2.delete(0, END)
    lboxx3.delete(0, END)
    lboxx4.delete(0, END)



label1 = tk.Label(r, text=" Input a Octal Number:")
label1.grid(row=1, column=2)
tk.Label(r, text="Oct").grid(row=5, column=2)
tk.Label(r, text="Hex").grid(row=5, column=3)
tk.Label(r, text="Decimal").grid(row=5, column=4)
tk.Label(r, text="Bin").grid(row=5, column=5)
en1 = tk.Entry(r, bg="wheat")
en1.grid(row=1, column=1)

lboxx1 = tk.Listbox(r, width=40)
lboxx1.grid(row=10, column=2)
lboxx2 = tk.Listbox(r, width=10)
lboxx2.grid(row=10, column=3)

b1 = tk.Button(r, text="Convert", command=lambda: from_entry(en1.get())) 
b1.grid(row=5, column=0)
b2 = tk.Button(r, text="Clear", command=clearlist)
b2.grid(row=6, column=0) 


if __name__ == "__main__":
    
    #import doctest
    #doctest.testmod()

    
    r.mainloop()

