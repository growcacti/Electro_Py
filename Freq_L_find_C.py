import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import tkinter.font
import math
#can = tk.Canvas(root46, height=100, width=100)
#can.grid(column=5, row=9)
#This version was pulled from notebook to make it an import module because of GUI issues
#This should be the latest version of this code 11/29/2021
root46 = tk.Tk()
root46.geometry("1800x1000")
root46.title("LC Resonant Calculation")
options = [" ", "m", "u", "n", "p"]
option2 = ["Hz", "kHz", "MHz", "GHz", "THz"] 
n = ttk.Combobox(root46, values=option2, font=("Arial", 14))
n.set("Hz")
n.grid(row=1, column=3)
n2 = ttk.Combobox(root46, values=options, font=("Arial", 14))
n2.set("u")
n2.grid(row=4, column=3)
l1 = tk.Label(root46, text="Frequency Value)", font=("Arial", 14))
l1.grid(row=0, column=2)
l = tk.Entry(root46, bg="yellow", bd=7, font=("Arial", 14))
l.grid(row=1, column=2)
c1 = tk.Label(root46, text="Inductance Value", font=("Arial", 14))
c1.grid(row=3, column=2)
c = tk.Entry(root46, bd=7, bg="light blue", font=("Arial", 14))
c.grid(row=4, column=2)
zz = tk.Label(root46, text="               ")
zz.grid(row=0,column=0)
unitlabel_l = tk.Label(root46, text="Hertz", font=("Arial Black", 10))
unitlabel_l.grid(row=1, column=4)
unitlabel_c = tk.Label(root46, text="Henries", font=("Arial Black", 10))
unitlabel_c.grid(row=4, column=4)
##eq = tk.Label(root46, text=" Equation Resonant Frequency is 1 /  2pi x SQRT LxC", font=("Arial", 10))
##eq.grid(row=11, column=4)


def clearlist():
    lb5.delete(0, END)
    lb6.delete(0, END)





lb5 = tk.Listbox(root46, bd=10, bg="seashell", width=40)
lb5.grid(row=16,  column=4)
lb6 = tk.Listbox(root46, bd=10, bg="seashell", width=40)
lb6.grid(row=16, column=5)


clr_btn = tk.Button(root46, text='CLEAR', bd=7, bg="orange", font=("Arial Black", 12), command=clearlist)
clr_btn.grid(row=6, column=5)



def combo_calc(l, c, n, n2, *args):
    a = 1
    a2 = 1
    # Testing the passing arguements with print statements
    print(l, c, n, n2)
    # conditions below to adjust entry by converting string to interger and divide
    # by the value assoicated by the text from the combobox.
    # Could not convert the string to float, this failed.
    # It appears to must conver string to interger then to float.
    # This is why there is so much extra math done.
    try:
        if n == "Hz ":
            a2 = c
            a = l

        elif n == "Khz":

            a = str(int(l)  * 1000)

        elif n == "MHz":

            a = str(int(l)  * 1000000)

        elif n == "GHz":

            a = str(int(l) * 1000000000)

        elif n == "THz":

            a = str(int(l) * 1000000000000)



        if n2 == " ":

            a2 = str(int(c) * 1)

        elif n2 == "m":

            a2 = str(int(c) / 1000)

        elif n2 == "u":

            a2 = str(int(c) / 1000000)

        elif n2 == "n":

            a2 = str(int(c) / 1000000000)

        elif n2 == "p":

            a2 = str(int(c) / 1000000000000)

    except Exception as ex:
            print(ex)
        
    print (a)



    print(a2)

   
##
##    ttrl = tk.Label(root46, text="Engineering Notation Set", font=("Arial Black", 8))
##
##    ttrl.grid(row=2, column=7)



    #na = tk.Label(root46, text=na, font=("Arial Black", 8))

    #na.grid(row=3, column=7)

    print(a, a2)
    lb5.insert(1, a)
    lb5.insert(2, a2)
    
    lb6.insert(1, "Hz")
    lb6.insert(2, "Henries")
