import tkinter as tk
from tkinter import ttk, Frame, filedialog, font, Toplevel 
from tkinter import *
import math
from math import *


root = tk.Tk()

root.title("JH Scientific Calculator Ver3")


root.geometry('1000x1900')


answer_ee2 = 0
cc_complete = 0

frm1 = ttk.Frame(root, height=20, width=200)
frm1.grid(row=0, column=1, columnspan=2)
frm1.columnconfigure(0, weight=4)
frm1.columnconfigure(1, weight=5)
frm2 = ttk.Frame(root, height=300, width=600)
frm2.grid(row=5, column=0, columnspan=2)


frm3 = ttk.Frame(root, height=100, width=600)
frm3.grid(row=25, column=0, columnspan=2)


lb = tk.Listbox(frm3)
lb.grid(row=27, column=0)
frm3.columnconfigure(0, weight=8)
frm3.columnconfigure(1, weight=6)


tk.Label(frm1, text="Entry 1").grid(row=0, column=0)
tk.Label(frm1, text="Entry 2").grid(row=0, column=1)
tk.Label(frm1, text="Entry 3").grid(row=0, column=2)
tk.Label(frm1, text="Entry 4").grid(row=0, column=3)
tk.Label(frm1, text="Answer from Entry 3&4").grid(row=2, column=3)
tk.Label(frm1, text="Answer from Answer 1&2").grid(row=2, column=5)



e1 = tk.Entry(frm1, bd=5, bg= "wheat")
e1.grid(row=1, column=0, padx=20, sticky="w")
e2 = tk.Entry(frm1, bd=5, bg= "light blue")
e2.grid(row=1, column=1, padx=20, sticky="w")
e3 = tk.Entry(frm1, bd=5, bg= "light green")
e3.grid(row=1, column=2, padx=20, sticky="w")
e4 = tk.Entry(frm1, bd=5, bg= "light pink")
e4.grid(row=1, column=3, padx=20, sticky="w")

e5 = tk.Entry(frm1, bd=5, bg= "light pink")
e5.grid(row=3, column=3, padx=20, sticky="w")
tk.Label(frm1, text="Answer from Entry 1&2").grid(row=2, column=1)
e6 = Entry(frm1, bd=5, bg= "wheat")
e6.grid(row=3, column=1)
e7 = tk.Entry(frm1, bd=5, bg= "light pink")
e7.grid(row=3, column=5, padx=20, sticky="w")
##tk.Label(frm1, text="                ").grid(row=2, column=0)
##tk.Label(frm1, text="                ").grid(row=3, column=1)
##tk.Label(frm1, text="                ").grid(row=2, column=2)
##tk.Label(frm1, text="                ").grid(row=3, column=2)
##tk.Label(frm1, text="                ").grid(row=2, column=3)
##tk.Label(frm1, text="                ").grid(row=3, column=3)
def add():
    if not len(e4.get()) == 0:
        ee4 = float(e4.get())
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        ee3 = float(e3.get())
        ee5 = float(ee4) - float(ee3)
        e5.insert(END, float(ee5))
        e3.delete(0, END)
    #if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        #e2.delete(0, END)
        
        
    
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
        
        return  e6.insert(END, answer)
        


    eqbtn1 = tk.Button(frm1, text='  =  ', bd=5, bg= 'AntiqueWhite2', font=('URW Chancery L',8,'bold'), command=eq)
    eqbtn1.grid(row=3, column=0)



def subtract():
    if not len(e4.get()) == 0:
        ee4 = float(e4.get())
        lb.insert(1, e4.get())
        e4.delete(0, END)
    if not len(e3.get()) == 0:
        ee3 = float(e3.get())
        ee5 = float(ee4) - float(ee3)
        e5.insert(END, float(ee5))
        e3.delete(0, END)
        tk.Label(frm1, text="-----answer------").grid(row=4, column=3)

    #if not len(e2.get()) == 0:
        lb.insert(1, e2.get())
        #e2.delete(0, END)
        
    
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
        tk.Label(frm1, text="-----answer------").grid(row=4, column=1)
        return  e6.insert(END, answer)
        


    eqbtn1 = tk.Button(frm1, text='  =  ', bd=5, bg= 'AntiqueWhite2', font=('URW Chancery L',8,'bold'), command=eq)
    eqbtn1.grid(row=3, column=0)



