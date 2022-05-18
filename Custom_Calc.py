import tkinter as tk
from tkinter import ttk, Entry, END
from math import *

root = tk.Tk()
root.title("Custom calculations")
root.geometry("10000x700")

##tk.Label(root, text="-").grid(row=0, column=0)
##tk.Label(root, text="_").grid(row=1, column=0)





def main():


    def op1(event):
        try:
        
            num14 = 1
            num1 = float(e1.get())
            num4 = float(e4.get())
            if cb1.get() == '+' :
                num14 = float(num1) + float(num4)
            elif cb1.get() == '-':
                num14 = float(num1) - float(num4)    
            elif cb1.get() == '*' :
                num14 = float(num1) * float(num4)

            elif cb1.get() == '/':
                if float(num4) == 0:
                    e4.insert(END, "undefined")
                else:    
                    num14 = float(num1) / float(num4)    
            elif cb1.get() == '^' :
                num14 = float(num1) ** float(num4)


            elif cb1.get() == 'root':
                 
                if float(num4) == 0:
                    e4.insert(END, "undefined")
                else:
                    inv4 = 1 / float(num4)
                    num14 = float(num1) ** float(inv4)    
            elif cb1.get() == ' ':
                pass        
            print(num1, num4, num14)
            e7.insert(END, num14)
            return float(num14)
        except Exception as ex:
            print(ex)


    def op2(event):
        try:
            num25 = 1
            num2 = float(e2.get())
            num5 = float(e5.get())
            
            
            
            if cb2.get() == '+' :     
                num25 = float(num2) + float(num5)
            
           
            elif cb2.get() == '-' :    
                num25 = float(num2) - float(num5)
           
            elif cb2.get() == '*' :
                num25 = float(num2) * float(num5)

            elif cb2.get() == '/':
                if float(num5) == 0:
                    e4.insert(END, "undefined")
                else:    
                    num25 = float(num2) / float(num5)    
            elif cb2.get() == '^' :
                num25 = float(num2) ** float(num5)


            elif cb2.get() == 'root':
               
                if float(num5) == 0:
                    e5.insert(END, "undefined")
                else:
                    inv5 = 1 / float(num5)
                    num25 = float(num2) ** float(inv5)
                    
            elif cb2.get() == ' ':
                pass

            print(num2, num5, num25)
            e8.insert(END, num25)
            return float(num25)
        except Exception as ex:
            print(ex)

    def op3(event):
        try:
            num36 = 1
            num3 = float(e3.get())
            num6 = float(e6.get())
           
        
            if cb3.get() == '+' :
                num36 = float(num3) + float(num6)


            elif cb3.get() == '-' :
                 num36 = float(num3) - float(num6)
                 
            elif cb3.get() == '*' :
                 num36 = float(num3) * float(num6)
            elif cb3.get() == '/':
                if float(num6) == 0:
                    e6.insert(END, "undefined")
                else:    
                    num36 = float(num3) / float(num6)    
            elif cb3.get() == '^' :
                num36 = float(num3) ** float(num6)


            elif cb3.get() == 'root':
                
                if float(num6) == 0:
                    e6.insert(END, "undefined")
                else:
                    inv6 = 1 / float(num6)
                    num36 = float(num3) ** float(inv6)  
           
            elif cb3.get() == ' ':
                pass

            print(num3, num6, num36)
            e9.insert(END, num36)
            return num36
        
        except Exception as ex:
            print(ex)
            
    def op4(event):
        try:
            num1425 = 1
            num14 = float(e7.get())
            num25 = float(e8.get())
           
        
            if cb_1425.get() == '+' :
                num1425 = float(num14) + float(num25)


            elif cb_1425.get() == '-' :
                 num1425 = float(num14) - float(num25)
                 
            elif cb_1425.get() == '*' :
                 num1425 = float(num14) * float(num25)
            elif cb_1425.get() == '/':
                if float(num25) == 0:
                    e11.insert(END, "undefined")
                else:    
                    num1425 = float(num14) / float(num25)    
            elif cb_1425.get() == '^' :
                num1425 = float(num14) ** float(num25)


            elif cb_1425.get() == 'root':
                
                if float(num25) == 0:
                    e11.insert(END, "undefined")
                else:
                    inv25 = 1 / float(num25)
                    num1425 = float(num14) ** float(inv25)  
           
            elif cb_1425.get() == ' ':
                pass

            print(num14, num25, num1425)
            e10.insert(END, num1425)
            return num1425
        
        except Exception as ex:
            print(ex)
               
    def op5(event):
        try:
            num2536 = 1
            num25 = float(e8.get())
            num36 = float(e9.get())
           
        
            if cb_2536.get() == '+' :
                num2536 = float(num25) + float(num36)


            elif cb_2536.get() == '-' :
                 num2536 = float(num25) - float(num36)
                 
            elif cb_2536.get() == '*' :
                 num2536 = float(num25) * float(num36)
            elif cb_2536.get() == '/':
                if float(num36) == 0:
                    e11.insert(END, "undefined")
                else:    
                    num2536 = float(num25) / float(num36)    
            elif cb_2536.get() == '^' :
                num2536 = float(num25) ** float(num36)


            elif cb_2536.get() == 'root':
                
                if float(num25) == 0:
                    e11.insert(END, "undefined")
                else:
                    inv36 = 1 / float(num36)
                    num2536 = float(num25) ** float(inv36)  
           
            elif cb_2536.get() == ' ':
                pass

            print(num25, num36, num2536)
            e11.insert(END, num2536)
            return num2536
        
        except Exception as ex:
            print(ex)

      


    def op6(event):
        try:
            final = 1
            ten = float(e10.get())
            eleven = float(e11.get())
           
        
            if cb_final.get() == '+' :
                final = float(ten) + float(eleven)


            elif cb_final.get() == '-' :
                 final = float(ten) - float(eleven)
                 
            elif cb_final.get() == '*' :
                 final = float(ten) * float(eleven)
            elif cb_final.get() == '/':
                if float(eleven) == 0:
                    e11.insert(END, "undefined")
                else:    
                    final = float(ten) / float(eleven)    
            elif cb_final.get() == '^' :
                final = float(ten) ** float(eleven)


            elif cb_final.get() == 'root':
                
                if float(eten) == 0:
                    e11.insert(END, "undefined")
                else:
                    inv11 = 1 / float(eleven)
                    final = float(ten) ** float(inv11)  
           
            elif cb_final.get() == ' ':
                pass

            print(ten, eleven, final)
            e12.insert(END, final)
            return final
        
        except Exception as ex:
            print(ex)
             
            
     
    def clr_all():
    
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        e7.delete(0, END)
        e8.delete(0, END)
        e9.delete(0, END)
        e10.delete(0, END)
        e11.delete(0, END)
        e12.delete(0, END)
        

    def clr_final():
         e12.delete(0, END)

    def clr_stage3():
        e10.delete(0, END)
        e11.delete(0, END)

    def clr_stage2():
        e7.delete(0, END)
        e8.delete(0, END)
        e9.delete(0, END)

    def clr_stage1():
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)


    
    operation = ['+', '-', '*', '/', '^','root',' ']
    tk.Label(root, text="Entry 1").grid(row=0, column=0)
    tk.Label(root, text="Stage 1 CUSTOM ENTRY CALCULATOR").grid(row=0, column=1)
    tk.Label(root, text="Entry 4").grid(row=0, column=3)
    tk.Label(root, text="_").grid(row=4, column=2)
    tk.Label(root, text="_").grid(row=0, column=5)
    tk.Label(root, text="_").grid(row=0, column=6)
    tk.Label(root, text="_").grid(row=0, column=7)
    tk.Label(root, text="_").grid(row=0, column=8)
    
   
    tk.Label(root, text="_").grid(row=1, column=2)
    
    
    tk.Label(root, text="_").grid(row=1, column=2)
    tk.Label(root, text="_").grid(row=3, column=2)
    tk.Label(root, text="_").grid(row=5, column=2)
    tk.Label(root, text="_").grid(row=3, column=2)
