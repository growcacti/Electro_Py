#!/usr/bin/python
# -*- coding: utf-8 -*-​
# dBm to mW and mw to dBm converter
import tkinter as tk
from tkinter import *
import sys
from math import log10


root = Tk()
label = tk.Label(root, text="dBm").grid(row=4, column=6)
lb = tk.Listbox(root, bd=5, bg="seashell")
lb.grid(row=5, column=6)
# Function to extract numbers from string
def getdigits(ch):
    if "," in ch:
        ch = ch.replace(',','.')
	

    if '.' in ch:
        return float(''.join(ele for ele in ch if ele.isdigit() or ele == '.'))
    else:
        return int(''.join(ele for ele in ch if ele.isdigit()))

# Function to convert from mW to dBm
def mW2dBm(mW):
    
    dBm_result = (10*log10(float((mW))))
    lb.insert(END, dBm_result)
    print(dBm_result)
    return 


# Function to convert from dBm to mW
def dBm2mW(dBm):
    mW_result = 10**(float((dBm)/10))
    
                     
    print(mW_result)


    return 



# Main thread
# if there's space between argument and "dBm"
if len(sys.argv) > 2:
    sys.argv[1] = sys.argv[1] + sys.argv[2]
    if len(sys.argv) > 1:
        if "MW" in sys.argv[1].upper():
            mW = getdigits(sys.argv[1])
            dBm = mW2dBm(mW)
            print( "%d mW = %0.2f dBm" %(mW, dBm))
        elif "DBM" in sys.argv[1].upper():



            
             dBm = getdigits(sys.argv[1])
             if "-" in sys.argv[1]:
                
                dBm = -dBm
                
                mW = dBm2mW(dBm)
                print("%0.2f dBm = %0.10f mW" %(dBm, mW))
        else:
            mW = dBm2mW(dBm)
                

    else:
            # bad syntax
            print("Usage: Enter input value as 9.99dBm or 999mW")
else:
    # print table for 100-2000 mW to dBm
    print( "Usage: Enter input value as 9.99dBm or 999mW")
    print( "-"*20)
    
    for mW in range(2000, 0, -100):
       
        dBm = mW2dBm(mW)
        
   
    # print table for 10-34 dBm to mW
    for dBm in range(10, 34, 1):
       
        mW = dBm2mW(dBm)
        
	
#def add_numbers():
    #a = float(a_var.get())
    #b = float(b_var.get())
    #result_var.set(str(a+b))
def lbclr():
    
    lb.delete(0, END)

 
# Use tkinter variables to talk to entry widgets
   
#result_var = StringVar()


 
mW = Entry(root, justify=RIGHT, bd=10, bg="seashell")
mW.grid(row=0, column=1)
  
label2 = Label(root, text='in milliwatt')
label2.grid(row=1, column=0)


    
btn1 = tk.Button(root, text='mW to dBm', bd=5, bg="violet", command=lambda: mW2dBm(mW.get()))
btn1.grid(row=3, column=2)
btn2 = tk.Button(root, text='clear', bd=5, bg="light green", command=lbclr)
btn2.grid(row=5, column=3)
          
root.mainloop()

 
