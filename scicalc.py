import tkinter as tk
from tkinter import ttk, Canvas, Frame, filedialog, font
from tkinter import *
import math
from math import *


root = tk.Tk()

root.title("Math App Ver2")


root.geometry('1000x1900')


answer_ee2 = 0
cc_complete = 0

frm1 = ttk.Frame(root, height=20, width=200)
frm1.grid(row=0, column=1, columnspan=2)
frm1.columnconfigure(0, weight=4)
frm1.columnconfigure(1, weight=5)
frm2 = ttk.Frame(root, height=100, width=1800)
frm2.grid(row=5, column=2)


frm3 = ttk.Frame(root, height=500, width=1800)
frm3.grid(row=10, column=4)
tk.Label(frm3, text="Store Temp Values").grid(row=24, column=2)
lb = tk.Listbox(frm3)
lb.grid(row=25, column=1)

tk.Label(frm3, text="Experimental").grid(row=24, column=3)
tk.Label(frm3, text="As Memory").grid(row=24, column=1)
e1 = tk.Entry(frm1, bd=5, bg= "wheat")
e1.grid(row=0, column=0, padx=20, sticky="w")
e2 = tk.Entry(frm1, bd=5, bg= "light blue")
e2.grid(row=0, column=1, padx=20, sticky="w")
e3 = tk.Entry(frm1, bd=5, bg= "light green")
e3.grid(row=0, column=2, padx=20, sticky="w")
e4 = tk.Entry(frm1, bd=5, bg= "light pink")
e4.grid(row=0, column=3, padx=20, sticky="w")


e6 = Entry(frm1, bd=5, bg= "wheat")
e6.grid(row=1, column=1)
tk.Label(frm1, text="                ").grid(row=2, column=0)
tk.Label(frm1, text="                ").grid(row=3, column=1)
tk.Label(frm1, text="                ").grid(row=2, column=2)
tk.Label(frm1, text="                ").grid(row=3, column=2)
tk.Label(frm1, text="                ").grid(row=2, column=3)
tk.Label(frm1, text="                ").grid(row=3, column=3)
def add():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        e3.insert(END, e2.get())
        e2.delete(0, END)
        
        
    
    ee1 = float(e1.get())   
    e2.insert(END, ee1)
    ee2 = e2.get()
    e1.delete(0, END)
  
    
    def eq():
        if not len(e6.get()) == 0:
            lb.insert(1, e6.get())
            e6.delete(0, END)
        ee1 = float(e1.get())
        ee2 = float(e2.get())
        answer = float(ee1) + float(ee2)
        tk.Label(frm1, text="         ----Answer----                   ").grid(row=3, column=1)
        return  e6.insert(END, answer)
        


    eqbtn1 = tk.Button(frm1, text='  =  ', bd=5, bg= 'AntiqueWhite2', font=('URW Chancery L',8,'bold'), command=eq)
    eqbtn1.grid(row=1, column=0)



def subtract():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        e3.insert(END, e2.get())
        e2.delete(0, END)
    
    ee1 = e1.get()
    e2.insert(END, ee1)
    ee2 = e2.get()
    e1.delete(0, END)
  
    
    def eq():
        if not len(e6.get()) == 0:
            lb.insert(1, e6.get())
            e6.delete(0, END)
        ee1 = float(e1.get())
        ee2 = float(e2.get())
        answer = float(ee2) - float(ee1)
        tk.Label(frm1, text="         ----Answer----                   ").grid(row=3, column=1)
        return  e6.insert(END, answer)
        


    eqbtn1 = tk.Button(frm1, text='  =  ', bd=5, bg= 'AntiqueWhite2', font=('URW Chancery L',8,'bold'), command=eq)
    eqbtn1.grid(row=1, column=0)



def mul():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        e3.insert(END, e2.get())
        e2.delete(0, END)
    ee1 = e1.get()
    e2.insert(END, ee1)
    ee2 = e2.get()
    e1.delete(0, END)
   
    
    def eq():
        if not len(e6.get()) == 0:
            lb.insert(1, e6.get())
            e6.delete(0, END)
        ee1 = float(e1.get())
        ee2 = float(e2.get())
        answer = float(ee2) * float(ee1)
        tk.Label(frm1, text="         ----Answer----                   ").grid(row=3, column=1)
        return  e6.insert(END, answer)
    eqbtn1 = tk.Button(frm1, text='  =  ', bd=5, bg='AntiqueWhite2', font=('URW Chancery L',15,'bold'), command=eq)
    eqbtn1.grid(row=1, column=0)