##################################################
    e1 = tk.Entry(root, bd=7, bg="seashell")
    e1.grid(row=2, column=0)
    e4 = tk.Entry(root, bd=7, bg="seashell")
    e4.grid(row=2, column=3)
#########################################################
    #cb_1425 = ttk.Combobox(root, values = operation)
    #cb_1425.grid(row=2, column=4)
    tk.Label(root, text="Entry 2").grid(row=3, column=0)
    tk.Label(root, text="Calc for Entry 1 & 4").grid(row=1, column=1)
    tk.Label(root, text="Calc for Entry 2 & 5").grid(row=3, column=1)
    tk.Label(root, text="Calc for Entry 3 & 6").grid(row=5, column=1)
    tk.Label(root, text="Entry 5").grid(row=3, column=3)
    tk.Label(root, text="Stage 1").grid(row=3, column=4)
    
################################################
    e2 = tk.Entry(root, bd=7, bg="seashell")
    e2.grid(row=4, column=0)
    e5 = tk.Entry(root, bd=7, bg="seashell")
    e5.grid(row=4, column=3)

#####################################################################    
        
    tk.Label(root, text="Entry 3").grid(row=5, column=0)
    
    tk.Label(root, text="Entry 6").grid(row=5, column=3)
          
    e3 = tk.Entry(root, bd=7, bg="seashell")
    e3.grid(row=6, column=0)
    e6 = tk.Entry(root, bd=7, bg="seashell")
    e6.grid(row=6, column=3)
