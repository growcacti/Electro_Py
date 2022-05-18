import tkinter as tk
from tkinter import Entry, END 
# calculate specs
# --- functions ---

def generate():
    try:
        r = float(e1.get())
        p = float(e2.get()) / 100
        per =  float(r) * float(p)
        lower = float(r) - float(p)
        upper = float(p) + float(r)
        e3.insert(0, lower)
        e4.insert(0, upper)
    except Exception as ex:
        print(ex)
        result = 'error'

   

def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)



# --- main ---

root = tk.Tk()
root.geometry('300x200')
root.title("Calculate Spec from Percentage") 


tk.Label(root, text=" Input Value").grid(row=0, column=0)
tk.Label(root, text="Percentage").grid(row=1, column=0)
tk.Label(root, text="is").grid(row=2, column=0)
tk.Label(root, text="and").grid(row=3, column=0)

e1 = tk.Entry(root, bd=7)
e1.grid(row=0, column=1)
e2 = tk.Entry(root, bd=7)
e2.grid(row=1, column=1)
e3 = tk.Entry(root, bd=7)
e3.grid(row=2, column=1)
e4 = tk.Entry(root, bd=7)
e4.grid(row=3, column=1)
button = tk.Button(root, text="Calculate", command=generate)
button.grid(row=4, column=1)
button2 = tk.Button(root, text="Clear", command=clear)
button2.grid(row=5, column=1)

root.mainloop()
