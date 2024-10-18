import tkinter as tk
from tkinter import messagebox

class BaseConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Base Converter")
        
        # Create the GUI
        self.create_widgets()

    def create_widgets(self):
        # Number input
        label_number = tk.Label(self.root, text="Enter the number:")
        label_number.grid(row=0, column=0, padx=10, pady=10)
        self.entry_number = tk.Entry(self.root, bd=5)
        self.entry_number.grid(row=0, column=1, padx=10, pady=10)

        # Base of the number
        label_base_from = tk.Label(self.root, text="Base of the number (2-36):")
        label_base_from.grid(row=1, column=0, padx=10, pady=10)
        self.entry_base_from = tk.Entry(self.root, bd=5)
        self.entry_base_from.grid(row=1, column=1, padx=10, pady=10)

        # Target base
        label_base_to = tk.Label(self.root, text="Convert to base (2-36):")
        label_base_to.grid(row=2, column=0, padx=10, pady=10)
        self.entry_base_to = tk.Entry(self.root, bd=5)
        self.entry_base_to.grid(row=2, column=1, padx=10, pady=10)

        # Convert button
        button_convert = tk.Button(self.root, text="Convert", bd=6, command=self.convert)
        button_convert.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Result label
        label_result = tk.Label(self.root, text="Result: ")
        label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Result entry
        self.result_entry = tk.Entry(self.root, bd=10)
        self.result_entry.grid(row=5, column=1, padx=10, pady=10)

    def base_check(self, xnumber, xbase):
        valid_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:int(xbase)]
        for char in xnumber.upper():
            if char not in valid_chars:
                return False
        return True

    def convert_from_10(self, xnumber, xbase):
        arr = []
        while xnumber > 0:
            remainder = xnumber % xbase
            arr.append("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[remainder])
            xnumber = xnumber // xbase
        return ''.join(arr[::-1]) if arr else "0"

    def convert_to_10(self, xnumber, xbase):
        xnumber = xnumber.upper()
        return sum("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(char) * (xbase ** idx) for idx, char in enumerate(xnumber[::-1]))

    def convert(self):
        number = self.entry_number.get().upper()
        base_from = int(self.entry_base_from.get())
        base_to = int(self.entry_base_to.get())

        # Check if the input number is valid for the source base
        if not self.base_check(number, base_from):
            messagebox.showerror("Invalid Input", f"{number} is not a valid base {base_from} number.")
            return
        
        # Convert to base 10 first
        if base_from == 10:
            number_in_10 = int(number)
        else:
            number_in_10 = self.convert_to_10(number, base_from)
        
        # Convert from base 10 to the target base
        if base_to == 10:
            result = str(number_in_10)
        else:
            result = self.convert_from_10(number_in_10, base_to)
        
        # Display the result in the result entry box
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, result)

# Tkinter GUI setup
root = tk.Tk()
app = BaseConverterApp(root)
root.mainloop()
