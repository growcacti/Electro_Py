import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import os
import subprocess
import shutil


     
def opensystem(event):
    x = lb.curselection()[0]
    os.system(lb.get(x))
    with open(file, 'r') as file:
        file = file.read()
        text.delete('1.0', tk.END)
        text.insert(tk.END, file)
        return
def showcontent(x):
    lb.focus()
    x = lb.curselection()[0]
    file = lb.get(x)
    with open(file, 'r') as file:
        file = file.read()
        text.delete('1.0', tk.END)
        text.insert(tk.END, file)         
        return
    
#


#-----------------------------------------------------------------------------
# GUI Magic Starts Here
#----------------------------------------------------------------------------

r = tk.Tk()
r.geometry('1800x1080')
r.title("GUI TEMPLATE")
notebook = ttk.Notebook(r)
notebook.grid(row=0, column=0)
f1 = ttk.Frame(notebook, width=1500, height=2000)
f1.grid(row=0, column=0)

notebook.add(f1, text='TAB1')

def command():
    pass

#btn1=tk.Button(f1, text='LBFM File Manager', command=command)
#btn1.grid(column=0, row=1)
##btn2=tk.Button(f1, text='button', command=command)
##btn2.grid(column=0, row=2)
##btn3=tk.Button(f1, text='button', command=command)
##btn3.grid(column=0, row=3)
##btn4=tk.Button(f1, text='button', command=command)
##btn4.grid(column=0, row=4)
##btn5=tk.Button(f1, text='button', command=command)
##btn5.grid(column=0, row=5)
##btn6=tk.Button(f1, text='button', command=command)
##btn6.grid(column=0, row=6)

text = tk.Text(f1, bg='wheat', height=50)
text.insert('1.0', tk.END)
text.grid(row=1, column=4, rowspan=25, columnspan=10)
###text2 = tk.Text(f1, bg='pink')
###text2.insert('1.0', tk.END)
###text2.grid(row=1, column=8, rowspan=25, columnspan=10)
###text = tk.Text(f1, bg='light green')
###text.insert('1.0', tk.END)
###text.grid(row=1, column=4, rowspan=25, columnspan=10)
lb = tk.Listbox(f1, height=50, bg="orange", exportselection=False, selectmode=tk.MULTIPLE)
lb.grid(row=1, column=3, rowspan=20, sticky="nswe")
lb.focus()
lb.configure(selectmode="")
flist = os.listdir()
for item in flist:
    lb.insert(tk.END, item)

lb.bind("<<ListboxSelect>>", showcontent)
lb.bind("<Double-Button-1>", opensystem)



r.mainloop()

    
r.mainloop()
   

