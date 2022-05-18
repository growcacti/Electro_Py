import tkinter as tk
# ohms law with GUI for power and resistance
# --- functions ---

def generate():
    try:
        num12 = float(num1.get()) - float(num2.get())
        num33 = float(num3.get()) / 1000
        result = float(num12) / float(num33)
        result2 = float(num12)* float(num33)
        e1.insert(0, result)
        e2.insert(0, result2)
    except Exception as ex:
        print(ex)
        result = 'error'
   
    return result

    
    #num4.set(result2)

# --- main ---

info_str="""Color      Voltage Drop (V)
Red       	                 2
Green 	                    2.1
Blue                            3.6
White 	                    3.6
Yellow 	                    2.1
Orange 	                    2.2
Amber 	                    2.1
Infrared                      1.7
Other 	                     2
Rainbow                       2.8
max current for single LED is typically 20ma
 """ 
root = tk.Tk()
root.geometry("600x600")
root.title("LED series resistor calc")

tk.Label(root, text="Input Source Volts:").grid(row=0, column=0)
tk.Label(root, text="Input LED Voltage drop:").grid(row=1, column=0)
tk.Label(root, text="Input Current in mA:").grid(row=2, column=0)


num1 = tk.Entry(root, bd=10, bg="seashell")
num1.grid(row=0, column=1)
num2 = tk.Entry(root, bd=10, bg="seashell")
num2.grid(row=1, column=1)
num3 = tk.Entry(root, bd=10, bg="seashell")
num3.grid(row=2, column=1)
e1 = tk.Entry(root, bd=10, bg="seashell")
e1.grid(row=6, column=1)
e2 = tk.Entry(root, bd=10, bg="seashell")
e2.grid(row=8, column=1)
tk.Label(root, text="Ohms").grid(row=6, column=2)
tk.Label(root, text="Power Rating").grid(row=8, column=2)
button = tk.Button(root, text="Calculate", bd=7, bg="orange", command=generate)
button.grid(row=4, column=1)
tk.Label(root,text=info_str).grid(row=11, column=1)
root.mainloop()