def mul():
    if not len(e4.get()) == 0:
        if not len(e3.get()) == 0:
            ee4 = float(e4.get())
            lb.insert(1, e4.get())
            e4.delete(0, END)
    
            ee3 = float(e3.get())
            ee5 = float(ee4) * float(ee3)
            e5.insert(END, float(ee5))
            tk.Label(frm1, text="-----answer------").grid(row=4, column=3)
            
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
            if not len(e5.get()) == 0:
                       ee5 = float(e5.get())
                       ee6 = float(e6.get())
                       ee7 = float(ee6) * float(ee5)
                       e7.insert(END, ee7)
                                          
        else:    
            e6.delete(0, END)
            ee1 = float(e1.get())
            ee2 = float(e2.get())
            answer = float(ee2) * float(ee1)
            tk.Label(frm1, text="-----answer------").grid(row=4, column=1)
            return  e6.insert(END, answer)
        
        
    eqbtn1 = tk.Button(frm1, text='  =  ', bd=5, bg='AntiqueWhite2', font=('URW Chancery L',15,'bold'), command=eq)
    eqbtn1.grid(row=3, column=0)
def div():
    if not len(e4.get()) == 0:
        if not len(e3.get()) == 0:
            ee4 = float(e4.get())
            lb.insert(1, e4.get())
            e4.delete(0, END)
            ee3 = float(e3.get())
            if ee3 == 0:
                e5.insert(0, "undefined")
                tk.Label(frm1, text="   ----no answer----  ").grid(row=4, column=1)
            else:    
                ee5 = float(ee4) / float(ee3)
                e5.insert(END, float(ee5))
                tk.Label(frm1, text="   ----answer----  ").grid(row=4, column=1)
                e3.delete(0, END)
    
    if not len(e2.get()) == 0:
        e3.insert(END, float(e2.get()))
        e2.delete(0, END)
    if not len(e1.get()) == 0:    
        ee1 = float(e1.get())
        e2.insert(END, float(ee1))
        ee2 = float(e2.get())
        e1.delete(0, END)
   
    
    def eq():
        if not len(e6.get()) == 0:
            if not len(e5.get()) == 0:
                       ee5 = float(e5.get())
                       ee6 = float(e6.get())
                       if ee5 == 0:
                           e7.insert(END, "Undefined")
                       else:
                           
                           ee7 = float(ee6) / float(ee5)
                           e7.insert(END, float(ee7))
                                          
        elif not len(e1.get()) == 0:    
            e6.delete(0, END)
            ee1 = float(e1.get())
            ee2 = float(e2.get())
          
       
        if ee1 == 0:
            e6.insert(END, "Undefined")
            tk.Label(frm1, text="-Infinite-").grid(row=4, column=1)
            tk.Label(frm1, text="---Value--").grid(row=5, column=1)
        else:    
            
            ans = float(ee2) / float(ee1)
            tk.Label(frm1, text="-----answer------").grid(row=4, column=1)
            
            return  e6.insert(END, float(ans))
    
        

    eqbtn1 = tk.Button(frm1, text='  =  ', bd=5, bg= 'AntiqueWhite3', font=('URW Chancery L',15,'bold'), command=eq)
    eqbtn1.grid(row=3, column=0)



    
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
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    tk.Label(frm1, text="                           ").grid(row=2, column=0)
    tk.Label(frm1, text="                           ").grid(row=4, column=1)
    tk.Label(frm1, text="                           ").grid(row=4, column=3)
    tk.Label(frm1, text="                           ").grid(row=5, column=1)
    tk.Label(frm1, text="                           ").grid(row=5, column=3)
    tk.Label(frm1, text="                           ").grid(row=5, column=5)
    tk.Label(frm1, text="                           ").grid(row=4, column=5)

def clear1():
    e1.delete(0, END)
    tk.Label(frm1, text="                           ").grid(row=4, column=1)
    tk.Label(frm1, text="                        ").grid(row=5, column=1)



def clear2():
    e2.delete(0, END)
    tk.Label(frm1, text="                           ").grid(row=4, column=1)
    tk.Label(frm1, text="                           ").grid(row=4, column=1)
    tk.Label(frm1, text="                           ").grid(row=4, column=3)
    tk.Label(frm1, text="                           ").grid(row=5, column=1)
    tk.Label(frm1, text="                           ").grid(row=5, column=3)
    tk.Label(frm1, text="                           ").grid(row=5, column=5)
    tk.Label(frm1, text="                           ").grid(row=4, column=5)




