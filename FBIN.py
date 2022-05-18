import tkinter as tk
from tkinter import *
from tkinter import ttk
import math

r = tk.Tk()
r.geometry('1200x400')
r.title("Math APPS Binary to Octal, Decimal, Hexidecimal")



lboxx3 = tk.Listbox(r, width=10)
lboxx3.grid(row=10, column=4)
lboxx4 = tk.Listbox(r, width=40)
lboxx4.grid(row=10, column=5)

                    

def from_entry(bin):

    try:
        bin1 = str(en1.get())
        
        lboxx1.insert(END, bin1)
        print(bin1)
        numstr = "num"
        bin_to_decimal(bin1)
        bin_to_octal(bin1)
    # except block 
    except ValueError as ex:
        print(ex)
        lboxx1.insert(END, ex)


def bin_to_octal(bin_string: str) -> str:
    if not all(char in "01" for char in bin_string):
        raise ValueError("Non-binary value was passed to the function")
    if not bin_string:
        raise ValueError("Empty string was passed to the function")
    oct_string = ""
    while len(bin_string) % 3 != 0:
        bin_string = "0" + bin_string
    bin_string_in_3_list = [
        bin_string[index : index + 3]
        for index in range(len(bin_string))
        if index % 3 == 0
    ]
    for bin_group in bin_string_in_3_list:
        oct_val = 0
        for index, val in enumerate(bin_group):
            oct_val += int(2 ** (2 - index) * int(val))
        oct_string += str(oct_val)
    return oct_string, lboxx2.insert(END, oct_string)

        
    
def bin_to_decimal(bin_string: str) -> int:
    """
    Convert a binary value to its decimal equivalent

    >>> bin_to_decimal("101")
    5
    >>> bin_to_decimal(" 1010   ")
    10
    >>> bin_to_decimal("-11101")
    -29
    >>> bin_to_decimal("0")
    0
    >>> bin_to_decimal("a")
    Traceback (most recent call last):
    ...
    ValueError: Non-binary value was passed to the function
    >>> bin_to_decimal("")
    Traceback (most recent call last):
    ...
    ValueError: Empty string was passed to the function
    >>> bin_to_decimal("39")
    Traceback (most recent call last):
    ...
    ValueError: Non-binary value was passed to the function
    """
    bin_string = str(bin_string).strip()
    if not bin_string:
        raise ValueError("Empty string was passed to the function")
    is_negative = bin_string[0] == "-"
    if is_negative:
        bin_string = bin_string[1:]
    if not all(char in "01" for char in bin_string):
        raise ValueError("Non-binary value was passed to the function")
    decimal_number = 0
    for char in bin_string:
        decimal_number = 2 * decimal_number + int(char)
        dec = decimal_number
        
    return -decimal_number if is_negative else decimal_number, lboxx3.insert(END, dec), lboxx4.insert(END, decimal_to_hexadecimal(dec)


)



# Modified from:
# https://github.com/TheAlgorithms/Javascript/blob/master/Conversions/DecimalToOctal.js


def decimal_to_octal(num: int) -> str:
    """Convert a Decimal Number to an Octal Number.

    >>> all(decimal_to_octal(i) == oct(i) for i
    ...     in (0, 2, 8, 64, 65, 216, 255, 256, 512))
    True
    """
    octal = 0
    counter = 0
    while num > 0:
        remainder = num % 8
        octal = octal + (remainder * math.floor(math.pow(10, counter)))
        counter += 1
        num = math.floor(num / 8)  # basically /= 8 without remainder if any
        # This formatting removes trailing '.0' from `octal`.
    return f"0o{int(octal)}"


def main() -> None:
    """Print octal equivalents of decimal numbers."""
    print("\n2 in octal is:")
    print(decimal_to_octal(2))  # = 2
    print("\n8 in octal is:")
    print(decimal_to_octal(8))  # = 10
    print("\n65 in octal is:")
    print(decimal_to_octal(65))  # = 101
    print("\n216 in octal is:")
    print(decimal_to_octal(216))  # = 330
    print("\n512 in octal is:")
    print(decimal_to_octal(512))  # = 1000
    print("\n")






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




def clearlist():
    lboxx1.delete(0, END)
    lboxx2.delete(0, END)
    lboxx3.delete(0, END)
    lboxx4.delete(0, END)



label1 = tk.Label(r, text=" Input a Binary Number:  ex: 1010101")
label1.grid(row=1, column=2)
tk.Label(r, text="Bin").grid(row=5, column=2)
tk.Label(r, text="OCT").grid(row=5, column=3)
tk.Label(r, text="Decimal").grid(row=5, column=4)
tk.Label(r, text="HEX").grid(row=5, column=5)
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
    
  

    
    r.mainloop()

