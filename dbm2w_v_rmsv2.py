import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter as tk
import math



root = tk.Tk()
root.title("dBm to Watts, Volts")
def dBmtoW(*args):
    try:
        num11 = float(e3.get())
        num111 = float(num11)
        
        num2 = 10 ** (num111 / 20)
        num3 = float(num2) * 0.2236
        num4 = float(num3) * 1.414
        num5 = float(num4) * 2
        print(num111, num2, num3, num4, num5)
        lbox.insert(1, num11)
        lbox.insert(2, num2)
        lbox.insert(3, num3)
        lbox.insert(4, num4)
        lbox.insert(5, num5)
        

        lbox2.insert(1, "dBm")
        lbox2.insert(2, "mW")
        lbox2.insert(3, "Volts RMS")
        lbox2.insert(4, "Volts Peak")
        lbox2.insert(5, "Volts PK-PK")
    except ValueError as ex:
        print(ex)
  
    return


e3 = tk.Entry(root, bd=7, bg="seashell", font=("Arial", 8))
e3.grid(row=0, column=2)
e3.focus()
tk.Label(root, text="dBm                                                 ").grid(row=0, column=3)
btn2 = tk.Button(root, text="Calculate", bd=5, bg="light blue",  command=dBmtoW)
btn2.grid(column=1, row=1)

lbox = tk.Listbox(root, bd=7, bg="seashell")
lbox.grid(column=2, row=3)


lbox2 = tk.Listbox(root, bd=7, bg="seashell")
lbox2.grid(column=3, row=3)