def div():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        e3.insert(END, e2.get())
        e2.delete(0, END)
    ee1 = e1.get()
    e2.insert(END, ee1)
    ee2 = e2.get()
    e1.delete(0, END)
  
    
    def eq():
        if not len(e6.get()) == 0:
            lb.insert(1, e6.get())
            e6.delete(0, END)
        ee1 = float(e1.get())
        ee2 = float(e2.get())
       
        if ee1 == 0:
            e6.insert(END, "Undefined")
            tk.Label(frm1, text="-----Infinite-----").grid(row=2, column=1)
            tk.Label(frm1, text="-------Value------").grid(row=3, column=1)
        else:    
            
            answer = float(ee2) / float(ee1)
            tk.Label(frm1, text="-------Answer-------").grid(row=3, column=1) 
            return  e6.insert(END, answer)
    
        

    eqbtn1 = tk.Button(frm1, text='  =  ', bd=5, bg= 'AntiqueWhite3', font=('URW Chancery L',15,'bold'), command=eq)
    eqbtn1.grid(row=1, column=0)



    
def cmd():
    pass
def one():
    e1.insert(END, 1)
    
    return 1
def two():
    e1.insert(END, 2)
    
    return 2
def three():
    e1.insert(END, 3)
    
    return 3
def four():
    e1.insert(END, 4)
    return 4
def five():
    e1.insert(END, 5)
    
    return 5
def six():
    e1.insert(END, 6)
   
    return 6
def seven():
    e1.insert(END, 7)
    
    return 7


def eight():
    e1.insert(END, 8)
    
    return 8
def nine():
    e1.insert(END, 9)
   
    return 9
def zero():
    e1.insert(END, 0)

    return 0


def clearall():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e6.delete(0, END)
    tk.Label(frm1, text="                         ").grid(row=2, column=1)
    tk.Label(frm1, text="                         ").grid(row=3, column=1)
def clear1():
     e1.delete(0, END)



def clear2():
     e2.delete(0, END)


def clear3():
     e3.delete(0, END)

     
def clear4():
     e4.delete(0, END)


def clear6():
    e6.delete(0, END)
    tk.Label(frm1, text="                      ").grid(row=2, column=1)
    tk.Label(frm1, text="                       ").grid(row=3, column=1)


def clrmem():
    lb.delete(0, END)

def recall_mem(event=None):
    try:
        mc = lb.curselection()[0]
        ee5 = lb.get(mc)
        e1.insert(END, ee5)
    except Exception as ex:
        tk.Label(frm1, text="nothing selected").grid(row=3, column=1)
        print(ex)


lb.bind("<Double-Button-1>", recall_mem)
lb.bind("<<ListboxSelect>>", recall_mem)

def sto1():
    ee1 = e1.get()
    lb.insert(1, ee1)
    e1.delete(0, END)

def stoans():
    lb.insert(1, e6.get())
    e6.delete(0, END)


def shift4():
    ee4 = e4.get()
    lb.insert(END, ee4)
    e4.delete(0, END)





def shift3():
    ee3 = e3.get()
    e4.insert(END, ee3)
    e3.delete(0, END)



def shift2():
    ee2 = e2.get()
    e3.insert(END, ee2)
    e2.delete(0, END)




    
def shift1():
    ee1 = e1.get()
    e2.insert(0, ee1)
    e1.delete(0, END)
########################################################################################################
###Sci Calc Function    
#
########################################################################################################
########################################################################################################


def factorial():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        e3.insert(END, e2.get())
        e2.delete(0, END)
    ee1 = int(e1.get())
    answer = math.factorial(ee1)
    e6.insert(END, answer)
    tk.Label(frm1, text="         ----Answer----                   ").grid(row=2, column=1) 




def fmod():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        e3.insert(END, e2.get())
        e2.delete(0, END)
    ee1 = float(e1.get())
    e2.insert(END, ee1)
    ee2 = float(e2.get())
    e1.delete(0, END)
    def eq():
         if not len(e6.get()) == 0:
            lb.insert(1, e6.get())
            e6.delete(0, END)
         ee1 = float(e1.get())
         ee2 = float(e2.get())
         answer = math.fmod(ee1, ee2)
         tk.Label(frm1, text="         ----Answer----                   ").grid(row=2, column=1)
         return  e6.insert(END, answer)
    eqbtn1 = tk.Button(frm1, text='  =  ', bd=5, bg='ivory2', font=('URW Chancery L',15,'bold'), command=eq)
    eqbtn1.grid(row=1, column=0)       
    
    


    eqbtn1 = tk.Button(frm1, text='  =  ', bd=5, bg= 'AntiqueWhite3', font=('URW Chancery L',15,'bold'), command=eq)
    eqbtn1.grid(row=1, column=0)
    



