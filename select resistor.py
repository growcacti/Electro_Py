import tkinter as tk
from tkinter import *
import subprocess
import sys
import runpy

top = Tk()
top.title("Electro Py Eng Math App")
top.geometry('300x600')
top.configure(bg='light green')


   
def run2():
    runpy.run_path(path_name='2res_para.py')
                   
def run3():
    runpy.run_path(path_name='3res_para.py')

def run4():
    runpy.run_path(path_name='4res_para.py')

def run5():
    runpy.run_path(path_name='5res_para.py')
def run6():
    runpy.run_path(path_name='6res_para.py')

def run7():
    runpy.run_path(path_name='7res_para.py')
def run8():
    runpy.run_path(path_name='8res_para.py')

def run9():
    runpy.run_path(path_name='9res_para.py')
def run10():
    runpy.run_path(path_name='10res_para.py')





frame = LabelFrame(top, text='Number of Parallel Resistors', padx=50, bg= 'light blue')
frame.pack()

Label(top, text='to calculate 2 - 10  resistors select number button below').pack()



btn02 = Button(top, text='2', command=run2, padx=20, pady=5).pack(pady=10)

btn03 = Button(top, text='3', command=run3, padx=20, pady=5).pack(pady=10)
btn04 = Button(top, text='4', command=run4, padx=20, pady=5).pack(pady=10)
btn05 = Button(top, text='5', command=run5, padx=20, pady=5).pack(pady=10)
btn06 = Button(top, text='6', command=run6, padx=20, pady=5).pack(pady=10)
btn07 = Button(top, text='7', command=run7, padx=20, pady=5).pack(pady=10)
btn08 = Button(top, text='8', command=run8, padx=20, pady=5).pack(pady=10)
btn09 = Button(top, text='9', command=run9, padx=20, pady=5).pack(pady=10)
btn10 = Button(top, text='10', command=run10, padx=20, pady=5).pack(pady=10)










top.mainloop()