###########################################################   
    #cb6 = ttk.Combobox(root, values = operation)
    #cb6.grid(row=6, column=4)
    
##############################################################

    cb1 = ttk.Combobox(root, values = operation)
    cb1.grid(row=2, column=1)
    
    cb2 = ttk.Combobox(root, values = operation)
    cb2.grid(row=4, column=1)

    cb3 = ttk.Combobox(root, values = operation)
    cb3.grid(row=6, column=1)
###################################################################
    tk.Label(root, text="ANS1").grid(row=10, column=0)
    tk.Label(root, text="ANS2").grid(row=10, column=4)
    tk.Label(root, text="ANS3").grid(row=10, column=7)
    tk.Label(root, text="From 1 & 4").grid(row=11, column=0)
    tk.Label(root, text="From 2 & 5").grid(row=11, column=4)
    tk.Label(root, text="From 3 & 6").grid(row=11, column=7)
    e7 = tk.Entry(root, bd=7, bg="seashell")
    e7.grid(row=12, column=0)
    cb_1425 = ttk.Combobox(root, values = operation)
    cb_1425.grid(row=12, column=1)

    e8 = tk.Entry(root, bd=7, bg="seashell")
    e8.grid(row=12, column=4)
    cb_2536 = ttk.Combobox(root, values = operation)
    cb_2536.grid(row=12, column=5)

    e9 = tk.Entry(root, bd=7, bg="seashell")
    e9.grid(row=12, column=7)
    cb_final = ttk.Combobox(root, values = operation)
    cb_final.grid(row=16, column=5)
#########################################################################
    e10 = tk.Entry(root, bd=7, bg="seashell")
    e10.grid(row=16, column=1)
##    cb10 = ttk.Combobox(root, values = operation)
##    cb10.grid(row=16, column=2)
    tk.Label(root, text="stage2").grid(row=14, column=1)
    tk.Label(root, text="from ANS1 & ANS 2").grid(row=15, column=1)

    tk.Label(root, text="ANS2&3").grid(row=15, column=4)
    tk.Label(root, text="stage3").grid(row=14, column=4)
    e11 = tk.Entry(root, bd=7, bg="seashell")
    e11.grid(row=16, column=4)
##    cb11 = ttk.Combobox(root, values = operation)
##    cb11.grid(row=16, column=5)

    tk.Label(root, text="___").grid(row=19, column=4)
    tk.Label(root, text="Final").grid(row=20, column=4)

    tk.Label(root, text="ANS 1-3").grid(row=21, column=4)

    e12 = tk.Entry(root, bd=7, bg="seashell")
    e12.grid(row=22, column=4)
##    cb12 = ttk.Combobox(root, values = operation)
##    cb12.grid(row=22, column=5)

##
##
##    e13 = tk.Entry(root)
##    e13.grid(row=18, column=3)
##    cb13 = ttk.Combobox(root, values = operation)
##    cb13.grid(row=18, column=3)
##
##
##
##    e14 = tk.Entry(root)
##    e14.grid(row=1, column=9)
##
##    cb14 = ttk.Combobox(root, values = operation)
##    cb14.grid(row=1, column=10)
##
##    e15 = tk.Entry(root)
##    e15.grid(row=3, column=9)
##
##    cb15 = ttk.Combobox(root, values = operation)
##    cb15.grid(row=3, column=10)
##



    #btn1 = tk.Button(root, text="Calculate")
    #btn1.grid(row=5, column=6)
    btn2 = tk.Button(root, text="Clear All", bd=5, bg="cyan", command=clr_all)
    btn2.grid(row=5, column=10)
    btn3 = tk.Button(root, text="Clear Stage2", bd=5, bg="light blue", command=clr_stage2)
    btn3.grid(row=9, column=10)
    btn4 = tk.Button(root, text="Clear Stage1", bd=5, bg="orange", command=clr_stage1)
    btn4.grid(row=7, column=10)
    btn5 = tk.Button(root, text="Clrear Stage3", bd=5, bg="light green", command=clr_stage3)
    btn5.grid(row=10, column=10)
    btn6 = tk.Button(root, text="Clear Final", bd=5, bg="violet", command=clr_final)
    btn6.grid(row=11, column=10)
     
    cb1.bind("<<ComboboxSelected>>", op1)
    cb_final.bind("<<ComboboxSelected>>", op6)
    cb2.bind("<<ComboboxSelected>>", op2)
    cb_2536.bind("<<ComboboxSelected>>", op5)
    cb3.bind("<<ComboboxSelected>>", op3)
    cb_1425.bind("<<ComboboxSelected>>", op4)




main()
root.mainloop()

