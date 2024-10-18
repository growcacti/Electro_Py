import tkinter as tk
from tkinter import messagebox

# Check if number is valid for the given base
def base_check(xnumber, xbase):
    valid_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:int(xbase)]
    for char in xnumber.upper():
        if char not in valid_chars:
            return False
    return True

# Convert a number from base 10 to another base
def convert_from_10(xnumber, xbase):
    arr = []
    while xnumber > 0:
        remainder = xnumber % xbase
        arr.append("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[remainder])
        xnumber = xnumber // xbase
    return ''.join(arr[::-1]) if arr else "0"

# Convert a number from another base to base 10
def convert_to_10(xnumber, xbase):
    xnumber = xnumber.upper()
    return sum("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(char) * (xbase ** idx) for idx, char in enumerate(xnumber[::-1]))

# Perform the base conversion
def convert():
    number = entry_number.get().upper()
    base_from = int(entry_base_from.get())
    base_to = int(entry_base_to.get())
    
    # Check if the input number is valid for the source base
    if not base_check(number, base_from):
        messagebox.showerror("Invalid Input", f"{number} is not a valid base {base_from} number.")
        return
    
    # Convert to base 10 first
    if base_from == 10:
        number_in_10 = int(number)
    else:
        number_in_10 = convert_to_10(number, base_from)
    
    # Convert from base 10 to the target base
    if base_to == 10:
        result = str(number_in_10)
    else:
        result = convert_from_10(number_in_10, base_to)
    
    #label_result.config(text=f"Result: {result}")
    result_entry.insert(0, f" {result}")
# Tkinter GUI setup
root = tk.Tk()
root.title("Base Converter")

label_number = tk.Label(root, text="Enter the number:")
label_number.grid(row=0, column=0, padx=10, pady=10)
entry_number = tk.Entry(root, bd=5)
entry_number.grid(row=0, column=1, padx=10, pady=10)

label_base_from = tk.Label(root, text="Base of the number (2-36):")
label_base_from.grid(row=1, column=0, padx=10, pady=10)
entry_base_from = tk.Entry(root,bd=5)
entry_base_from.grid(row=1, column=1, padx=10, pady=10)

label_base_to = tk.Label(root, text="Convert to base (2-36):")
label_base_to.grid(row=2, column=0, padx=10, pady=10)
entry_base_to = tk.Entry(root,bd=5)
entry_base_to.grid(row=2, column=1, padx=10, pady=10)

button_convert = tk.Button(root, text="Convert",bd=6, command=convert)
button_convert.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

label_result = tk.Label(root, text="Result: ")
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
result_entry = tk.Entry(root, bd=10)
result_entry.grid(row=5, column=1, padx=10, pady=10)

root.mainloop()
