from tkinter import *
from tkinter.ttk import *

import math
import time

def animate():
    print("dgr")

def makegraph(event,A,B,C,D):

    g.delete("abc")
    print(A,B,C,D)
    
    
    AVal.delete(0,END)
    AVal.insert(0,A)
    BVal.delete(0,END)
    BVal.insert(0,B)
    CVal.delete(0,END)
    CVal.insert(0,C)
    
    DVal.delete(0,END)
    DVal.insert(0,D)

    xy = []

    for x in range(0,7600):
        # x coordinates
        xy.append(x)
        # y coordinates
        y1 = float(A*math.sin(((2*math.pi)* B)*(x+C)) + D * -1)
        y2 = float(math.sin(((2*math.pi)* B)*(x*3))+ D) * -1
        y3 = float(math.sin(((2*math.pi)* B)* (x*5))+  D * -1)
        y4 = float(math.sin(((2*math.pi)* B)* (x*7)) + D * -1)
        y = float(y1) * float(y2) * float(y3) * float(y4)
        xy.append(y)
        #g.create_text(x,y, fill="black", text="•",tags=("abc"),)
        
    g.create_line(xy,fill="blue", tags=("abc"), width=2) 
    
    #print(xy)
    

root = Tk()
root.title("Amplitude, Period, Phase Shift and Frequency Graph Generator")
root.geometry("800x600+260+50")
root.resizable(False,False)

g = Canvas(root, background="#fff", height="600", width="960")
g.create_line(40,0,40,400,fill="green", width=1)
g.create_line(0,200,760,200,fill="red", width=1)
g.create_text(25,25, text="↑\ny", font=("colonna",14,"bold"),fill="green")
g.create_text(740,210, text="x →", font=("colonna",14,"bold"),fill="red")
g.place(x=10, y=10)

Label(root, text="Amplitude (A)").place(x=10, y=440)
Label(root, text="Period (2*PI/B)").place(x=10, y=480)
Label(root, text="Phase Shift (C)").place(x=10, y=520)
Label(root, text="Vertical Shift (D)").place(x=10, y=560)

A = DoubleVar()
A.set(2.44)

B = DoubleVar()
B.set(100.0)
C = DoubleVar()
C.set(321.0)
D = DoubleVar()
D.set(4.0)

AText = StringVar()
AText.set(A.get())

BText = StringVar()
BText.set(B.get())

CText = StringVar()
CText.set(C.get())

DText = StringVar()
DText.set(D.get())

A = Scale(root, variable=A, length=400, from_=0.0001, to = 3)
A.place(x=100, y=440)
AVal = Entry(root, width=20, textvariable=AText)
AVal.place(x=510, y=440)

B = Scale(root, variable=B, length=400, from_=1, to = 380)
B.place(x=100, y=480)
BVal = Entry(root, width=20, textvariable=BText)
BVal.place(x=510, y=480)

C = Scale(root, variable=C, length=400, from_=1, to = 760)
C.place(x=100, y=520)
CVal = Entry(root, width=20, textvariable=CText)
CVal.place(x=510, y=520)

D = Scale(root, variable=D, length=400, from_=0.001, to = 10)
D.place(x=100, y=560)
DVal = Entry(root, width=20, textvariable=DText)
DVal.place(x=510, y=560)

Label(root, text="Source :\nmathsisfun.com \n\nEquation Used: \n y = A sin(B(x + C)) + D\n\nThis program can be\nused to demonstrate\nthe above equation.").place(x=650,y=440)

root.bind("<ButtonRelease-1>",lambda event:makegraph(event, A.get(),B.get(),C.get(),D.get()))

root.mainloop()