def epown():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        e3.insert(END, e2.get())
        e2.delete(0, END)

    ee1 = float(e1.get())
    answer = math.exp(ee1)
    e6.insert(END, answer)
    tk.Label(frm1, text="         ----Answer----                   ").grid(row=2, column=1) 
    return answer








def epownm1():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        e3.insert(END, e2.get())
        e2.delete(0, END)
    ee1 = float(e1.get())
    answer = math.expm1(ee1)
    e6.insert(END, answer)
    tk.Label(frm1, text="         ----Answer----                   ").grid(row=2, column=1) 
    return answer



#math.log(x[, base])
#With one argument, return the natural logarithm of x (to base e).
#With two arguments, return the logarithm of x to the given base, calculated as log(x)/log(base).


def loge():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        e3.insert(END, e2.get())
        e2.delete(0, END)
    ee1 = float(e1.get())
    answer = math.log1p(ee1)
    e6.insert(END, answer)
    tk.Label(frm1, text="         ----Answer----                   ").grid(row=2, column=1) 
    return answer




def log():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        e3.insert(END, e2.get())
        e2.delete(0, END)
    ee1 = float(e1.get())
    e2.insert(END, ee1)
    ee2 = float(e2.get())
    e1.delete(0, END)
    tk.Label(frm1, text="Enter Base").grid(row=2, column=0)
    def eq():
        if not len(e6.get()) == 0:
            lb.insert(1, e6.get())
            e6.delete(0, END)
        ee1 = float(e1.get())
        ee2 = float(e2.get())
        answer = math.log(ee1, ee2)
        e6.insert(END, answer)
        tk.Label(frm1, text="         ----Answer----                   ").grid(row=2, column=1)
        return

        

    eqbtn1 = tk.Button(frm1, text='  =  ', bd=5, bg= 'cornsilk', font=('URW Chancery L',15,'bold'), command=eq)
    eqbtn1.grid(row=1, column=0)

   

def log10():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        e3.insert(END, e2.get())
        e2.delete(0, END)
    ee1 = float(e1.get())
    answer = math.log10(ee1)
    e6.insert(END, answer)
    tk.Label(frm1, text="         ----Answer----                   ").grid(row=2, column=1)
    


def pow_of_var():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        e3.insert(END, e2.get())
        e2.delete(0, END)
    ee1 = float(e1.get())
    e2.insert(END, ee1)
    ee2 = float(e2.get())
    e1.delete(0, END)
    tk.Label(frm1, text="Enter number raised").grid(row=2, column=0)
    def eq():
         if not len(e6.get()) == 0:
             lb.insert(1, e6.get())
             e6.delete(0, END)
         ee1 = float(e1.get())
         ee2 = float(e2.get())
         answer = math.pow(ee1, ee2)
         e6.insert(END, answer)
         tk.Label(frm1, text="         ----Answer----                   ").grid(row=2, column=1) 
         return
    eqbtn1 = tk.Button(frm1, text='  =  ', bd=5, bg= 'lavender', font=('URW Chancery L',15,'bold'), command=eq)
    eqbtn1.grid(row=1, column=0)




def sqrt():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        e2.delete(0, END)
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())
    answer = math.sqrt(ee2)
    e6.insert(END, answer)
    return answer



def inv():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        e2.delete(0, END)
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())
    if ee2 == 0:
              e6.insert(END, "Undefined")
              tk.Label(frm1, text="----ERROR----").grid(row=2, column=1) 

    else:
        answer = 1 / ee2
        e6.insert(END, answer)
        tk.Label(frm1, text="         ----Answer----                   ").grid(row=2, column=1)
    return



def sin():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        e2.delete(0, END)
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())
    answer = math.sin(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="         ----Answer----                   ").grid(row=2, column=1)
    return




def cos():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        e2.delete(0, END)
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())
    answer = math.cos(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="         ----Answer----                   ").grid(row=2, column=1)
    return
          




