import tkinter as tk
from tkinter import *
from tkinter import ttk
import math

r = tk.Tk()
r.geometry('1000x300')
r.title("Math APPS")



lboxx3 = tk.Listbox(r, bd=10, width=20)
lboxx3.grid(row=10, column=4)
lboxx4 = tk.Listbox(r, bd=10, width=20)
lboxx4.grid(row=10, column=5)
hex_table = {hex(i)[2:]: i for i in range(16)}  # Use [:2] to strip off the leading '0x'


def hex_to_decimal(hex_string: str) -> int:
    """
    Convert a hexadecimal value to its decimal equivalent
    #https://www.programiz.com/python-programming/methods/built-in/hex

    >>> hex_to_decimal("a")
    10
    >>> hex_to_decimal("12f")
    303
    >>> hex_to_decimal("   12f   ")
    303
    >>> hex_to_decimal("FfFf")
    65535
    >>> hex_to_decimal("-Ff")
    -255
    >>> hex_to_decimal("F-f")
    Traceback (most recent call last):
    ...
    ValueError: Non-hexadecimal value was passed to the function
    >>> hex_to_decimal("")
    Traceback (most recent call last):
    ...
    ValueError: Empty string was passed to the function
    >>> hex_to_decimal("12m")
    Traceback (most recent call last):
    ...
    ValueError: Non-hexadecimal value was passed to the function
    """
    hex_string = hex_string.strip().lower()
    if not hex_string:
        raise ValueError("Empty string was passed to the function")
    is_negative = hex_string[0] == "-"
    if is_negative:
        hex_string = hex_string[1:]
    if not all(char in hex_table for char in hex_string):
        raise ValueError("Non-hexadecimal value was passed to the function")
    decimal_number = 0
    for char in hex_string:
        decimal_number = 16 * decimal_number + hex_table[char]
    dec = decimal_number
    lboxx2.insert(END, decimal_to_octal(dec))
    lboxx3.insert(END, dec)
    
    return -decimal_number if is_negative else decimal_number

def hex_to_bin(hex_num: str) -> int:
    """
    Convert a hexadecimal value to its binary equivalent
    #https://stackoverflow.com/questions/1425493/convert-hex-to-binary
    Here, we have used the bitwise right shift operator: >>
    Shifts the bits of the number to the right and fills 0 on voids left as a result.
    Similar effect as of dividing the number with some power of two.
    Example:
    a = 10
    a >> 1 = 5

    >>> hex_to_bin("AC")
    10101100
    >>> hex_to_bin("9A4")
    100110100100
    >>> hex_to_bin("   12f   ")
    100101111
    >>> hex_to_bin("FfFf")
    1111111111111111
    >>> hex_to_bin("-fFfF")
    -1111111111111111
    >>> hex_to_bin("F-f")
    Traceback (most recent call last):
    ...
    ValueError: Invalid value was passed to the functiondecimal_to_octal
    >>> hex_to_bin("")
    Traceback (most recent call last):
    ...
    ValueError: No value was passed to the function
    """

    hex_num = hex_num.strip()
    if not hex_num:
        raise ValueError("No value was passed to the function")

    is_negative = hex_num[0] == "-"
    if is_negative:
        hex_num = hex_num[1:]

    try:
        int_num = int(hex_num, 16)
    except ValueError:
        raise ValueError("Invalid value was passed to the function")

    bin_str = ""
    while int_num > 0:
        bin_str = str(int_num % 2) + bin_str
        int_num >>= 1
       
    return int(("-" + bin_str) if is_negative else bin_str), lboxx4.insert(END, bin_str)


"""Convert a Decimal Number to an Octal Number."""


# Modified from:

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



                    

def from_entry(num):

    try:
        num = str(en1.get())
        
        lboxx1.insert(END, num)
        print(num)
        numstr = "num"
        hex_to_decimal(num)
        hex_to_bin(num)
    # except block 
    except ValueError as ex:
        print(ex)   
    




def clearlist():
    lboxx1.delete(0, END)
    lboxx2.delete(0, END)
    lboxx3.delete(0, END)
    lboxx4.delete(0, END)



label1 = tk.Label(r, text=" Input a Hexidecmal Number:")
label1.grid(row=1, column=2)
tk.Label(r, text="Hex").grid(row=5, column=2)
tk.Label(r, text=" Oct").grid(row=5, column=3)
tk.Label(r, text="Decimal").grid(row=5, column=4)
tk.Label(r, text="Bin").grid(row=5, column=5)
en1 = tk.Entry(r, bd=7, bg="wheat")
en1.grid(row=1, column=1)

lboxx1 = tk.Listbox(r, bd=10, width=20)
lboxx1.grid(row=10, column=2)
lboxx2 = tk.Listbox(r, bd=10, width=40)
lboxx2.grid(row=10, column=3)

b1 = tk.Button(r, text="Convert", bd=7, bg="orange", command=lambda: from_entry(en1.get())) 
b1.grid(row=5, column=0)
b2 = tk.Button(r, text="Clear", bd=7, bg="cyan2", command=clearlist)
b2.grid(row=6, column=0) 


if __name__ == "__main__":
    import doctest

    #doctest.testmod()
r.mainloop()