def clear3():
    e3.delete(0, END)
    tk.Label(frm1, text="                           ").grid(row=4, column=1)


     
def clear4():
    e4.delete(0, END)
    tk.Label(frm1, text="                           ").grid(row=4, column=1)



def clear6():
    e6.delete(0, END)
    tk.Label(frm1, text="                           ").grid(row=4, column=1)
    tk.Label(frm1, text="                           ").grid(row=4, column=3)
    tk.Label(frm1, text="                           ").grid(row=5, column=1)
    tk.Label(frm1, text="                           ").grid(row=5, column=3)
    tk.Label(frm1, text="                           ").grid(row=5, column=5)
    tk.Label(frm1, text="                           ").grid(row=4, column=5)

    
     
   

def clrmem():
    lb.delete(0, END)
    tk.Label(frm1, text="                           ").grid(row=4, column=1)
    tk.Label(frm1, text="                           ").grid(row=4, column=3)
    tk.Label(frm1, text="                           ").grid(row=5, column=1)
    tk.Label(frm1, text="                           ").grid(row=5, column=3)
    tk.Label(frm1, text="                           ").grid(row=5, column=5)
    tk.Label(frm1, text="                           ").grid(row=4, column=5)


def recall_mem(event=None):
    try:
        mc = lb.curselection()[0]
        ee5 = lb.get(mc)
        e1.insert(END, ee5)
    except Exception as ex:
        tk.Label(frm1, text="nothing selected").grid(row=4, column=1)
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

def to_mem():
    ee1 = e1.get()
    lb.insert(END, ee1)
    



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


def shift_ans1():
    ee6 = float(e6.get())
    top2 = Toplevel()

    def to_ent3():
        e3.delete(0, END)
        e3.insert(END, float(ee6))
        e6.delete(0, END)
    def to_ent4():
        e4.delete(0, END)
        e4.insert(END, float(ee6))
        e6.delete(0, END)

    def to_ent5():
        e5.delete(0, END)
        e5.insert(END, float(ee6))
        e6.delete(0, END)
    def to_ent7():
        e7.insert(END, float(ee6))
        e6.delete(0, END)

    def to_ent1():
        e1.delete(0, END)
        e1.insert(END, float(ee6))
        e6.delete(0, END)
    def to_ent2():
        e2.delete(0, END)
        e2.insert(END, float(ee6))
        e6.delete(0, END)     

    btn1= tk.Button(top2, text="move answser to entry 3", command=to_ent3)
    btn1.grid(row=0, column=0)
    btn2= tk.Button(top2, text="move answser to entry 4", command=to_ent4)
    btn2.grid(row=1, column=0)
    btn3= tk.Button(top2, text="move answser to entry 5", command=to_ent5)
    btn3.grid(row=2, column=0)
    btn4= tk.Button(top2, text="move answser to entry 7", command=to_ent7)
    btn4.grid(row=3, column=0)
    btn5= tk.Button(top2, text="move answser to entry 1", command=to_ent1)
    btn5.grid(row=4, column=0)
    btn6= tk.Button(top2, text="move answser to entry 2", command=to_ent2)
    btn6.grid(row=5, column=0)
    