def tan():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        e2.delete(0, END)
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())
    answer = math.tan(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="         ----Answer----                   ").grid(row=2, column=1)
    return




def asin():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        e2.delete(0, END)
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())
    answer = math.asin(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="         ----Answer----                   ").grid(row=2, column=1)
    return




def acos():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        e2.delete(0, END)
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())
    answer = math.acos(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="         ----Answer----                   ").grid(row=2, column=1)
    return




def atan():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        e2.delete(0, END)
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())

    answer = math.atan(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="         ----Answer----                   ").grid(row=2, column=1)
    return





def sinh():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        e2.delete(0, END)
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())
    answer = math.sinh(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="         ----Answer----                   ").grid(row=2, column=1)
    return



def cosh():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        e2.delete(0, END)
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())
    answer = math.cosh(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="         ----Answer----                   ").grid(row=2, column=1)
    return




def tanh():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        e2.delete(0, END)
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())

    answer = math.tanh(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="         ----Answer----                   ").grid(row=2, column=1)
    return



def asinh():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        e2.delete(0, END)
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())

    answer = math.asinh(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="         ----Answer----                   ").grid(row=2, column=1)
    return



def acosh():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        e2.delete(0, END)
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())
    answer = math.acosh(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="         ----Answer----                   ").grid(row=2, column=1)
    return




def atanh():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        e2.delete(0, END)
    e2.insert(END, float(e1.get()))
    e1.delete(0, END)
    ee2 = float(e2.get())

    answer = math.tanh(ee2)
    e6.insert(END, answer)
    tk.Label(frm1, text="         ----Answer----                   ").grid(row=2, column=1)
    return


              
              
def signchr():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        e2.delete(0, END)
    e2.insert(END, ans)
    e1.delete(0, END)
    return
        

    
def hyp():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        e2.delete(0, END)
    
    ee1 = float(e1.get())
    e2.insert(END, ee1)
    ee2 = float(e2.get())
    e1.delete(0, END)
    tk.Label(frm1, text="").grid(row=2, column=0)
    def eq():
        if not len(e6.get()) == 0:
            lb.insert(1, e6.get())
            e6.delete(0, END)
        ee1 = float(e1.get())
        ee2 = float(e2.get())
        answer = math.hypot(ee1, ee2)
        e6.insert(END, answer)
        tk.Label(frm1, text="         ----Answer----                   ").grid(row=2, column=1)
        return
    
    eqbtn1 = tk.Button(frm1, text='  =  ', bd=5, bg='azure', font=('URW Chancery L',15,'bold'), command=eq)
    eqbtn1.grid(row=1, column=0)



def pi():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e6.get()) == 0:
        lb.insert(1, e6.get())
        e6.delete(0, END)

    if not len(e2.get()) == 0:
         
        lb.insert(1, e2.get())
        e2.delete(0, END)
    pi = float(math.pi)
    pie = pi
    e2.insert(END, pie)
    lb3.insert(1, pie)
    return pie


def absolute_value():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        e2.delete(0, END)
    if not len(e6.get()) == 0:
        lb.insert(1, e6.get())
        e6.delete(0, END)
        ans = abs(float(e1.get()))

    e2.insert(END, ans)    



def pi2():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        e2.delete(0, END)
    if not len(e6.get()) == 0:
        lb.insert(1, e6.get())
        e6.delete(0, END)
   

    pi = float(math.pi)
    pi2 = pi * 2
    e2.insert(END, pi2)
    lb3.insert(1, pi2)
    return pi2


def half_pi():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        e2.delete(0, END)
    if not len(e6.get()) == 0:
        lb.insert(1, e6.get())
        e6.delete(0, END)
   
    pi = float(math.pi)
    halfpi = float(pi) / 2
    e2.insert(END, halfpi)
    lb3.insert(1, halfpi)
    return halfpi

def quarter_pi():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        e2.delete(0, END)
    if not len(e6.get()) == 0:
        lb.insert(1, e6.get())
        e6.delete(0, END)

        if not len(e2.get()) == 0:
                lb.insert(1, e2.get())
                e2.delete(0, END)
    pi = float(math.pi)
    quartpi = pi / 4
    e2.insert(END, quartpi)
    lb3.insert(1, quartpi)
    return quartpi

def eighth_pi():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        e2.delete(0, END)
    if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        e2.delete(0, END)

    if not len(e6.get()) == 0:
            lb.insert(1, e6.get())
            e6.delete(0, END)
    pi = float(math.pi)
    eighthpi = pi / 8
    e2.insert(END, eighthpi)
    lb3.insert(1, eighthpi)
    return eighthpi


