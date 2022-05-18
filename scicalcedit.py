import tkinter as tk
from tkinter import ttk
import tkinter.font
from tkinter import *
import math

# welcome to the world of the global hell
# To make this work easily everything just had go this way
# At one point you get tired of errors, name error, arguement rules, undefined errors, call before referenced, unbound ect...
# Dont what to go stack exchange all the time, even if I do, I regret it.
# And you need something to work, as a newbie, I will figure out how to make this proper.
def clearall():
    global expression
    global equation
    global value
    global ans
    expression=''
    value=''
    ans=''
    equation.set(expression)

def sgn(a):
    return 1 if a>0 else -1 if a<0 else 0

def clearback():
    result1=""
    result2=""
    global equation
    global expression
    global value
    global ans

    expression = area.get()
    temp1= list(expression)    
    temp2= list(value)
        
    if value=='':
        temp1=[]
        temp2=[]
    elif expression[-5:] in ["asin(","acos(","atan("]:
        for _ in range(5):temp1.pop()
        for _ in range(10):temp2.pop()
   
    elif expression[-4:]=="log(":
        for _ in range(4):temp1.pop()
        for _ in range(11):temp2.pop()
        
    elif expression[-4:] in ['sin(','cos(','tan(']:
        for _ in range(4): temp1.pop()
        for _ in range(9): temp2.pop()
    
    elif expression[-4:]=='sgn(':
        for _ in range(4): temp1.pop()
        for _ in range(4): temp2.pop()
        
    elif expression[-3:]=='ln(':
        for _ in range(3):temp1.pop()
        for _ in range(9): temp2.pop()
        
    elif expression[-2:]=='e^':
        for _ in range(2):temp1.pop()
        for _ in range(8): temp2.pop()
        
    elif expression[-1]=='^':
        for _ in range(1):temp1.pop()
        for _ in range(2): temp2.pop()

    elif expression[-1]=="√":
        for _ in range(1):temp1.pop()
        for _ in range(10):temp2.pop()
        
    elif expression[-1]=='π':
        for _ in range(1):temp1.pop()
        for _ in range(7): temp2.pop()
        
    elif expression[-1]=='e':
        for _ in range(1):temp1.pop()
        for _ in range(6): temp2.pop() 

    elif expression[-1]=='%':
        for _ in range(1):temp1.pop()
        for _ in range(4): temp2.pop()      
        
    else: 
        temp1.pop()
        temp2.pop()
        
    for element in range(len(temp1)):
        result1+=temp1[element]
    expression = result1
    equation.set(expression)
        
    for element in range(len(temp2)):
        result2+=temp2[element]
        
    value=result2
    try:ans = str(eval(value))
    except:pass
    
def pressbtn(num):
    global expression 
    global value
    global ans
    expression = expression + str(num)
    equation.set(expression)
    if num in ["1","2","3","4","5","6","7","8","9","0","(",")","00"]:
        value += num
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"
        
    elif num in ["+",'-','/','*','.','1/','sgn(']:
        value += num
      
    elif num in ['asin(','acos(','atan(','sin(','cos(','tan(']:
        value += 'math.'+ num
    
    elif num=='^':value += '**'
    
    elif num=='%':
        value += '/100'
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"
    elif num=='^2':
        value += '**2'
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"
    elif num=='^3':
        value += '**3'
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"

    elif num=='√(':value += 'math.sqrt('
    
    elif num=='e':
        value += 'math.e'
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"
    elif num=='π':
        value += 'math.pi'
        try:ans = str(eval(value))
        except:ans = "Invalid Expression"
    elif num=='log(':value += 'math.log10('
    elif num=='ln(':value += 'math.log('
    elif num=='e^':value += 'math.e**'
    
def command():
    pass

def equal():
    global ans
    global value
    global expression
    
    if value=="":
        ans=""
        
    equation.set(ans)
    ans=''
    value=''
    expression=''

root=Tk()
root.title("Scientific rootculator")

root.resizable(False,False)
frm = tk.Frame(root, height=50, width=80)
frm.grid()
frm.configure(bg="burlywood4")
equation=StringVar()

area = Entry(root, textvariable = equation,width= 60, font= ("URW Chancery L", 15),bd=10 ,justify=LEFT,state=NORMAL,
             disabledbackground="white",disabledforeground="black") 
area.insert(0,"0")
area.grid(row=0,columnspan=8)

def standard():
    root.geometry('400x400')
    area['width']=40
    area.grid(row=0,columnspan=4,sticky= EW)
    root.title(" Py Standard Calculator")
    
