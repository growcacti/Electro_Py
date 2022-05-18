import tkinter as tk
from tkinter import ttk
from tkinter import *
# ohms law with GUI for power and resistance
# --- functions ---

def convert(tc):
    sel = cb1.get()
    if sel == '°C':
        c = float(tc)
        f = (float(c) * 1.8) + 32
        print(f)
        e3.insert(END, float(f))
        e4.insert(END, '-------------------')
        tk.Label(root, text="°F                                   ").grid(row=2, column=2)
    elif sel == '°F':
        f = float(tc)
        c = (float(f) - 32) * 0.555
        print(c)
        e4.insert(END, float(c))
        e3.insert(END, '-------------------')
        tk.Label(root, text="°C                                    ").grid(row=3, column=2)

 



   
 


    
    
    


def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    tk.Label(root, text="                                     ").grid(row=2, column=2)
    tk.Label(root, text="                                     ").grid(row=3, column=2)

# --- main ---

root = tk.Tk()
root.title("Temperature Converter JH Math APPS")
root.geometry("600x350")

tk.Label(root, text="").grid(row=0, column=0)
tk.Label(root, text="").grid(row=1, column=0)
tk.Label(root, text="").grid(row=2, column=2)
tk.Label(root, text="").grid(row=3, column=2)
from_units = ['°C', '°F']
to_unit = ['°C', '°F']
e1 = tk.Entry(root, bd=7, bg="seashell")
e1.grid(row=0, column=1)
tk.Label(root, text="<<------ Select Temperature Unit From").grid(row=0, column=3)
cb1 = ttk.Combobox(root, values = from_units)
cb1.grid(row=0, column=2)
##cb2 = ttk.Combobox(root, values = to_units)
##cb2.grid(row=0, column=2)
##to_val =  cb2.get()
e2 = tk.Entry(root, bd=7, bg="seashell")
e2.grid(row=1, column=1)
e3 = tk.Entry(root, bd=7, bg="seashell")
e3.grid(row=2, column=1)
e4 = tk.Entry(root, bd=7, bg="seashell")
e4.grid(row=3, column=1)
btn1 = tk.Button(root, text="Calculate", bd=6, bg='light green', command=lambda :convert(float(e1.get())))
btn1.grid(row=4, column=1)
btn2 = tk.Button(root, text="CLEAR", bd=6, bg='light blue', command=clear)
btn2.grid(row=5, column=1)
root.mainloop()

