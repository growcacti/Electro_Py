import tkinter as tk


import math





f11 = tk.Tk()

def clear():
    lb71.delete(0, tk.END)
    lb81.delete(0, tk.END)


def generate():
    
    try:
        r1 = num1.get()
        r2 = num2.get()
        rdiv = float(r2) / float(r1)
        rp1 = rdiv + 1
        vout = 1.25 * rp1



        lb71.insert(1, r1)
        lb71.insert(2, r2)
        lb71.insert(3, vout)



        lb81.insert(1, 'r1')
        lb81.insert(2, 'r2')

        lb81.insert(3, 'Vout')



    except Exception as ex: 
        print(ex)


f11.title("2 resistore calc for Regulator LM317 Family")



tk.Label(f11, text=" Input R1:").grid(row=0, column=0)
tk.Label(f11, text="Input R2:").grid(row=1, column=0)


num1 = tk.Entry(f11, bg="yellow")
num1.grid(row=0, column=1)
num2 = tk.Entry(f11, bg="yellow")
num2.grid(row=1, column=1)

b1 = tk.Button(f11, text="Calculate", command=generate)
b1.grid(row=6, column=0)
b2 = tk.Button(f11, text="Clear", command=clear)
b2.grid(row=7, column=0)
lb71 = tk.Listbox(f11, bg="pink")
lb71.grid(row=5, column=2)
lb81 = tk.Listbox(f11, bg="light green")
lb81.grid(row=5, column=3)


f11.mainloop()
