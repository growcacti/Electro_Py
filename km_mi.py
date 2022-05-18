import tkinter as tk
from tkinter import ttk, END
#from tkinter import *
# ohms law with GUI for power and resistance
# --- functions ---

def convert():

    try:

        if cb1.get() == 'km':
             km = float(e1.get())
             mi = km / 1.609
             
             e3.insert(0, float(mi))
             tk.Label(root, text="Miles                                     ").grid(row=2, column=3)

        if cb1.get() == 'mi':
             mi = float(e1.get())
             km = mi * 1.609
             e3.insert(0, float(km))
             tk.Label(root, text="Kilometers                                 ").grid(row=2, column=3)



    except Exception as ex:
        print(ex)

    


         
    
    
    


def clear():
    e1.delete(0, END)
    ##e2.delete(0, END)
    e3.delete(0, END)
    #e4.delete(0, END)
    tk.Label(root, text="                                                        ").grid(row=2, column=3)
    
     # --- main ---

root = tk.Tk()
root.title("Unit Converter Miles & Kilometers")
root.geometry("600x350")

tk.Label(root, text="-").grid(row=0, column=0)
tk.Label(root, text="_").grid(row=1, column=0)
tk.Label(root, text="_").grid(row=2, column=0)
tk.Label(root, text="_").grid(row=3, column=0)
from_units = ['km','mi']
#to_unit = ['km', 'cm', 'm', 'km','in', 'ft', 'mi']
e1 = tk.Entry(root, bd=5, bg="seashell")
e1.grid(row=0, column=1)
cb1 = ttk.Combobox(root, values = from_units)
cb1.grid(row=0, column=2)
#cb2 = ttk.Combobox(root, values = to_units)
#cb2.grid(row=0, column=2)

##e2 = tk.Entry(root)
##e2.grid(row=1, column=1)
e3 = tk.Entry(root, bd=5, bg="seashell")
e3.grid(row=2, column=1)
##e4 = tk.Entry(root)
##e4.grid(row=3, column=1)
btn1 = tk.Button(root, text="Calculate", bd=5, bg="light green", command=convert)
btn1.grid(row=4, column=1)
btn2 = tk.Button(root, text="clear", bd=5, bg="light blue", command=clear)
btn2.grid(row=5, column=1)
root.mainloop()