def scientific():
    root.geometry('800x800')
    area['width']=80
    area.grid(row=0,columnspan=8)
    root.title("Py Scientific rootculator")

menubar = Menu(root)
filemenu= Menu(menubar,tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label= "Standard", command= standard)
filemenu.add_separator()
filemenu.add_command(label="Scientific", command= scientific)
root.config(menu=menubar)

value=""   
ans=""
expression=""

font= tkinter.font.Font(size=12,weight= "bold", family='URW Chancery L',)
h=2
w=7
actvbgnd='white'
bg1='light blue'
bg2="pink"
bg3="light green"
bg4= "violet"
fg1= "white"
fg2="black"

numberpad = [7,8,9,4,5,6,1,2,3]
i=0


btn1=tk.Button(root, text='', command=command)
btn1.grid(column=0, row=1)
btn2=tk.Button(root, text='2', command=command)
btn2.grid(column=0, row=2)
btn3=tk.Button(root, text='', command=command)
btn3.grid(column=0, row=3)
btn4=tk.Button(root, text='HEX D', command=command)
btn4.grid(column=0, row=4)
btn5=tk.Button(root, text='HEX A', command=command)
btn5.grid(column=0, row=5)
btn6=tk.Button(root, text='7', command=command)
btn6.grid(column=0, row=6)
btn7=tk.Button(root, text='4', command=command)
btn7.grid(column=0, row=7)
btn8=tk.Button(root, text='1', command=command)
btn8.grid(column=0, row=8)
btn9=tk.Button(root, text='0', command=command)
btn9.grid(column=0, row=9)
btn10=tk.Button(root, text='.', command=command)
btn10.grid(column=0, row=10)


btn11=tk.Button(root, text='btn11', command=command)
btn11.grid(column=1, row=1)
btn12=tk.Button(root, text='btn12', command=command)
btn12.grid(column=1, row=2)
btn13=tk.Button(root, text='auto2', command=command)
btn13.grid(column=1, row=3)
btn14=tk.Button(root, text='HEX E', command=command)
btn14.grid(column=1, row=4)
btn15=tk.Button(root, text='HEX B', command=command)
btn15.grid(column=1, row=5)
btn16=tk.Button(root, text='8', command=command)
btn16.grid(column=1, row=6)
btn17=tk.Button(root, text='5', command=command)
btn17.grid(column=1, row=7)
btn18=tk.Button(root, text='2', command=command)
btn18.grid(column=1, row=8)
btn19=tk.Button(root, text='button 9', command=command)
btn19.grid(column=1, row=9)
btn20=tk.Button(root, text='button 10', command=command)
btn20.grid(column=1, row=10)


btn21=tk.Button(root, text='btn21', command=command)
btn21.grid(column=2, row=1)
btn22=tk.Button(root, text='btn22', command=command)
btn22.grid(column=2, row=2)
btn23=tk.Button(root, text='auto2', command=command)
btn23.grid(column=2, row=3)
btn24=tk.Button(root, text='HEX F', command=command)
btn24.grid(column=2, row=4)
btn25=tk.Button(root, text='HEX C', command=command)
btn25.grid(column=2, row=5)
btn26=tk.Button(root, text='9', command=command)
btn26.grid(column=2, row=6)
btn27=tk.Button(root, text='6', command=command)
btn27.grid(column=2, row=7)
btn28=tk.Button(root, text='3', command=command)
btn28.grid(column=2, row=8)
btn29=tk.Button(root, text='button 9', command=command)
btn29.grid(column=2, row=9)
btn30=tk.Button(root, text='button 10', command=command)
btn30.grid(column=2, row=10)

btn31=tk.Button(root, text='-----', command=command)
btn31.grid(column=3, row=1)
btn32=tk.Button(root, text='------', command=command)
btn32.grid(column=3, row=2)
btn33=tk.Button(root, text='------', command=command)
btn33.grid(column=3, row=3)
btn34=tk.Button(root, text='button 34', command=command)
btn34.grid(column=3, row=4)
btn35=tk.Button(root, text='button 35', command=command)
btn35.grid(column=3, row=5)
btn36=tk.Button(root, text='button 36', command=command)
btn36.grid(column=3, row=6)
btn37=tk.Button(root, text='button 37', command=command)
btn37.grid(column=3, row=7)
btn38=tk.Button(root, text='button 38', command=command)
btn38.grid(column=3, row=8)
btn39=tk.Button(root, text='39', command=command)
btn39.grid(column=3, row=9)
btn40=tk.Button(root, text='button 40', command=command)
btn40.grid(column=3, row=10)