##    na2 = tk.Label(root46, text=na2, font=("Arial Black", 8))
##
##    na2.grid(row=4, column=7)

    ff = float(a) * float(a)
    pisq = math.pi * math.pi
    pi2 = math.pi * 2
    pi42 = pisq * 4
    w = float(pi2) * float(a)  
    piffcc = float(ff) * float(a2) * pi42

    print(pi2)
    print(pi42)
    print(pisq)
    print(piffcc)
    xL = pi2 * float(a) * float(a2)
    ad = 1 / float(xL)
    cap = 1 / float(piffcc)
    uF = 10e5 * cap
    nF = 10e8 * cap
    pf = 10e11 * cap
    
    #print(freq)
    lb5.insert(3, xL)
    lb6.insert(3, "ohms")
    lb5.insert(4, cap)
    lb6.insert(4, "F")
    lb5.insert(5, uF)
    lb6.insert(5, "uF")
    lb5.insert(6, nF)
    lb6.insert(6, "nF")
    lb5.insert(7, pf)
    lb6.insert(7, "pF")
    lb5.insert(8, w)
    lb6.insert(8, "(w) angular freq")
    lb5.insert(9, ad)
    lb6.insert(9, "Admittance")






calc_button = tk.Button(root46, text='Calculate>>', bd=7, bg="orange", font=("Arial Black", 12), command = lambda: combo_calc(l.get(), c.get(), n.get(), n2.get()))
calc_button.grid(row=5, column=5)    
    #c_reactance = 1 / (pi2 * 4 * float(na)*float(na) *float(na2))
    #inductance = 1 / (pi2 * freq * float(a2))
#     l_admittance = 1 / l_reactance
##    c_admittance = 1 / c_reactance
##    kHz = freq / 1000
##    Mhz = kHz / 1000
##    a8 = kHz
##    a10 = Mhz
##    a4 = freq
##    a4 = Label(root46, text=inductance, font=("Arial Black", 12))
##    a4.grid(row=11, column=2)
##    a6 = Label(root46, text="H", font=("Arial Black", 12))
##    a6.grid(row=11, column=3)
##    a8 = Label(root46, text=kHz, font=("Arial Black", 12))
##    a8.grid(row=12, column=2)
##    a9 = Label(root46, text="kHz", font=("Arial Black", 12))
##    a9.grid(row=12, column=3)
##    a10 = Label(root46, text=Mhz, font=("Arial Black", 12))
##    a10.grid(row=13, column=2)
##    a11 = Label(root46, text="MHz", font=("Arial Black", 12))
##    a11.grid(row=13, column=3)
##    a12 = Label(root46, text=l_reactance, font=("Arial", 10))
##    a12.grid(row=9,column=7)
##    a13 = Label(root46, text=" LC Reactance Impedance in OHMS", font=("Arial", 10))
##    a13.grid(row=9,column=7)
##    a14 = Label(root46, text=c_reactance, font=("Arial", 10))
##    a14.grid(row=10,column=7)
##    
##    a17 = Label(root46, text="Admittance Values for XL & XC", font=("Arial", 10))
##    a17.grid(row=13 ,column=7)
##    a18 = Label(root46, text=l_admittance, font=("Arial", 10))
##    a18.grid(row=14 ,column=7)
##    a19 = Label(root46, text=c_admittance, font=("Arial", 10))
##    a19.grid(row=15 ,column=7)

    # Goal is top present every caculation answer for future math apps
    
##    lb5.insert(4, kHz)
##    lb5.insert(5, Mhz)
##    lb5.insert(6, l_reactance)
##    lb5.insert(7, c_reactance)
##    lb5.insert(8, l_admittance)
##    lb5.insert(9, c_admittance)
##    lb5.insert(10, invfreq)
##    lb6.insert(4, "kHz")
##    lb6.insert(5, "Mhz")
##    lb6.insert(6, "XL inductive Reactance")
##    lb6.insert(7, "XC Capacitance Reactance")
##    lb6.insert(8, "Inductive Admittance")
##    lb6.insert(9, "Admittance Capactive")
##    lb6.insert(10, "Time sec")
##    return