def shift_mem():
    top3 = Toplevel()
    def to_e1(event=None):
        try:
            mc = lb.curselection()[0]
            ee1 = lb.get(mc)
            e1.delete(0, END)
            e1.insert(END, ee1)
        except Exception as ex:
            tk.Label(frm1, text="nothing selected").grid(row=4, column=1)
            print(ex)

    def to_e2(event=None):
        try:
            mc = lb.curselection()[0]
            ee1 = lb.get(mc)
            e2.delete(0, END)
            e2.insert(END, ee1)
        except Exception as ex:
            tk.Label(frm1, text="nothing selected").grid(row=4, column=1)
            print(ex)    
    def to_e3(event=None):
        try:
            mc = lb.curselection()[0]
            ee1 = lb.get(mc)
            e3.delete(0, END)
            e3.insert(END, ee1)
        except Exception as ex:
            tk.Label(frm1, text="nothing selected").grid(row=4, column=1)
            print(ex)
            
    def to_e4(event=None):
        try:
            mc = lb.curselection()[0]
            ee1 = lb.get(mc)
            e4.delete(0, END)
            e4.insert(END, ee1)
        except Exception as ex:
            tk.Label(frm1, text="nothing selected").grid(row=4, column=1)
            print(ex)            


   


    btn1= tk.Button(top3, text="memory selection to entry 1", command=to_e1)
    btn1.grid(row=0, column=0)
    btn2= tk.Button(top3, text="memory selection to entry 2", command=to_e2)
    btn2.grid(row=1, column=0)
    btn3= tk.Button(top3, text="memory selection to entry 3", command=to_e3)
    btn3.grid(row=2, column=0)
    btn4= tk.Button(top3, text="memory selection to entry 4", command=to_e4)
    btn4.grid(row=3, column=0)
   
    
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
         
         return  e6.insert(END, answer)
    eqbtn1 = tk.Button(frm1, text='  =  ', bd=5, bg='ivory2', font=('URW Chancery L',15,'bold'), command=eq)
    eqbtn1.grid(row=3, column=0)       
    
    


    eqbtn1 = tk.Button(frm1, text='  =  ', bd=5, bg= 'AntiqueWhite3', font=('URW Chancery L',15,'bold'), command=eq)
    eqbtn1.grid(row=3, column=0)
    



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
     
    return answer

def point():
    if not len(e1.get()) == 0:
        ee1 = float(e1.get())
        e1.delete(0, END)
        e1.insert(END, float(ee1))
    else:
         tk.Label(frm1, text="Enter number first").grid(row=2, column=0)
    


def pow2():
    if not len(e1.get()) == 0:
        ee1 = float(e1.get()) ** 2
        e1.delete(0, END)
        e1.insert(END, float(ee1))
    else:
         tk.Label(frm1, text="Enter number first").grid(row=2, column=0)
    



def pow3():
    if not len(e1.get()) == 0:
        ee1 = float(e1.get()) ** 3 
        e1.delete(0, END)
        e1.insert(END, float(ee1))
    else:
         tk.Label(frm1, text="Enter number first").grid(row=2, column=0)
    


def pow4():
    if not len(e1.get()) == 0:
        ee1 = float(e1.get()) ** 4
        e1.delete(0, END)
        e1.insert(END, float(ee1))
    else:
         tk.Label(frm1, text="Enter number first").grid(row=2, column=0)
    


def powpow():
    if not len(e1.get()) == 0:
        ee1 = float(e1.get()) ** float(e1.get())
        e1.delete(0, END)
        e1.insert(END, float(ee1))
    else:
         tk.Label(frm1, text="Enter number first").grid(row=2, column=0)
    


def powpow3():
    if not len(e1.get()) == 0:
        if float(e1.get()) >= 5:
            e1.insert(END, 'too big>=5')
        else:              
            ee1 = float(e1.get()) ** float(e1.get()) ** float(e1.get())
            e1.delete(0, END)
            e1.insert(END, float(ee1))
    else:
         tk.Label(frm1, text="Enter number first").grid(row=2, column=0)
    

def sq_rt():
    if not len(e1.get()) == 0:
        ee1 = float(e1.get()) ** 0.5
        e1.delete(0, END)
        e1.insert(END, float(ee1))
    else:
         tk.Label(frm1, text="Enter number first").grid(row=2, column=0)
    
def cu_rt():
    if not len(e1.get()) == 0:
        ee1 = float(e1.get()) ** 0.3
        e1.delete(0, END)
        e1.insert(END, float(ee1))
    else:
         tk.Label(frm1, text="Enter number first").grid(row=2, column=0)

def pow_qt():
    if not len(e1.get()) == 0:
        ee1 = float(e1.get()) ** 0.25
        e1.delete(0, END)
        e1.insert(END, float(ee1))
    else:
         tk.Label(frm1, text="Enter number first").grid(row=2, column=0)



def inv2():
    if not len(e1.get()) == 0:
        if e1.get() == 0:
            e1.insert(END, 'not 0')
        else:
            ee1 = 1 / float(e1.get())
            e1.delete(0, END)
            e1.insert(END, float(ee1))
    else:
         tk.Label(frm1, text="Enter number first").grid(row=2, column=0)
    


         
    