btn41=tk.Button(root, text='btn41', command=command)
btn41.grid(column=4, row=1)
btn42=tk.Button(root, text='btn42', command=command)
btn42.grid(column=4, row=2)
btn43=tk.Button(root, text='btn43', command=command)
btn43.grid(column=4, row=3)
btn44=tk.Button(root, text='button 44', command=command)
btn44.grid(column=4, row=4)
btn45=tk.Button(root, text='button 45', command=command)
btn45.grid(column=4, row=5)
btn46=tk.Button(root, text='button 46', command=command)
btn46.grid(column=4, row=6)
btn47=tk.Button(root, text='button 47', command=command)
btn47.grid(column=4, row=7)
btn48=tk.Button(root, text='button 48', command=command)
btn48.grid(column=4, row=8)
btn49=tk.Button(root, text='button 49', command=command)
btn49.grid(column=4, row=9)
btn50=tk.Button(root, text='button 50', command=command)
btn50.grid(column=4, row=10)








##for j in range(3):
##    for k in range(3):
##        Button(root,command  = lambda x = str(numberpad[i]) : pressbtn(x), text = str(numberpad[i]), bg= bg1, fg=fg2,activebackground=actvbgnd,
##               height=h, width=w,font= font).grid(row=j+2,column=k)
##        i+=1
##
##r=10
##c=10
##Button(root,command  = lambda: pressbtn('0'),  text = "0", bg= bg1, fg=fg2,activebackground=actvbgnd,
##                    height=h, width=w,font= font).grid(row=r,column= c-7)
##Button(root,command  = lambda: pressbtn('00'),text = "00", bg= bg1, fg=fg2,activebackground=actvbgnd,
##                    height=h, width=w,font= font).grid(row=r,column= c-6)
##Button(root,command  = clearback,            text = "C", bg= bg2, fg=fg2,activebackground=actvbgnd,
##                    height=h, width=w,font= font).grid(row=r-4,column= c-7)
##Button(root,command  = clearall,              text = "AC",bg= bg2, fg=fg2,activebackground=actvbgnd,
##                   height=h, width=w,font= font).grid(row=r-4,column= c-6)
##Button(root,command  = lambda: pressbtn('.'), text = "•", bg= bg3, fg=fg2,activebackground=actvbgnd,
##                   height=h, width=w,font= font).grid(row=r,column=c-5)
##Button(root,command  = lambda: pressbtn('+'), text = "+", bg= bg3, fg=fg2,activebackground=actvbgnd,
##                   height=h, width=w,font= font).grid(row=r-2,column=c-4)
##Button(root,command  = lambda: pressbtn('-'),  text = "–", bg= bg3, fg=fg2,activebackground=actvbgnd,
##                  height=h, width=w,font= font).grid(row=r-3,column=c-4)
##Button(root,command  = lambda: pressbtn('/'),   text = "/", bg= bg3, fg=fg2,activebackground=actvbgnd,
##                 height=h, width=w,font= font).grid(row=r-4,column=c-5)
##Button(root,command  = lambda: pressbtn('*'),  text = "✶", bg= bg3, fg=fg2,activebackground=actvbgnd,
##                  height=h, width=w,font= font).grid(row=r-4,column=c-4)
##Button(root,command  = equal,                text = "=", bg= bg2, fg=fg2,activebackground=actvbgnd,
##                    height=2*h,width=w,font= font,pady=10).grid(row=r-1,column=c-4,rowspan=2,)

list1=['(',')','%','asin','sin','log','x^2','acos','cos','ln','x^3','atan','tan','e^x','1/x','x^y','e',"π",'√x','sgn']
list2=['(',')','%','asin(','sin(','log(','^2','acos(','cos(','ln(','^3','atan(','tan(','e^','1/','^','e',"π",'√(','sgn(']
i=0
for j in range(8):
    for k in range(8):
        Button(root,command  = lambda x= list2[i]: pressbtn(x),  text = list1[i], bg=bg4,  fg= fg2,activebackground=actvbgnd,
               height=h,width=w,font= font).grid(row=j+2,column=k+10)
        i+=1

msize=80
root.rowconfigure(0,minsize=50)
for i in range(1,6):
    root.rowconfigure(i,minsize=60)

msize = 120
for i in range(8): 
    root.columnconfigure(i,minsize= msize)

root.mainloop()
