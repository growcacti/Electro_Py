import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import tkinter.font
import math
#can = tk.Canvas(root45, height=100, width=100)
#can.grid(column=5, row=9)
#This version was pulled from notebook to make it an import module because of GUI issues
#This should be the latest version of this code 11/29/2021
root45 = tk.Tk()
root45.geometry("1800x1000")
root45.title("LC Resonant Calculation")
options = [" ", "m", "u", "n", "p"]
option2 = ["Hz", "kHz", "MHz", "GHz", "THz"] 
n = ttk.Combobox(root45, values=option2, font=("Arial", 14))
n.set("Hz")
n.grid(row=1, column=3)
n2 = ttk.Combobox(root45, values=options, font=("Arial", 14))
n2.set("p")
n2.grid(row=4, column=3)
l1 = tk.Label(root45, text="Frequency Value)", font=("Arial", 14))
l1.grid(row=0, column=2)
freq = tk.Entry(root45, bd=10, bg="yellow", font=("Arial", 14))
freq.grid(row=1, column=2)
c1 = tk.Label(root45, text="Capcitance Value", font=("Arial", 14))
c1.grid(row=3, column=2)
c = tk.Entry(root45, bd=10, bg="light blue", font=("Arial", 14))
c.grid(row=4, column=2)
zz = tk.Label(root45, text="               ")
zz.grid(row=0,column=0)
unitlabel_l = tk.Label(root45, text="Hertz", font=("Arial Black", 10))
unitlabel_l.grid(row=1, column=4)
unitlabel_c = tk.Label(root45, text="Farads", font=("Arial Black", 10))
unitlabel_c.grid(row=4, column=4)
##eq = tk.Label(root45, text=" Equation Resonant Frequency is 1 /  2pi x SQRT LxC", font=("Arial", 10))
##eq.grid(row=11, column=4)



def clearlist():
    lb5.delete(0, END)
    lb6.delete(0, END)
    



lb5 = tk.Listbox(root45, bd=10, bg="seashell", width=40)
lb5.grid(row=16,  column=4)
lb6 = tk.Listbox(root45, bd=10, bg="lavender", width=40)
lb6.grid(row=16, column=5)




clr_btn = tk.Button(root45, text='CLEAR', bd=7, bg="orange", font=("Arial Black", 12), command=clearlist)
clr_btn.grid(row=6, column=5)



def combo_calc(a, a2, n, n2, *args):
    a = float(freq.get())
    a2 = float(c.get())
    # Testing the passing arguements with print statements
 
    # conditions below to adjust entry by converting string to interger and divide
    # by the value assoicated by the text from the combobox.
    # Could not convert the string to float, this failed.
    # It appears to must conver string to interger then to float.
    # This is why there is so much extra math done.
    try:
        if n == "Hz":
            a2 = a2 / 1  
            aa = a / 1 

        elif n == "Khz":

            aa = str(int(a)  * 1000)

        elif n == "MHz":

            aa = str(int(a)  * 1000000)

        elif n == "GHz":

            aa = str(int(a) * 1000000000)

        elif n == "THz":

            aa = str(int(a) * 1000000000000)



        if n2 == " ":

            aa2 = str(int(a2) * 1)

        elif n2 == "m":

            aa2 = str(int(a2) / 1000)

        elif n2 == "u":

            aa2 = str(int(a2) / 1000000)

        elif n2 == "n":

            aa2 = str(int(a2) / 1000000000)

        elif n2 == "p":

            aa2 = str(int(a2) / 1000000000000)

    except Exception as ex:
            print(ex)
        
    print (aa)



    print(aa2)

    
##
##    ttrl = tk.Label(root45, text="Engineering Notation Set", font=("Arial Black", 8))
##
##    ttrl.grid(row=2, column=7)



    #na = tk.Label(root45, text=na, font=("Arial Black", 8))

    #na.grid(row=3, column=7)

    print(aa, aa2)
    lb5.insert(1, aa)
    lb5.insert(2, aa2)
    
    lb6.insert(1, "Hz")
    lb6.insert(2, "Farads")
##    na2 = tk.Label(root45, text=na2, font=(
    pi2 = math.pi * 2
    pi42 = pi2 ** 2
    ff = float(aa) ** 2
   
  
    piffcc = float(ff) * float(aa2) * pi42
    w = float(pi2) * float(aa)
    print(pi2)
    print(pi42)

    dfreq = float(ff) * pi42
    print(piffcc)
    ad = (pi2 * float(aa) * float(aa2))
    xc = 1 / ad
    ind = 1 / float(piffcc)
    uH = 10e5 * ind
    mH = 10e2 * ind
    #print(freq)
    lb5.insert(3, xc)
    lb6.insert(3, "ohms")
    lb5.insert(4, ind)
    lb6.insert(4, "H")
    lb5.insert(5, uH)
    lb6.insert(5, "uH")
    lb5.insert(6, mH)
    lb6.insert(6, "mH")
    lb5.insert(7, w)
    lb6.insert(7, "(w) angular freq")
    lb5.insert(8, ad)
    lb6.insert(8, "Admittance")
    



calc_button = tk.Button(root45, text='Calculate>>', bd=7,  bg="orange", font=("Arial Black", 12), command = lambda: combo_calc(freq.get(), c.get(), n.get(), n2.get()))
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
##    a4 = Label(root45, text=inductance, font=("Arial Black", 12))
##    a4.grid(row=11, column=2)
##    a6 = Label(root45, text="H", font=("Arial Black", 12))
##    a6.grid(row=11, column=3)
##    a8 = Label(root45, text=kHz, font=("Arial Black", 12))
##    a8.grid(row=12, column=2)
##    a9 = Label(root45, text="kHz", font=("Arial Black", 12))
##    a9.grid(row=12, column=3)
##    a10 = Label(root45, text=Mhz, font=("Arial Black", 12))
##    a10.grid(row=13, column=2)
##    a11 = Label(root45, text="MHz", font=("Arial Black", 12))
##    a11.grid(row=13, column=3)
##    a12 = Label(root45, text=l_reactance, font=("Arial", 10))
##    a12.grid(row=9,column=7)
##    a13 = Label(root45, text=" LC Reactance Impedance in OHMS", font=("Arial", 10))
##    a13.grid(row=9,column=7)
##    a14 = Label(root45, text=c_reactance, font=("Arial", 10))
##    a14.grid(row=10,column=7)
##    
##    a17 = Label(root45, text="Admittance Values for XL & XC", font=("Arial", 10))
##    a17.grid(row=13 ,column=7)
##    a18 = Label(root45, text=l_admittance, font=("Arial", 10))
##    a18.grid(row=14 ,column=7)
##    a19 = Label(root45, text=c_admittance, font=("Arial", 10))
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