def any_rt():
    tk.Label(frm1, text="base then root").grid(row=2, column=0)
    if not len(e4.get()) == 0:
        if not len(e3.get()) == 0:
            ee4 = float(e4.get())
            lb.insert(1, e4.get())
            e4.delete(0, END)
            ee3 = float(e3.get())
            if ee3 == 0:
                e5.insert(0, "undefined")
                tk.Label(frm1, text="   ----no answer----  ").grid(row=4, column=1)
            else:    
                ee5 = float(ee4) / float(ee3)
                e5.insert(END, float(ee5))
                tk.Label(frm1, text="   ----answer----  ").grid(row=4, column=1)
                e3.delete(0, END)
    
    if not len(e2.get()) == 0:
        e3.insert(END, float(e2.get()))
        e2.delete(0, END)
    if not len(e1.get()) == 0:    
        ee1 = float(e1.get())
        e2.insert(END, float(ee1))
        ee2 = float(e2.get())
        e1.delete(0, END)
   
    
    def eq():
        if not len(e6.get()) == 0:
            if not len(e5.get()) == 0:
                       ee5 = float(e5.get())
                       ee6 = float(e6.get())
                       if ee5 == 0:
                           e7.insert(END, "Undefined")
                       else:
                           rt5 = 1 / float(ee5)
                           
                           ee7 = float(ee6) ** float(rt5)
                           e7.insert(END, float(ee7))
                                          
        elif not len(e1.get()) == 0:    
            e6.delete(0, END)
            ee1 = float(e1.get())
            ee2 = float(e2.get())
          
       
        if ee1 == 0:
            e6.insert(END, "Undefined")
            tk.Label(frm1, text="----------Infinite-----------").grid(row=4, column=1)
            tk.Label(frm1, text="---Value--").grid(row=5, column=1)
        else:    
            rt1 = 1 / ee1
            ans = float(ee2) ** float(rt1)
            tk.Label(frm1, text="----------------answer-------------------").grid(row=4, column=1)
            
            return  e6.insert(END, float(ans))
    
        

    eqbtn1 = tk.Button(frm1, text='  =  ', bd=5, bg= 'AntiqueWhite3', font=('URW Chancery L',15,'bold'), command=eq)
    eqbtn1.grid(row=3, column=0)
    


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
        
        return

        

    eqbtn1 = tk.Button(frm1, text='  =  ', bd=5, bg= 'cornsilk', font=('URW Chancery L',15,'bold'), command=eq)
    eqbtn1.grid(row=3, column=0)

   

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
          
         return
    eqbtn1 = tk.Button(frm1, text='  =  ', bd=5, bg= 'lavender', font=('URW Chancery L',15,'bold'), command=eq)
    eqbtn1.grid(row=3, column=0)




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
    
    return


              
              
def signchr():
    if not len(e4.get()) == 0:
        ee4 = float(e4.get0() * -1)
        #e4.delete(0, END)
    if not len(e3.get()) == 0:
        e3.insert(END, float(e3.get() * -1))
        #e3.delete(0, END)
    if not len(e2.get()) == 0:
                  ee2 = e2.get() * -1
                  ee2.insert(0, float(ee2))
                  
       
    ee1 = float(e1.get() * -1)    
    e2.insert(END, float(ee1))
    #e1.delete(0, END)
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
        
        return
    
    eqbtn1 = tk.Button(frm1, text='  =  ', bd=5, bg='azure', font=('URW Chancery L',15,'bold'), command=eq)
    eqbtn1.grid(row=3, column=0)



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



