import tkinter as tk
from tkinter import Entry, END, Button, Label, StringVar
# ohms law with GUI for Voltage and Power
# --- functions ---

def generate():
    try:
        result = float(num1.get()) * float(num2.get())
        
        result2 = float(num1.get()) * float(num1.get()) * float(num2.get())
    except Exception as ex:
        print(ex)
        result = 'error'

    e3.insert(0, result)
    e4.insert(0, result2)


def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)



# --- main ---

root = tk.Tk()

num1 = tk.StringVar()
num2 = tk.StringVar()
num3 = tk.StringVar()
num4 = tk.StringVar()
tk.Label(root, text=" Input Amps:").grid(row=0, column=0)
tk.Label(root, text="Input Ohms:").grid(row=1, column=0)
tk.Label(root, text=" Output Volts:").grid(row=2, column=0)
tk.Label(root, text="Output Watts:").grid(row=3, column=0)

e1 = tk.Entry(root, textvariable=num1)
e1.grid(row=0, column=1)
e2 = tk.Entry(root, textvariable=num2)
e2.grid(row=1, column=1)
e3 = tk.Entry(root, textvariable=num3)
e3.grid(row=2, column=1)
e4 = tk.Entry(root, textvariable=num4)
e4.grid(row=3, column=1)
btn1 = tk.Button(root, text="Calculate", command=generate)
btn1.grid(row=4, column=1)
btn2 = tk.Button(root, text="clear", command=clear)
btn2.grid(row=5, column=1)
root.mainloop()
