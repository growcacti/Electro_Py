import tkinter as tk
from tkinter import ttk
from tkinter import *
import math


r = tk.Tk()
r.title("JH Math App Engineering Notation")
r.geometry('600x500')

#r = ttk.Frame(r)    #height=450, width=450)





options = [ "T", "G", "M", "k", "h", "da", " ", "d", "c", "m", "u", "n", "p"]
n = ttk.Combobox(r, values=options, font=("Arial", 14))
n.set("m")
n.grid(row=1, column=3)
n2 = ttk.Combobox(r, values=options, font=("Arial", 14))
n2.set("m")
n2.grid(row=4, column=3)
l1 = tk.Label(r, text="Value", font=("Arial", 14))
l1.grid(row=0, column=2)
l = tk.Entry(r, bg="cyan", font=("Arial", 14))
l.grid(row=1, column=2)
c1 = tk.Label(r, text="Value", font=("Arial", 14))
c1.grid(row=3, column=2)
c = tk.Entry(r, bg="pink", font=("Arial", 14))
c.grid(row=4, column=2)
zz = tk.Label(r, text="----")
zz.grid(row=0, column=0)
unitlabel_l = tk.Label(r, text="Unit Value", font=("Arial Black", 10))
unitlabel_l.grid(row=1, column=4)
unitlabel_c = tk.Label(r, text="Unit Value", font=("Arial Black", 10))
unitlabel_c.grid(row=4, column=4)
# This funcction is callec eunc for Engineering Unit Notation Calculation
def eunc(l, c, n, n2, *args):
    try:
        num = int(l)
        num2 = int(c)
        print(num, num2)
    except ValueError as ex:
        print(ex)
       
    if n == "T":
    
        a = str(int(l) * 10e12)

    elif n == "G":

        a = str(int(l) * 10e9)

    elif n == "M":

         a = str(int(l) * 10e6)
    elif n == "k":

         a = str(int(l) * 1000)
    elif n == "h":

         a = str(int(l) * 100)
    elif n == "da":

          a = str(int(l) * 10)

    elif n == " ":
         a2 = c
         a = l

    elif n == "d":

         a = str(int(l)  / 10)

    elif n == "c":

        a = str(int(l)  / 100)

    elif n == "m":

        a = str(int(l)  / 1000)

    elif n == "u":

        a = str(int(l)  / 1000000)

    elif n == "n":

        a = str(int(l) / 1000000000)

    elif n == "p":

        a = str(int(l) / 1000000000000)
#-------------------------------------


    if n2 == "T":
        
        a2 = str(int(c) * 10e12)

    elif n2 == "G":

        a2 = str(int(c) * 10e9)

    elif n2 == "M":

         a2 = str(int(c) * 10e6)
    elif n2 == "k":

         a2 = str(int(c) * 1000)
    elif n2 == "h":

         a2 = str(int(l) * 100)
    elif n2 == "da":

         a2 = str(int(l) * 10)

    elif n2 == " ":
         a2 = c
         a = l

    elif n2 == "d":

         a2 = str(int(c)  / 10)

    elif n2 == "c":

        a2 = str(int(c)  / 100)

    elif n2 == "m":

        a2 = str(int(c)  / 1000)

    elif n2 == "u":

        a2 = str(int(c)  / 1000000)

    elif n2 == "n":

        a2 = str(int(c) / 1000000000)

    elif n2 == "p":

        a2 = str(int(c) / 1000000000000)

     
            
    else:
        contnue
            
        print (a)



        print(a2)

        na = a
        na2 = a2
        return
    ttrl = tk.Label(r, text="Engineering Notation Set", font=("Arial Black", 8))

    ttrl.grid(row=5, column=2)
    tk.Label(r, text=a, font=("Arial Black", 14)).grid(row=10, column=2)
    tk.Label(r, text=a2, font=("Arial Black", 14)).grid(row=12, column=2)

calc_button = tk.Button(r, text='Calculate>>', bg="orange", font=("Arial Black", 12), command=lambda: eunc(l.get(), c.get(), n.get(), n2.get()))
calc_button.grid(row=7, column=3)
#n.bind("<<ComboboxSelected>>", eunc)
#n2.bind("<<ComboboxSelected>>", eunc)
#l.bind("<Key>", eunc)
#l.focus_set()
#c.bind("<Key>", eunc)
#c.focus_set()

    ##
##units_prefix = {
##                'tera'   : (1000000000000, 10**12),
##                'giga'   : (1000000000, 10**9),
##                'mega'   : (1000000, 10**6),
##                'kilo'   : (1000, 10**3),
##                'hecta'  : (100, 10**2),
##                'deca'   : (10, 10),
##                'base'   : (1,1),
##                'deci'   : (0.1, 10**-1),
##                'centi'  : (0.01, 10**-2),
##                'milli'  : (0.001, 10**-3),
##                'micro'  : (0.000001, 10**-6),
##                'nano'   : (0.000000001, 10**-9),
##                'pico'   : (0.000000000001, 10**-12)
##                }
##
##units = {
##        'T'   : (1000000000000, 10**12),
##        'G'   : (1000000000, 10**9),
##        'M'   : (1000000, 10**6),
##        'k'   : (1000, 10**3),
##        'h'   : (100, 10**2),
##        'da'  : (10, 10),
##        'base': (1,1),
##        'd'   : (0.1, 10**-1), 
##        'c'   : (0.01, 10**-2),
##        'm'   : (0.001, 10**-3),
##        'u'   : (0.000001, 10**-6),
##        'n'   : (0.000000001, 10**-9),
##        'p'   : (0.000000000001, 10**-12)
##        }
r.mainloop()