def eq1():

    
    def solver(a,b,c):
        """ Solves quadratic equation and returns the result in formatted string """
        D = b*b - 4*a*c
        if D >= 0:
            x1 = (-b + math.sqrt(D)) / (2*a)
            x2 = (-b - math.sqrt(D)) / (2*a)
            text = "The discriminant is: %s \n X1 is: %s \n X2 is: %s \n" % (D, x1, x2)        
        else:
            text = "The discriminant is: %s \n This equation has no solutions" % D 
        return text

    def inserter(value):
        """ Inserts specified value into text widget """
        output.delete("0.0","end")
        output.insert("0.0",value)    

    def clear(event):
        """ Clears entry form """
        caller = event.widget
        caller.delete("0", "end")

    def handler():
        """ Get the content of entries and passes result to the text """
        try:
            # make sure that we entered correct values
            a_val = float(a.get())
            b_val = float(b.get())
            c_val = float(c.get())
            inserter(solver(a_val, b_val, c_val))
        except ValueError:
            inserter("Make sure you entered 3 numbers")

    top = Toplevel()
    top.title("Quadratic calculator")
    top.minsize(325,230)
    top.resizable(width=False, height=False)


    frame = Frame(top)
    frame.grid()

    a = Entry(frame, width=3)
    a.grid(row=1,column=1,padx=(10,0))
    a.bind("<FocusIn>", clear)
    a_lab = Label(frame, text="x**2+").grid(row=1,column=2)

    b = Entry(frame, width=3)
    b.bind("<FocusIn>", clear)
    b.grid(row=1,column=3)
    b_lab = Label(frame, text="x+").grid(row=1, column=4)

    c = Entry(frame, width=3)
    c.bind("<FocusIn>", clear)
    c.grid(row=1, column=5)
    c_lab = Label(frame, text="= 0").grid(row=1, column=6)

    but = Button(frame, text="Solve", command=handler).grid(row=1, column=7, padx=(10,0))

    output = Text(frame, bg="lightblue", font="Arial 12", width=35, height=10)
    output.grid(row=2, columnspan=8)








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
btn9 = tk.Button(frm2, text="1/X INV", bd=5, bg= 'wheat', font=('URW Chancery L',8,'bold'), command=inv2)
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

btn51 = tk.Button(frm2, text="^2", bd=5, bg= 'lawn green', font=('URW Chancery L',8,'bold'), command=pow2)
btn51.grid(row=9, column=2)
btn52 = tk.Button(frm2, text="^3", bd=5, bg= 'light blue', font=('URW Chancery L',8,'bold'), command=pow3)
btn52.grid(row=10, column=2)
btn53 = tk.Button(frm2, text="^4", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=pow4)
btn53.grid(row=11, column=2)
btn54 = tk.Button(frm2, text="pow^pow", bd=5, bg= 'cyan', font=('URW Chancery L',8,'bold'), command=powpow)
btn54.grid(row=12, column=2)
btn55 = tk.Button(frm2, text="^pow^pow", bd=5, bg= 'violet', font=('URW Chancery L',8,'bold'), command=powpow3)
btn55.grid(row=13, column=2)
btn56 = tk.Button(frm2, text="sqrt2", bd=5, bg= 'light yellow', font=('URW Chancery L',8,'bold'), command=sq_rt)
btn56.grid(row=14, column=2)
btn57 = tk.Button(frm2, text="cube rt", bd=5, bg= 'wheat', font=('URW Chancery L',8,'bold'), command=cu_rt)
btn57.grid(row=15, column=2)
btn58 = tk.Button(frm2, text="4th rt", bd=5, bg= 'light green', font=('URW Chancery L',8,'bold'), command=pow_qt)
btn58.grid(row=16, column=2)
btn59 = tk.Button(frm2, text="y ^ 1/x", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=any_rt)
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
btn188.grid(row=10, column=3)
btn189 = tk.Button(frm2, text="  0   ", bd=5, bg= 'light blue', font=('URW Chancery L',8,'bold'), command=zero)
btn189.grid(row=9, column=3)

############################################################################################################
############################################################################################################

btn99 = tk.Button(frm2, text="Quadratic", bd=5, bg= 'light blue', font=('URW Chancery L',8,'bold'), command=eq1)
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
btn147 = tk.Button(frm2, text="1/x ans", bd=5, bg= 'cornsilk', font=('URW Chancery L',8,'bold'), command=inv)
btn147.grid(row=9, column=4)
btn150 = tk.Button(frm2, text="Shift Ans", bd=5, bg= 'violet', font=('URW Chancery L',8,'bold'), command=shift_ans1)
btn150.grid(row=10, column=4)
btn151 = tk.Button(frm2, text="Mem move to", bd=5, bg= 'pink', font=('URW Chancery L',8,'bold'), command=shift_mem)
btn151.grid(row=11, column=4)
btn152 = tk.Button(frm2, text="Entry1 to Mem", bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=to_mem)
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
btn167 = tk.Button(frm2, text=".", bd=5, bg= 'cyan', font=('URW Chancery L',8,'bold'), command=point)
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
    


    
           





