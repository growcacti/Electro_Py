import tkinter as tk
from tkinter import *
# ohms law with GUI for power and resistance
# --- functions ---

def convert():
    if cb1.get == 'in':
        mm = 25.4 + float(e1.get())
        cm = 2.54 + float(e1.get())




    if cb2.get() == 'mm':
         e3.insert(0, mm)

    if cb2.get() == 'cm':
         e3.insert(0, cm)

    if cb2.get() == 'cm':
         e3.insert(0, mm)


    if cb2.get() == 'cm':
         e3.insert(0, mm)


if cb2.get() == 'cm':
         e3.insert(0, mm)

         



         e3.insert(0, cm)
         e3.insert(0, km)
         e3.insert(0, mm)
         e3.insert(0, mm)
    
    
    
    


def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

# --- main ---

root = tk.Tk()
root.title("Unit Converter")
root.geometry("600x350")

tk.Label(root, text="-").grid(row=0, column=0)
tk.Label(root, text="_").grid(row=1, column=0)
tk.Label(root, text="_").grid(row=2, column=0)
tk.Label(root, text="_").grid(row=3, column=0)
from_units = ['in', 'ft', 'mi','mm', 'cm', 'm', 'km']
to_unit = ['mm', 'cm', 'm', 'km','in', 'ft', 'mi']
e1 = tk.Entry(root)
e1.grid(row=0, column=1)
cb1 = ttk.Combobox(root, values = from_units)
cb1.grid(row=0, column=2)
cb2 = ttk.Combobox(root, values = to_units)
cb2.grid(row=0, column=2)
to_val =  cb2.get()
e2 = tk.Entry(root)
e2.grid(row=1, column=1)
e3 = tk.Entry(root)
e3.grid(row=2, column=1)
e4 = tk.Entry(root)
e4.grid(row=3, column=1)
btn1 = tk.Button(root, text="Calculate", command=convert)
btn1.grid(row=4, column=1)
btn2 = tk.Button(root, text="clear", command=clear)
btn2.grid(row=5, column=1)
root.mainloop()