def pi_div16():
    if not len(e4.get()) == 0:
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        e4.insert(END, e3.get())
        e3.delete(0, END)
    if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        e2.delete(0, END)
    if not len(e6.get()) == 0:
        lb.insert(1, e6.get())
        e6.delete(0, END)

    
    pi = float(math.pi)
    sixteenthpi = pi / 16
    e2.insert(END, sixteenthpi)
    lb3.insert(1, sixteenthpi)
    return sixteenthpi











##############################################################################################################
###############################################################################################################
btn1 = tk.Button(frm2, text="Factorial", bd=5, bg= 'CadetBlue3', font=('URW Chancery L',8,'bold'), command=factorial)
btn1.grid(row=5, column=1)
btn2 = tk.Button(frm2, text="FMOD", bd=5, bg= 'DarkOrchid1', font=('URW Chancery L',8,'bold'), command=fmod)
btn2.grid(row=6, column=1)
btn3 = tk.Button(frm2, text="EPX", bd=5, bg= 'DarkSlateGray1', font=('URW Chancery L',8,'bold'), command=epown)
btn3.grid(row=7, column=1)
btn4 = tk.Button(frm2, text="EPX -1", bd=5, bg= 'DeepSkyBlue2', font=('URW Chancery L',8,'bold'), command=epownm1)
btn4.grid(row=8, column=1)
btn5 = tk.Button(frm2, text="LOG e", bd=5, bg= 'DodgerBlue2', font=('URW Chancery L',8,'bold'), command=loge)
btn5.grid(row=9, column=1)
btn6 = tk.Button(frm2, text="LOG", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=log)
btn6.grid(row=10, column=1)
btn7 = tk.Button(frm2, text="LOG10", bd=5, bg= 'cyan', font=('URW Chancery L',8,'bold'), command=log10)
btn7 .grid(row=11, column=1)
btn8 = tk.Button(frm2, text="POWER x,y", bd=5, bg= 'cornsilk', font=('URW Chancery L',8,'bold'), command=pow_of_var)
btn8.grid(row=12, column=1)
btn9 = tk.Button(frm2, text="1/X INV", bd=5, bg= 'wheat', font=('URW Chancery L',8,'bold'), command=inv)
btn9.grid(row=13, column=1)
btn10 = tk.Button(frm2, text="SQU ROOT", bd=5, bg= 'lavender', font=('URW Chancery L',8,'bold'), command=sqrt)
btn10.grid(row=14, column=1)
btn11 = tk.Button(frm2, text="Pi", bd=5, bg= 'yellow', font=('URW Chancery L',8,'bold'), command=pi)
btn11.grid(row=15, column=1)
btn12 = tk.Button(frm2, text="2Pi", bd=5, bg= 'lime green', font=('URW Chancery L',8,'bold'), command=pi2)
btn12.grid(row=16, column=1)
btn13 = tk.Button(frm2, text="Pi/2", bd=5, bg= 'violet', font=('URW Chancery L',8,'bold'), command=half_pi)
btn13.grid(row=17, column=1)
btn15 = tk.Button(frm2, text="Pi/4", bd=5, bg= 'light blue', font=('URW Chancery L',8,'bold'), command=quarter_pi)
btn15.grid(row=18, column=1)
btn16a = tk.Button(frm2, text="Pi/8", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=eighth_pi)
btn16a.grid(row=19, column=1)
btn15b = tk.Button(frm2, text="Pi/16", bd=5, bg= 'azure', font=('URW Chancery L',8,'bold'), command=quarter_pi)
btn15b.grid(row=20, column=1)

############################################################################################################

btn62 = tk.Button(frm2, text="  7  ", bd=5, bg= 'azure', font=('URW Chancery L',8,'bold'), command=seven)
btn62.grid(row=6, column=2)
btn63 = tk.Button(frm2, text="  4  ", bd=5, bg= 'azure', font=('URW Chancery L',8,'bold'), command=four)
btn63.grid(row=7, column=2)
btn0064 = tk.Button(frm2, text="  1  ", bd=5, bg= 'azure', font=('URW Chancery L',8,'bold'), command=one)
btn0064.grid(row=8, column=2)

