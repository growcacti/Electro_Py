import tkinter as tk
from tkinter import ttk
from tkinter import *
import math

def clearlb():
    lb_1.delete(0, tk.END)
    lb_2.delete(0, tk.END)


def returnloss():
    try:
        vswr = str(float(vswrr.get()))

        coe1 = 1 - float(vswr)
        coe2 = 1 + float(vswr)
        coee = float(coe1) / float(coe2)
        coe = abs(coee)
        coesq = float(coe) * float(coe)
        rl = math.log10(float(coe)) * 20
        ml = math.log10(1 - float(coesq)) * 10
        print(coe1, coe2, coee, coe, rl, ml)
        
        lb_1.insert(1, vswrr.get())
        lb_1.insert(2, coe1)
        lb_1.insert(3, coe2)
        lb_1.insert(4, coee)
        lb_1.insert(5, coe)
        lb_1.insert(6, ml)
        lb_1.insert(7, rl)

         
        lb_2.insert(1, "vswr")
        lb_2.insert(2, "coe")
        lb_2.insert(3, "coe")
        lb_2.insert(4, "coee")
        lb_2.insert(5, "electr")
        lb_2.insert(6, "Mismatch Loss")
        lb_2.insert(7, "Return Loss")
    except Exception as ex:
        lb_1.insert(1, ex)
    return
    
root9 = tk.Tk()
root9.title("VSWR to Retrunloss Calcuation App")

tk.Label(root9, text="VSWR to Return Loss dB").grid(column=0, row=0)
vswrr = Entry(root9)
vswrr.grid(column=1, row=1)
lb_1 = tk.Listbox(root9)
lb_1.grid(column=1, row=3)
lb_2 = tk.Listbox(root9)
lb_2.grid(column=2, row=3)
btn98 = Button(root9, text="Convert", command=returnloss).grid(column=0, row=5)
btn99 = Button(root9, text="Clear", command=clearlb).grid(column=0, row=7)

root9.mainloop()
