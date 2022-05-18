import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import tkinter.font
import math
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

import os
import sys 

root = tk.Tk()
root.geometry('1200x800')
root.title("Resistor Voltage Divider Calc")


#templete of standard startcode.
#remove unused imports as needed
def generate():
    try:
        r1 = num111.get()
        r2 = num222.get()
        vv1 = vvv1.get()
        con1 = 1 / float(r1) # seems to work better if done in steps
        con2 = 1 / float(r2) # con is for conductance
        consum = float(con1) + float(con2)       
        num333 = 1/float(consum)
        num444 = float(r1) + float(r2) #using float is obvious way
        result3 = float(r2) / float(num444)
        I2 = float(vv1) / float(num444)
        vdiv1 = float(I2) * float(r1)
        vdiv11 = float(I2) * float(r2)
        pwr1 = float(I2) * float(vv1)
        lb7.insert(1, r1)
        lb7.insert(2, r2)
        lb7.insert(3, vv1)
        lb7.insert(4, con1)
        lb7.insert(5, con2)
        lb7.insert(6, consum)
        lb7.insert(7, num333)
        lb7.insert(8, num444)
        lb7.insert(9, result3)
        lb7.insert(10, I2)
        lb7.insert(11, vdiv1)
        lb7.insert(12, vdiv11)
        lb7.insert(13, pwr1)
        lb9.insert(1, "R1")
        lb9.insert(2, "R2")
        lb9.insert(3, "Vin")
        lb9.insert(4, "1/R1")
        lb9.insert(5, "1/R2")
        lb9.insert(6, "1/R +1/R2")
        lb9.insert(7, "RT Parallel")
        lb9.insert(8, "Series R1 + R2")
        lb9.insert(9, "R2 / R1 + R2")
        lb9.insert(10, "I2 Vin / Rt Series")
        lb9.insert(11, "VR1")
        lb9.insert(12, "VR2")
        lb9.insert(13, "Power")
    except Exception as ex: 
        print(ex)
        result = 'error'
                   
                
def gen2():
    try:
        r01 = num1234.get()
        r02 = num4567.get()
        r03 = num7891.get()
        r04 = num1112.get() 
        vv2 = vvv2.get()        
        ccon1 = 1 / float(r01) # seems to work better if done in steps
        ccon2 = 1 / float(r02) # con is for conductance
        ccon3 = 1 / float(r03) # con is for conductance
        ccon4 = 1 / float(r04) # con is for conductance
        num333 = float(ccon1) + float(ccon2) + float(ccon3) + float(ccon4)     
        num444 = 1 / float(num333)
        rtotal2 = float(r01) + float(r02) + float(r03) + float(r04)
        numout44 = float(rtotal2)
        I4 = float(vv2) / float(numout44)
        num9999 = float(I4) * float(r01)
        num8888 = float(I4) * float(r02)
        num7777 = float(I4) * float(r03)         
        num6666 = float(I4) * float(r04)
        pwr2 = float(I4) * float(vv2)
        lb8.insert(1, r01)
        lb8.insert(2, r02)
        lb8.insert(3, r03)
        lb8.insert(4, r04)
        lb8.insert(5, vv2)
        lb8.insert(6, ccon1)
        lb8.insert(7, ccon2)
        lb8.insert(8, ccon3)
        lb8.insert(9, ccon4)
        lb8.insert(10, num333)
        lb8.insert(11, num444)
        lb8.insert(12, rtotal2)
        lb8.insert(13, I4)
        lb8.insert(14, num9999)
        lb8.insert(15, num8888)
        lb8.insert(16, num7777)
        lb8.insert(17, num6666)
        lb8.insert(18, pwr2)
       
       

        lb10.insert(1, "R1")
        lb10.insert(2, "R2")
        lb10.insert(3, "R3")
        lb10.insert(4, "R4")
        lb10.insert(5, "Vin")
        lb10.insert(6, "1/R1")
        lb10.insert(7, "1/R2")
        lb10.insert(8, "1/R3")
        lb10.insert(9, "1/R4")
        lb10.insert(10, "SUM INV R1-R4")
        lb10.insert(11, "RT Parallel")
        lb10.insert(12, "RT series")
        lb10.insert(13, "Current")
        lb10.insert(14, "VR1")
        lb10.insert(15, "VR2")
        lb10.insert(16, "VR3")
        lb10.insert(17, "VR4")
        lb10.insert(18, "Power")
        
        
                   
    except Exception as ex: 
        print(ex)
        result = 'error'
def clearlist1():
    lb7.delete(0, END)
    lb9.delete(0, END)
    vvv1.delete(0, END)
    num111.delete(0, END)
    num222.delete(0, END)
def clearlist2():
    lb8.delete(0, END)
    lb10.delete(0, END)
    num1234.delete(0, END)
    num4567.delete(0, END)
    num7891.delete(0, END)
    num1112.delete(0, END)
    vvv2.delete(0, END)
# --- main ---

tk.Label(root, text=" Input R1:").grid(row=0, column=0)
tk.Label(root, text="Input R2:").grid(row=1, column=0)
tk.Label(root, text="Vin for Vdiv").grid(row=2, column=0)
num111 = tk.Entry(root, bd=7, bg="seashell")
num111.grid(row=0, column=1)
num222 = tk.Entry(root, bd=7, bg="cornsilk")
num222.grid(row=1, column=1)

vvv1 = tk.Entry(root, bd=7, bg="seashell")
vvv1.grid(row=2, column=1)
lb7 = tk.Listbox(root, height=20, bd=10, bg="violet")
lb7.grid(row=6,  column=2)
lb9 = tk.Listbox(root, height=20, bd=10, bg="pink")
lb9.grid(row=6,  column=1)
b1 = tk.Button(root, text="Calculate", bd=5, bg='cyan', command=generate)
b1.grid(row=6, column=0)
b3 = tk.Button(root, text="Clear", bd=5, bg='orange', command=clearlist1)
b3.grid(row=7, column=0)
num1234 = tk.Entry(root, bd=7, bg="cornsilk")
num1234.grid(row=0, column=5)
num4567 = tk.Entry(root, bd=7, bg="seashell")
num4567.grid(row=1, column=5)
 
num7891 = tk.Entry(root, bd=7,  bg="cornsilk")
num7891.grid(row=2, column=5)
num1112 = tk.Entry(root, bd=7,  bg="wheat")
num1112.grid(row=3, column=5)
vvv2 = tk.Entry(root, bd=7, bg="seashell")
vvv2.grid(row=4, column=5)
#num9999 = 
#num8888 =
#num7777 = 
#num6666 = 

tk.Label(root, text=" Input R1:").grid(row=0, column=4)
tk.Label(root, text="Input R2:").grid(row=1, column=4)
tk.Label(root, text="Input R3:").grid(row=2, column=4)
tk.Label(root, text="Input R4").grid(row=3, column=4)
tk.Label(root, text="Vin").grid(row=4, column=4)




lb8 = tk.Listbox(root, bd=10, bg="light blue", height=20)
lb8.grid(row=6,  column=7)
lb10 = tk.Listbox(root, bd=10, bg="light green", height=20)
lb10.grid(row=6,  column=6)
b2 = tk.Button(root, text="Calculate 4 Resistor", bd=5, bg="plum",  command=gen2)
b2.grid(row=6, column=5)
b4 = tk.Button(root, text="Clear", bd=5, bg="orange", command=clearlist2)
b4.grid(row=7, column=5)



















root.mainloop()