btn51 = tk.Button(frm2, text="btn", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn51.grid(row=9, column=2)
btn52 = tk.Button(frm2, text="btn", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn52.grid(row=10, column=2)
btn53 = tk.Button(frm2, text=" btn", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn53.grid(row=11, column=2)
btn54 = tk.Button(frm2, text="btn", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn54.grid(row=12, column=2)
btn55 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn55.grid(row=13, column=2)
btn56 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn56.grid(row=14, column=2)
btn57 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn57.grid(row=15, column=2)
btn58 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn58.grid(row=16, column=2)
btn59 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn59.grid(row=17, column=2)
btn60 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn60.grid(row=18, column=2)


############################################################################################################
############################################################################################################




btn108 = tk.Button(frm2, text="  8  ", bd=5, bg= 'azure', font=('URW Chancery L',8,'bold'), command=eight)
btn108.grid(row=6, column=3)
btn109 = tk.Button(frm2, text="  5  ", bd=5, bg= 'azure',  font=('URW Chancery L',8,'bold'), command=five)
btn109.grid(row=7, column=3)
btn909 = tk.Button(frm2, text="  2  ", bd=5, bg= 'azure',  font=('URW Chancery L',8,'bold'), command=two)
btn909.grid(row=8, column=3)
btn188 = tk.Button(frm2, text=" +/-  ", bd=5, bg= 'light green', font=('URW Chancery L',8,'bold'), command=signchr)
btn188.grid(row=9, column=3)
btn189 = tk.Button(frm2, text="  0   ", bd=5, bg= 'light blue', font=('URW Chancery L',8,'bold'), command=zero)
btn189.grid(row=10, column=3)

############################################################################################################
############################################################################################################

btn99 = tk.Button(frm2, text="Btn1", bd=5, bg= 'light blue', font=('URW Chancery L',8,'bold'), command=cmd)
btn99.grid(row=11, column=3)
btn100 = tk.Button(frm2, text="Btn1", bd=5, bg= 'light blue', font=('URW Chancery L',8,'bold'), command=cmd)
btn100.grid(row=12, column=3)
btn101 = tk.Button(frm2, text="Btn1", bd=5, bg= 'light blue', font=('URW Chancery L',8,'bold'), command=cmd)
btn101.grid(row=13, column=3)
btn102 = tk.Button(frm2, text="Btn1", bd=5, bg= 'light blue', font=('URW Chancery L',8,'bold'), command=cmd)
btn102.grid(row=14, column=3)
btn103 = tk.Button(frm2, text="Btn1", bd=5, bg= 'light blue', font=('URW Chancery L',8,'bold'), command=cmd)
btn103.grid(row=15, column=3)
btn104 = tk.Button(frm2, text="Btn1", bd=5, bg= 'light blue', font=('URW Chancery L',8,'bold'), command=cmd)
btn104.grid(row=16, column=3)
btn105 = tk.Button(frm2, text="Btn1", bd=5, bg= 'light blue', font=('URW Chancery L',8,'bold'), command=cmd)
btn105.grid(row=17, column=3)
btn106 = tk.Button(frm2, text="Btn1", bd=5, bg= 'light blue', font=('URW Chancery L',8,'bold'), command=cmd)
btn106.grid(row=18, column=3)


############################################################################################################
############################################################################################################



btn160 = tk.Button(frm2, text="  9  ", bd=5, bg= 'azure',font=('URW Chancery L',8,'bold'), command=nine)
btn160.grid(row=6, column=4)
btn161 = tk.Button(frm2, text="   6  ", bd=5, bg= 'azure', font=('URW Chancery L',8,'bold'), command=six)
btn161.grid(row=7, column=4)
btn1777 = tk.Button(frm2, text="  3  ", bd=5, bg= 'azure',font=('URW Chancery L',8,'bold'), command=three)
btn1777.grid(row=8, column=4)
btn147 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn147.grid(row=9, column=4)
btn150 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn150.grid(row=10, column=4)
btn151 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn151.grid(row=11, column=4)
btn152 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn152.grid(row=12, column=4)
btn153 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn153.grid(row=13, column=4)
btn154 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn154.grid(row=14, column=4)
btn155 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn155.grid(row=15, column=4)
btn156= tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn156.grid(row=16, column=4)
btn157 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn157.grid(row=17, column=4)
btn158= tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn158.grid(row=18, column=4)

############################################################################################################
############################################################################################################


######################################################
btn167 = tk.Button(frm2, text="Btn1", bd=5, bg= 'cyan', font=('URW Chancery L',8,'bold'), command=cmd)
btn167.grid(row=5, column=5)
btn200 = tk.Button(frm2, text="  /  ", bd=5, bg= 'cornsilk', font=('URW Chancery L',8,'bold'), command=div)
btn200.grid(row=6, column=5)
btn1499 = tk.Button(frm2, text=" X ", bd=5, bg= 'lavender',  font=('URW Chancery L',8,'bold'), command=mul)
btn1499.grid(row=7, column=5)
btn109 = tk.Button(frm2, text="  -  ", bd=5, bg= 'LightPink1', font=('URW Chancery L',8,'bold'), command=subtract)
btn109.grid(row=8, column=5)
btn140 = tk.Button(frm2, text="  +  ", bd=5, bg= 'light blue', font=('URW Chancery L',8,'bold'), command=add)
btn140.grid(row=9, column=5)
############################################################################################################
############################################################################################################


btn172 = tk.Button(frm2, text="Btn1", bd=5, bg= 'cyan', font=('URW Chancery L',8,'bold'), command=cmd)
btn172.grid(row=10, column=5)                                                                                       

btn192 = tk.Button(frm2, text="Btn1", bd=5, bg= 'cyan', font=('URW Chancery L',8,'bold'), command=cmd)
btn192.grid(row=11, column=5)
btn193 = tk.Button(frm2, text="Btn1", bd=5, bg= 'cyan', font=('URW Chancery L',8,'bold'), command=cmd)
btn193.grid(row=12, column=5)
btn194 = tk.Button(frm2, text="Btn1", bd=5, bg= 'cyan', font=('URW Chancery L',8,'bold'), command=cmd)
btn194.grid(row=13, column=5)
btn195 = tk.Button(frm2, text="Btn1", bd=5, bg= 'cyan', font=('URW Chancery L',8,'bold'), command=cmd)
btn195.grid(row=14, column=5)
btn196 = tk.Button(frm2, text="Btn1", bd=5, bg= 'cyan', font=('URW Chancery L',8,'bold'), command=cmd)
btn196.grid(row=15, column=5)
btn197 = tk.Button(frm2, text="Btn1", bd=5, bg= 'cyan', font=('URW Chancery L',8,'bold'), command=cmd)
btn197.grid(row=16, column=5)
btn198 = tk.Button(frm2, text="Btn1", bd=5, bg= 'cyan', font=('URW Chancery L',8,'bold'), command=cmd)
btn198.grid(row=17, column=5)
btn199 = tk.Button(frm2, text="Btn1", bd=5, bg= 'cyan', font=('URW Chancery L',8,'bold'), command=cmd)
btn199.grid(row=18, column=5)                                                                                      


############################################################################################################
############################################################################################################

btn173 = tk.Button(frm2, text="SIN", bd=5, bg= 'pink', font=('URW Chancery L',8,'bold'), command=sin)
btn173.grid(row=5, column=6)
btn174 = tk.Button(frm2, text="COS", bd=5, bg= 'light blue', font=('URW Chancery L',8,'bold'), command=cos)
btn174.grid(row=6, column=6)
btn175 = tk.Button(frm2, text="TAN", bd=5, bg= 'light yellow', font=('URW Chancery L',8,'bold'), command=tan)
btn175.grid(row=7, column=6)
btn176 = tk.Button(frm2, text="ASIN", bd=5, bg= 'light green', font=('URW Chancery L',8,'bold'), command=asin)
btn176.grid(row=8, column=6)
btn177 = tk.Button(frm2, text="ACOS", bd=5, bg= 'pink', font=('URW Chancery L',8,'bold'), command=acos)
btn177.grid(row=9, column=6)
btn178 = tk.Button(frm2, text="ATAN", bd=5, bg= 'cyan', font=('URW Chancery L',8,'bold'), command=atan)
btn178.grid(row=10, column=6)
btn179 = tk.Button(frm2, text="SINH", bd=5, bg= 'violet', font=('URW Chancery L',8,'bold'), command=sinh)
btn179.grid(row=11, column=6)
btn180 = tk.Button(frm2, text="COSH", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cosh)
btn180.grid(row=12, column=6)
btn181 = tk.Button(frm2, text="TANH", bd=5, bg= 'lavender', font=('URW Chancery L',8,'bold'), command=tanh)
btn181.grid(row=13, column=6)
btn182 = tk.Button(frm2, text="ASINH", bd=5, bg= 'seashell', font=('URW Chancery L',8,'bold'), command=asinh)
btn182.grid(row=14, column=6)
btn183 = tk.Button(frm2, text="ACOSH", bd=5, bg= 'seagreen', font=('URW Chancery L',8,'bold'), command=acosh)
btn183.grid(row=15, column=6)
btn184 = tk.Button(frm2, text="ATANH", bd=5, bg= 'cornsilk', font=('URW Chancery L',8,'bold'), command=atanh)
btn184.grid(row=16, column=6)
btn185= tk.Button(frm2, text="HYP", bd=5, bg= 'linen', font=('URW Chancery L',8,'bold'), command=hyp)
btn185.grid(row=17, column=6)
btn186 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn186.grid(row=18, column=6)

###########################################################################################################
############################################################################################################


btn110 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn110.grid(row=5, column=7)
btn111 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn111.grid(row=6, column=7)
btn112 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn112.grid(row=7, column=7)
btn113 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn113.grid(row=8, column=7)
btn114 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn114.grid(row=9, column=7)
btn115 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn115.grid(row=10, column=7)
btn116= tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn116.grid(row=11, column=7)
btn117 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn117.grid(row=12, column=7)
btn118 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn118.grid(row=13, column=7)
btn119 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn119.grid(row=14, column=7)
btn120 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn120.grid(row=15, column=7)

btn121 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn121.grid(row=16, column=7)
btn122 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn122.grid(row=17, column=7)
btn123 = tk.Button(frm2, text="Btn1", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
btn123.grid(row=18, column=7)
############################################################################################################
############################################################################################################


gg243 = tk.Button(frm2, text="CLR ALL", bd=5, bg= '#cbcdd8', font=('URW Chancery L',8,'bold'), command=clearall)
gg243.grid(row=5, column=8)
gg244 = tk.Button(frm2, text="CE1", bd=5, bg= '#cbcdd8', font=('URW Chancery L',8,'bold'), command=clear1)
gg244.grid(row=6, column=8)
gg245 = tk.Button(frm2, text="CE2", bd=5, bg= '#cbcdd8', font=('URW Chancery L',8,'bold'), command=clear2)
gg245.grid(row=7, column=8)
gg246 = tk.Button(frm2, text="CE3", bd=5, bg= '#cbcdd8', font=('URW Chancery L',8,'bold'), command=clear3)
gg246.grid(row=8, column=8)
gg247 = tk.Button(frm2, text="CE4", bd=5, bg= '#cbcdd8', font=('URW Chancery L',8,'bold'), command=clear4)
gg247.grid(row=9, column=8)
gg250 = tk.Button(frm2, text="CLR ANS", bd=5, bg= 'DarkOrchid1', font=('URW Chancery L',8,'bold'), command=clear6)
gg250.grid(row=10, column=8)
gg251 = tk.Button(frm2, text="CLR MEM", bd=5, bg= 'DeepSkyBlue2', font=('URW Chancery L',8,'bold'), command=clrmem)
gg251.grid(row=11, column=8)
gg252 = tk.Button(frm2, text="MEM ENTRY", bd=5, bg='LightGoldenrod1', font=('URW Chancery L',8,'bold'), command=sto1)
gg252.grid(row=12, column=8)
gg253 = tk.Button(frm2, text="MEM ANS", bd=5, bg= 'light yellow', font=('URW Chancery L',8,'bold'), command=stoans)
gg253.grid(row=13, column=8)
gg254 = tk.Button(frm2, text="RECALL", bd=5, bg= 'ivory2', font=('URW Chancery L',8,'bold'), command=recall_mem)
gg254.grid(row=14, column=8)
gg255 = tk.Button(frm2, text="Shift1-2", bd=5, bg= 'ivory3', font=('URW Chancery L',8,'bold'), command=shift1)
gg255.grid(row=15, column=8)
gg256= tk.Button(frm2, text="Shift2-3", bd=5, bg= 'pink', font=('URW Chancery L',8,'bold'), command=shift2)
gg256.grid(row=16, column=8)
gg257 = tk.Button(frm2, text="Shift3-4", bd=5, bg= 'yellow', font=('URW Chancery L',8,'bold'), command=shift3)
gg257.grid(row=17, column=8)
gg258= tk.Button(frm2, text="Shift4-Mem", bd=5, bg= 'violet', font=('URW Chancery L',8,'bold'), command=shift4)
gg258.grid(row=18, column=8)






if __name__=='__main__':
    root.mainloop()
    


    
           





