import tkinter as tk
from tkinter import ttk, END, Toplevel,Frame,Entry,Label,Text,Button
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Combobox

from datetime import datetime

import math
import time
import itertools
import os

########################
####GLOBAL_CONSTANTS####
########################
FREQ_UNIT =  {
            'THz': 1e12,
            'GHz': 1e9,
            'MHz': 1e6,
            'kHz': 1e3,
            'Hz': 1,
            'mHz': 1e-3
        }
class ScrollableNotebook(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1000x800')
        self.title('ELECTRO-PY MATH APP')

        # Create a frame for the notebook and scrollbar
        notebook_frame = tk.Frame(self, width=600,height=600)
        notebook_frame.grid(row=0, column=0,rowspan=4,columnspan=4, sticky='nsew')

        # Configure the grid to expand the frame
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

       
        self.canvas = tk.Canvas(notebook_frame, width=600,height=600)
        self.canvas.grid(row=0, column=0, sticky='nsew')

        # Add a scrollbar to the frame
        scrollbar = ttk.Scrollbar(notebook_frame, orient='horizontal', command=self.canvas.xview)
        scrollbar.grid(row=23, column=0, sticky='ew')
        self.canvas.configure(xscrollcommand=scrollbar.set)

        # Configure the notebook frame grid
        notebook_frame.grid_rowconfigure(0, weight=1)
        notebook_frame.grid_columnconfigure(0, weight=1)

        # Create a frame inside the canvas to hold the notebook
        notebook_frame_inside = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=notebook_frame_inside, anchor='nw')

        # Create the notebook
        self.notebook = ttk.Notebook(notebook_frame_inside)
        self.notebook.grid(row=0, column=0, sticky='nsew')
        notebook_frame_inside.bind('<Configure>', self.on_configure)
       

    
    def on_configure(self, event):

         self.canvas.configure(scrollregion=self.canvas.bbox('all'))

       
    def add_tab(self, title, **kwargs):
        frame = ttk.Frame(self.notebook, **kwargs)
        self.notebook.add(frame, text=title)
        return frame 
        '''
        Add a new tab to the notebook.

        :param frame: The frame (or any widget) to be used as the content of the tab.
        :param title: The title of the tab.
        '''
        self.notebook.add(frame, text=title)
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))


nb = ScrollableNotebook()

class TabFrame:
    def __init__(self):
        self.f0 = nb.add_tab('Title Page')
        ttk.Label(self.f0, text=' ').grid(row=1,column=1)
        self.f1 = nb.add_tab('Iter Calc')
        ttk.Label(self.f1, text='Iter Calc').grid(row=1,column=1)
        self.f2 = nb.add_tab('Ohms Law')
        ttk.Label(self.f2, text='O').grid(row=1,column=1)
        self.f3 = nb.add_tab('RFCalc')
        ttk.Label(self.f3, text= 'RL & VSWR, Wavelenght, dBm & W').grid(row=1,column=1)
        self.f4 = nb.add_tab('ResonantCalc')
        ttk.Label(self.f4, text='Calculate Frequency Capacitance & Inductance @ Resonance').grid(row=1,column=1)
        self.f5 = nb.add_tab('Calculator')
        ttk.Label(self.f5, text='Calculator').grid(row=1,column=1)
        self.f6 = nb.add_tab('StopWatch')
        ttk.Label(self.f6, text='Pystopwatch').grid(row=1,column=1)
        self.f7 = nb.add_tab('Percentage')
        ttk.Label(self.f7, text='Percentage +/- Spec Calc').grid(row=1,column=1)
        self.f8 = nb.add_tab('Convert')
        ttk.Label(self.f8, text='Common Unit Conversions').grid(row=1,column=1)
        self.f13 = nb.add_tab('MEM')
        ttk.Label(self.f13, text='History& Memory').grid(row=0,column=1)
        ttk.Label(self.f13, text='Load Previous Stored History').grid(row=0,column=10)
        self.f14 = nb.add_tab('Complex')
        ttk.Label(self.f14, text='Complex Numbers').grid(row=1,column=1)
       
tab=TabFrame()


class Mem:
    def __init__(self):
        self.lb = tk.Listbox(tab.f13,bd=7,width=80, height=45)
        self.lb.grid(row=1, column=0, rowspan=6,columnspan=5, sticky="ns")
        self.path = os.getcwd()
        self.btn_1 = tk.Button(tab.f13,bd=5,text='Open',command=self.open_file)
        self.btn_1.grid(row=0, column=8)
        self.btn_2 = tk.Button(tab.f13,bd=5,text='Save',command=self.save_file)
        self.btn_2.grid(row=1, column=8)
        self.btn_3 = tk.Button(tab.f13, bd=5,text='Clear', command=self.clear)
        self.btn_3.grid(row=2, column=8, sticky='ew', padx=5, pady=5)
        self.textwidget = ScrolledText(tab.f13, bg='white', bd=12, height=35,width=60,)
        self.textwidget.grid(row=1, column=10,sticky='e')



    def sto(self, *args):
        self.lb.insert(END, args)
        print(args)

    def open_file(self):
        '''Open a file for editing.'''
        filepath = askopenfilename(
            filetypes=[('Text Files', '*.txt'),
                ('All Files', '*.*'),
            ]
        )
        if not filepath:
            return
        self.textwidget.delete(1.0, tk.END)
        with open(filepath, 'r') as input_file:
            text = input_file.read()
            self.textwidget.insert(tk.END, text)
            return filepath

    def save_file(self):
        filepath = asksaveasfilename(
            defaultextension='.txt',
            filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')],
        )
        if not filepath:
            return
        with open(filepath, 'w') as output_file:
            text = self.textwidget.get(1.0, tk.END)
            output_file.write(text)
            return filepath
    def clear(self):
        self.lb.delete(0, tk.END)
        self.textwidget.delete('1.0', tk.END)
    
mem = Mem()
def zero_tab():
   

        
    label1 = tk.Label(tab.f0, text='              ', font=('Arial', 14)).grid(row=2, column=0)
    label2 = tk.Label(tab.f0, text='              ', font=('Arial', 14)).grid(row=1, column=0)
    label3 = tk.Label(tab.f0, text='              ', font=('Arial', 14)).grid(row=3, column=0)
    ####
    label1 = tk.Label(tab.f0, text='Electro PY Notebook Math App', bg='azure', font=('Arial Black', 16)).grid(row=0, column=5)
zero_tab()




def scalc():    
    def sscalculate():
         num = float(entry_num.get())
         start = float(entry_start.get())
         stop = float(entry_stop.get())
         step = float(entry_step.get())

         operation = combo_operation.get()

         result_list.delete(0, tk.END)
         step_list.delete(0, tk.END)

         for i in range(int((stop - start)/step) + 1):
             current_val = start + i * step
             step_list.insert(tk.END, current_val)

             if operation == 'Add':
                 result_list.insert(tk.END, num + current_val)
                 mem.sto(num + current_val)
             elif operation == 'Subtract':
                 result_list.insert(tk.END, num - current_val)
                 mem.sto(num - current_val)
             elif operation == 'Multiply':
                 result_list.insert(tk.END, num * current_val)
                 mem.sto(num * current_val)
             elif operation == 'Divide':
                 if current_val != 0:
                     result_list.insert(tk.END, num / current_val)
                     mem.sto(num / current_val)
                 else:
                     result_list.insert(tk.END, 'DIV by ZERO')

             elif operation == 'Power of':
                 result_list.delete(i)
                 result_list.insert(i, num ** current_val)

             elif operation == 'SQRT of':
                 result_list.delete(i)
                 result_list.insert(i, math.sqrt(current_val))

             elif operation == 'INV':
                 result_list.delete(i)
                 if current_val != 0:
                     result_list.insert(tk.END, 1 / current_val)
                 else:
                     result_list.insert(tk.END, 'DIV by ZERO')
                    

                 

         if activate_additional.get():
             additional_num = float(entry_additional_num.get())
             additional_op = combo_additional_op.get()

             for i in range(result_list.size()):
                 current_result = float(result_list.get(i))

                 if additional_op == 'Add':
                     result_list.delete(i)
                     result_list.insert(i, current_result + additional_num)
                 elif additional_op == 'Subtract':
                     result_list.delete(i)
                     result_list.insert(i, current_result - additional_num)
                 elif additional_op == 'Multiply':
                     result_list.delete(i)
                     result_list.insert(i, current_result * additional_num)
                 elif additional_op == 'Divide':
                     result_list.delete(i)
                     if additional_num != 0:
                         result_list.insert(i, current_result / additional_num)
                         mem.sto(1, current_result / additional_num)
                     else:
                         result_list.insert('end', 'Can not be Zero')


                 elif additional_op == 'Power of':
                     result_list.delete(i)
                     result_list.insert(i, current_result ** additional_num)
                     mem.sto(i, current_result ** additional_num)

                 elif additional_op == 'SQRT of':
                     result_list.delete(i)
                     result_list.insert(i, math.sqrt(current_result))
                     mem.sto(result_list.get(0, END))

         if activate_additional2.get():
             additional_num2 = float(entry_additional_num.get())
             additional_op2 = combo_additional_op.get()

             for i in range(result_list.size()):
                 current_result = float(result_list.get(i))

                 if additional_op2 == 'Add':
                    result_list.delete(i)
                    result_list.insert(i, current_result + additional_num)
                 elif additional_op2 == 'Subtract':
                    result_list.delete(i)
                    result_list.insert(i, current_result - additional_num)
                 elif additional_op2 == 'Multiply':
                    result_list.delete(i)
                    result_list.insert(i, current_result * additional_num)
                 elif additional_op2 == 'Divide':
                    result_list.delete(i)
                    if additional_num != 0:
                        result_list.insert(i, current_result / additional_num)
                        mem.sto(1, current_result / additional_num)
                    else:
                        result_list.insert('end', 'Can not be Zero')


                 elif additional_op == 'Power of':
                    result_list.delete(i)
                    result_list.insert(i, current_result ** additional_num)
                    mem.sto(i, current_result ** additional_num)

                 elif additional_op == 'SQRT of':
                    result_list.delete(i)
                    result_list.insert(i, math.sqrt(current_result))
                    mem.sto(result_list.get(0, END))   
    def sync_scroll(first, last):
        result_list.yview('moveto', first)
        step_list.yview('moveto', first)

    
   
    # Number Entry
    lbl_num = tk.Label(tab.f1, text='Number')
    lbl_num.grid(row=0, column=0)
    entry_num = tk.Entry(tab.f1)
    entry_num.grid(row=0, column=1)

    # Operation ComboBox
    lbl_operation = tk.Label(tab.f1, text='Operation')
    lbl_operation.grid(row=1, column=0)
    combo_operation = ttk.Combobox(tab.f1, values=['Add', 'Subtract', 'Multiply', 'Divide','Power of', 'SQRT of'])
    combo_operation.grid(row=1, column=1)
    combo_operation.set('Add')

    # Range Entries
    lbl_range = tk.Label(tab.f1, text='Start-Stop-Step Range')
    lbl_range.grid(row=2, column=0)
    entry_start = tk.Entry(tab.f1, width=5)
    entry_start.grid(row=2, column=1)
    entry_stop = tk.Entry(tab.f1, width=5)
    entry_stop.grid(row=2, column=2)
    entry_step = tk.Entry(tab.f1, width=5)
    entry_step.grid(row=2, column=3)

    # Result and Steps Listbox
    lbl_result = tk.Label(tab.f1, text='Results')
    lbl_result.grid(row=3, column=0)
    result_list = tk.Listbox(tab.f1, width=20, height=10)
    result_list.grid(row=3, column=1)
    lbl_step = tk.Label(tab.f1, text='Steps')
    lbl_step.grid(row=3, column=2)
    step_list = tk.Listbox(tab.f1, width=20, height=10)
    step_list.grid(row=3, column=3)

    # Scrollbar for the listboxes
    scrollbar = tk.Scrollbar(tab.f1)
    scrollbar.grid(row=3, column=4, sticky='ns')

    result_list.config(yscrollcommand=lambda f, l: sync_scroll(f, l))
    step_list.config(yscrollcommand=lambda f, l: sync_scroll(f, l))


    # Additional Operations and Number
    activate_additional = tk.IntVar()
   
    chk_additional = tk.Checkbutton(tab.f1, text='Activate Additional Operation', variable=activate_additional)
    chk_additional.grid(row=4, column=0)
    combo_additional_op = ttk.Combobox(tab.f1, values=['Add', 'Subtract', 'Multiply', 'Divide', 'Power of', 'SQRT of'])
    combo_additional_op.grid(row=4, column=1)
    entry_additional_num = tk.Entry(tab.f1)
    entry_additional_num.grid(row=4, column=2)
    activate_additional2 = tk.IntVar()
    chk_additional2 = tk.Checkbutton(tab.f1, text='Activate Additional Operation', variable=activate_additional)
    chk_additional2.grid(row=8, column=0)
    combo_additional_op2 = ttk.Combobox(tab.f1, values=['Add', 'Subtract', 'Multiply', 'Divide', 'Power of', 'SQRT of'])
    combo_additional_op2.grid(row=8, column=1)
    entry_additional_num2 = tk.Entry(tab.f1)
    entry_additional_num2.grid(row=8, column=2)

    # Calculate Button
    btn_calculate = tk.Button(tab.f1, text='Calculate', command=sscalculate)
    btn_calculate.grid(row=5, column=0, columnspan=4)
    btn_calculate2 = tk.Button(tab.f1, text='Calculate', command=sscalculate)
    btn_calculate2.grid(row=10, column=0, columnspan=4)
       
    tkbtn2 = tk.Button(tab.f1, text='SSCALC', command=scalc)
    tkbtn2.grid(column=5, row=7)

scalc()
nb001 = ttk.Notebook(tab.f2)
ffr0 = ttk.Frame(nb001)
ffr1 = ttk.Frame(nb001)
ffr2 = ttk.Frame(nb001)
ffr3 = ttk.Frame(nb001)
ffr4 = ttk.Frame(nb001)
ffr5 = ttk.Frame(nb001)
nb001.grid(row=2, column=2)
class Ohms_Law:
    def __init__(self,ffr0):
       
        self.n1 = 1
        self.n2 =1
        self.n3 =1
        self.n4 =1
        self.x = tk.StringVar()
        self.y = tk.StringVar()
        self.options1 = ['Volts ', 'Watts', 'Amps']
        self.options2 = ['Amps', 'Ohms', 'Volts']
        self.n = ttk.Combobox(ffr0, values=self.options1, font=('Arial', 8))
        self.n.set('Volts')
        self.n.grid(row=4, column=2)
        self.n2 = ttk.Combobox(ffr0, values=self.options2, font=('Arial', 8))
        self.n2.set('Ohms')
        self.n2.grid(row=6, column=2)
        self.x = tk.Entry(ffr0, bg='cornsilk', font=('Arial', 8))
        self.x.grid(row=4, column=1)
        self.y = tk.Entry(ffr0, bg='cornsilk', font=('Arial', 8))
        self.y.grid(row=6, column=1)
        self.btn1 = tk.Button(ffr0, text='calculate', bg = 'cyan', font=('Arial', 8), command=self.operations)
        self.btn1.grid(row=8, column=1)
        self.btn2 = tk.Button(ffr0, text='Clear Answers', bg = 'light green', font=('Arial', 8), command=self.clearlist1)
        self.btn2.grid(row=8, column=0)

        self.lboxx1 = tk.Listbox(ffr0)
        self.lboxx1.grid(row=12, column=1)
        self.lboxx2 = tk.Listbox(ffr0)
        self.lboxx2.grid(row=12, column=2)
        self.str1 = ''
        self.str2 = ''
      
    def clearlist1(self):
        self.lboxx1.delete(0, END)
        self.lboxx2.delete(0, END)


   
       
    def operations(self):   
        self.num1 = float(self.x.get())
        self.num2 = float(self.y.get())
        self.cb1 = self.n.get()
        self.cb2 = self.n2.get()
        if self.cb1 == 'Volts' and self.cb2 == 'Amps':
           
            self.num3 = float(self.num1) / float(self.num2)
            self.num4 = float(self.num1) * float(self.num2)
            self.str1 =  'Ohms'
            self.str2 = 'Watts'
        elif self.cb1 == 'Volts' and self.cb2 == 'Ohms':
             self.num3 = float(self.num1) / float(self.num2)
             self.num4 = float(self.num1) * float(self.num1) / float(self.num2)
             self.str1 = 'Amps'
             self.str2 = 'Watts'
        elif self.cb1 == 'Volts' and self.cb2 == 'Watts':
             self.num3 = float(self.num1) * float(self.num1) / float(self.num2)
             self.str1 = 'Ohms'
             self.num4 = float(self.num2) / float(self.num1)
             self.str2 = 'Amps'
        elif self.cb1 == 'Amps' and self.cb2 == 'Ohms':
             self.num3 = float(self.num1) * float(self.num2)
             self.str1 = 'Volts'
             self.num4 = float(self.num1) * float(self.num1) / float(self.num2)
             self.str2 = 'Watts'
        elif self.cb1 == 'Watts' and self.cb2 == 'Amps':
             self.num3 = float(self.num1) / float(self.num2) ** 2
             self.str1 = 'Ohms'
             self.num4 = float(self.num1) / float(self.num2)
             self.str = 'Volts'
        elif self.cb1 == 'Watts' and self.cb2 == 'Volts':
             self.num3 = float(self.num1) * float(self.num1) / float(self.num2)
             self.str1 = 'Ohms'
             self.num4 = float(self.num2) / float(self.num1)
        elif self.cb1 == 'Watts' and self.cb2 == 'Ohms':
             self.num3 = math.sqrt(float(self.num1) / float(self.num2))
             self.str1 = 'Amps'
             self.num4 =  math.sqrt(float(self.num1) * float(self.num2))
             self.str2 ='Volts'
        elif self.cb1 == 'Amps' and self.cb2 == 'Watts':
             self.num3 = float(self.num2) / float(self.num1) ** 2
             self.str1 = 'Ohms'
             self.num4 = float(self.num2) / float(self.num1)
             self.str = 'Volts'
        elif self.cb1 == 'Amps' and self.cb2 == 'Amps':
             self.num3 = 1
             self.str1 = 'Amps'
             self.num4 = 1
             self.str2 = 'Amps'
 
        elif self.cb1 == 'Volts' and self.cb2 == 'Volts':
             self.num3 = 1
             self.str1 = 'Volts'
             self.num4 = 1
             self.str2 = 'Volts'

        elif self.cb1 == 'Amps' and self.cb2 == 'Volts':
             self.num3 = float(self.num1) / float(self.num2)
             self.num4 = float(self.num1) * float(self.num2)
             self.str1 =  'Ohms'
             self.str2 = 'Watts'
        else:
             self.num3 = self.num4

     
        self.lboxx1.insert(1, self.num3)
        self.lboxx1.insert(2, self.num4)
        self.lboxx2.insert(1, self.str1)
        self.lboxx2.insert(2, self.str2)
        mem.sto(self.num3)
        mem.sto(self.num4)




class ResistanceCalculator:
    def __init__(self, parent):
        self.parent = parent
        # Number of resistors input
        self.num_resistors_entry = tk.Entry(self.parent, bd=6, bg='cornsilk')
        self.num_resistors_entry.grid(row=0, column=1)
        self.update_btn = tk.Button(self.parent, text='Update Resistors Number of Resistors', command=self.update_resistor_entries)
        self.update_btn.grid(row=0, column=2)

        self.create_widgets()
        
    def create_widgets(self):
        # Create and place all widgets here
        tk.Label(self.parent, text=' Number of parallel resistors').grid(row=0, column=0)
        # ... other labels

        self.num_entries = [tk.Entry(self.parent, bd=6, bg='lavender') for _ in range(10)]
        for i, entry in enumerate(self.num_entries):
            entry.grid(row=i+1, column=1)

        # Buttons
        b1 = tk.Button(self.parent, text='Calculate in Ohms', command=self.do_res_math)
        b1.grid(row=22, column=3)
        b2 = tk.Button(self.parent, text='Clear', command=self.clear)
        b2.grid(row=23, column=3)

        # Listbox
        self.lb7 = tk.Listbox(self.parent, bd=9, bg='light blue', width=25, height=5)
        self.lb7.grid(row=12, column=3, rowspan=5)

    def update_resistor_entries(self):
        try:
            self.clear_resistor_entries()  # Clear existing entries

            num_resistors = int(self.num_resistors_entry.get())
            self.num_entries = [tk.Entry(self.parent, bd=6, bg='azure') for _ in range(num_resistors)]
            for i, entry in enumerate(self.num_entries):
                entry.grid(row=i+1, column=1)
        except ValueError:
            print('Please enter a valid number of resistors.')

    def clear_resistor_entries(self):
        # Destroy or hide existing resistor entries
        for entry in getattr(self, 'num_entries', []):
            entry.grid_forget()

    def do_res_math(self):
        try:
            resistances = [float(entry.get()) for entry in self.num_entries if entry.get()]
            
            # Calculate total resistance in series
            total_series_resistance = sum(resistances)

            # Calculate total resistance in parallel
            total_parallel_reciprocal = sum([1/r for r in resistances if r != 0])
            if total_parallel_reciprocal != 0:
                total_parallel_resistance = 1 / total_parallel_reciprocal
            else:
                total_parallel_resistance = float('inf')  # Infinite resistance for open circuit

            # Update the listbox with results
            self.lb7.insert(tk.END, 'Series')
            self.lb7.insert(tk.END, total_series_resistance)
            self.lb7.insert(tk.END, 'Parallel')
            self.lb7.insert(tk.END, total_parallel_resistance)
            mem.sto('Series'+' \n')
            mem.sto(total_series_resistance)
            mem.sto( 'Parallel'+'\n')
            mem.sto(total_parallel_resistance)




            
        except ValueError:
            # Handle case where the entry is not a valid number
            print('Invalid input! Please enter only numbers.')
        except Exception as ex:
            print(ex)

    def clear(self):
        self.lb7.delete(0, tk.END)





class ReverseParalellResistanceCalculator:
    def __init__(self, root):
        self.root = root
     
        self.series_var = tk.StringVar(self.root)
        self.series_var.set('E24')  # default option
        self.tolerance_var = tk.DoubleVar(self.root)
        self.tolerance_var.set(0.20)  # default tolerance
        self.var_multiple_resistors = tk.IntVar()
        self.var_tolerance_filter = tk.DoubleVar(value=5.0)  # Default to 5% tolerance

        self.base_standard_values = [1.00, 1.01, 1.02, 1.04,
                                    1.05, 1.06, 1.07, 1.09, 1.10,
                                    1.11, 1.13, 1.14, 1.15, 1.17, 1.18, 1.20, 1.21, 1.23,
                                    1.24, 1.26, 1.27, 1.29, 1.30, 1.32, 1.33, 1.35, 1.37,
                                    1.38, 1.40, 1.42, 1.43, 1.45, 1.47, 1.49, 1.50, 1.52,
                                    1.54, 1.56, 1.58, 1.60, 1.62, 1.64, 1.65, 1.67, 1.69,
                                    1.72, 1.74, 1.76, 1.78, 1.80, 1.82, 1.84, 1.87, 1.89,
                                    1.91, 1.93, 1.96, 1.98, 2.00, 2.03, 2.05, 2.08, 2.10,
                                    2.13, 2.15, 2.18, 2.21, 2.23, 2.26, 2.29, 2.32, 2.34,
                                    2.37, 2.40, 2.43, 2.46, 2.49, 2.52, 2.55, 2.58, 2.61,
                                    2.64, 2.67, 2.71, 2.74, 2.77, 2.80, 2.84, 2.87, 2.91,
                                    2.94, 2.98, 3.01, 3.05, 3.09, 3.12, 3.16, 3.20, 3.24,
                                    3.28, 3.32, 3.36, 3.40, 3.44, 3.48, 3.52, 3.57, 3.61,
                                    3.65, 3.70, 3.74, 3.79, 3.83, 3.88, 3.92, 3.97, 4.02,
                                    4.07, 4.12, 4.17, 4.22, 4.27, 4.32, 4.37, 4.42, 4.48,
                                    4.53, 4.59, 4.64, 4.70, 4.75, 4.81, 4.87, 4.93, 4.99,
                                    5.05, 5.11, 5.17, 5.23, 5.30, 5.36, 5.42, 5.49, 5.56,
                                    5.62, 5.69, 5.76, 5.83, 5.90, 5.97, 6.04, 6.12, 6.19,
                                    6.26, 6.34, 6.42, 6.49, 6.57, 6.65, 6.73, 6.81, 6.90,
                                    6.98, 7.06, 7.15, 7.23, 7.32, 7.41, 7.50, 7.59, 7.68,
                                    7.77, 7.87, 7.96, 8.06, 8.16, 8.25, 8.35, 8.45, 8.56,
                                    8.66, 8.76, 8.87, 8.98, 9.09, 9.20, 9.31, 9.42, 9.53,
                                    9.65, 9.76, 9.88,2.20, 2.70, 3.00, 3.30, 3.60, 3.90,
                                    4.30, 5.10, 5.60, 6.20, 6.80, 8.20, 9.10, 1.00, 2.00,
                                    3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00]
        self.multipliers = [1, 10, 100, 1000, 10000, 1000000, 10000000, 100000000]

        self.standard_values = [value * multiplier for value in self.base_standard_values for multiplier in self.multipliers]
        self.create_widgets()
    
    def create_widgets(self):

        self.standard_values = [value * multiplier for value in self.base_standard_values for multiplier in self.multipliers]
        self.create_widgets()
    
    def create_widgets(self):
        self.entry_label = tk.Label(self.root, text='Enter Desired Resistance (Ω):')
        self.entry_label.grid(row=0, column=0, padx=10, pady=10)
        self.entry_desired_resistance = tk.Entry(self.root)
        self.entry_desired_resistance.grid(row=0, column=1, padx=10, pady=10)
    
        self.checkbutton_multiple_resistors = tk.Checkbutton(self.root, text='Use multiple resistors', variable=self.var_multiple_resistors, command=self.toggle_resistor_entry)
        self.checkbutton_multiple_resistors.grid(row=1, column=0, columnspan=2)
        
        self.entry_num_resistors = tk.Entry(self.root)
        self.entry_num_resistors.grid(row=2, column=1, padx=10, pady=10)
        self.entry_num_resistors.insert(0, '2')  # Default number of resistors
        self.entry_num_resistors.config(state=tk.DISABLED)
        
        self.label_num_resistors = tk.Label(self.root, text='Number of Resistors:')
        self.label_num_resistors.grid(row=2, column=0, padx=10, pady=10)
        
        self.submit_button = tk.Button(self.root, text='Calculate', command=self.on_submit)
        self.submit_button.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.clear_button = tk.Button(self.root, text='Clear', command=self.clear_text_area)
        self.clear_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.save_button = tk.Button(self.root, text='Save Results', command=self.save_results)
        self.save_button.grid(row=4, column=2, columnspan=2, pady=10)
        
        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
        
        # Spinbox for setting the error tolerance
        self.label_tolerance = tk.Label(self.root, text="Set Maximum Error (%)")
        self.label_tolerance.grid(row=6, column=0, padx=10, pady=5)
        self.spinbox_tolerance = tk.Spinbox(self.root, from_=1.0, to=20.0, increment=0.1, textvariable=self.var_tolerance_filter)
        self.spinbox_tolerance.grid(row=6, column=1, padx=10, pady=5)

    def on_submit(self):
        self.text_area.delete('1.0', tk.END)  # Clear the text area
        try:
            self.desired_resistance = float(self.entry_desired_resistance.get())
        except ValueError:
            self.text_area.insert(tk.END, "Invalid resistance value. Please enter a number.\n")
            return
        
        self.max_num_resistors = int(self.entry_num_resistors.get()) if self.var_multiple_resistors.get() else 2
        self.combinations_found = False

        tolerance_percentage = self.var_tolerance_filter.get() / 100  # Convert percentage to decimal

        # Check combinations
        for combination in self.generate_combinations(self.desired_resistance, self.max_num_resistors, tolerance=tolerance_percentage):
            if combination is None:
                self.text_area.insert(tk.END, 'No combinations found within the specified tolerance.\n')
                break

            res = combination[-2]
            err = combination[-1] * 100  # Convert error to percentage
            resistors = ', '.join(f'{r}Ω' for r in combination[:-2])
            self.text_area.insert(tk.END, f'{resistors} -> {res:.2f}Ω (Error: {err:.2f}%)\n')
            self.combinations_found = True

        if self.combinations_found:
            # Now show 2x the value of the desired resistance using two equal resistors
            two_equal_resistors_resistance = self.parallel_resistance([self.desired_resistance, self.desired_resistance])
            self.text_area.insert(tk.END, f"\nUsing two resistors of {self.desired_resistance:.2f}Ω gives {two_equal_resistors_resistance:.2f}Ω.\n")
        else:
            self.text_area.insert(tk.END, 'Checked all combinations. No matches found.\n')

    def generate_combinations(self, desired_resistance, max_num_resistors, tolerance=0.20):
        found_combinations = False
        for num_resistors in range(2, max_num_resistors + 1):
            for combination in itertools.combinations_with_replacement(self.standard_values, num_resistors):
                combined_resistance = self.parallel_resistance(combination)
                error = abs((combined_resistance - desired_resistance) / desired_resistance)
                if error <= tolerance:
                    found_combinations = True
                    yield *combination, combined_resistance, error
            if found_combinations:
                break
        if not found_combinations:
            yield None

    def parallel_resistance(self, resistors):
        inverse_sum = sum(1/r for r in resistors)
        return 1 / inverse_sum if inverse_sum != 0 else float('inf')

    def clear_text_area(self):
        self.text_area.delete('1.0', tk.END)

    def toggle_resistor_entry(self):
        if self.var_multiple_resistors.get() == 1:
            self.entry_num_resistors.config(state=tk.NORMAL)
        else:
            self.entry_num_resistors.config(state=tk.DISABLED)
            self.entry_num_resistors.delete(0, tk.END)
            self.entry_num_resistors.insert(0, '2')  # Reset to default value of 2

    def save_results(self):
        # Open a file dialog to save the results
        file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            # Get the content from the text area and save it
            with open(file_path, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))
            tk.messagebox.showinfo("Success", f"Results saved to {file_path}")



class VoltageDividerTab:
    def __init__(self, parent):
        self.parent = parent

        # Number of resistors input
        self.num_resistors_entry = tk.Entry(self.parent, bd=6, bg='cornsilk')
        self.num_resistors_entry.grid(row=0, column=1)
        self.update_btn = tk.Button(self.parent, text='Update Number of Resistors', command=self.update_resistor_entries)
        self.update_btn.grid(row=0, column=2)

        # Voltage input
        tk.Label(self.parent, text='Total Voltage (Vin)').grid(row=1, column=0)
        self.voltage_entry = tk.Entry(self.parent, bd=6, bg='lavender')
        self.voltage_entry.grid(row=1, column=1)

        # Create initial widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Label for number of resistors
        tk.Label(self.parent, text='Number of resistors').grid(row=0, column=0)

        # Initialize empty list for resistor entries
        self.resistor_entries = []

        # Button to calculate voltage
        calculate_btn = tk.Button(self.parent, text='Calculate Voltage', command=self.calculate_voltage)
        calculate_btn.grid(row=22, column=3)

        # Output area
        self.result_label = tk.Label(self.parent, text='')
        self.result_label.grid(row=23, column=1)
        self.lb= tk.Listbox(self.parent, width=40)
        self.lb.grid(row=0 ,column=4,rowspan=4, columnspan=4, sticky='nsew')
        
    def update_resistor_entries(self):
        try:
            self.clear_resistor_entries()

            num_resistors = int(self.num_resistors_entry.get())
            self.resistor_entries = [tk.Entry(self.parent, bd=6, bg='azure') for _ in range(num_resistors)]
            for i, entry in enumerate(self.resistor_entries):
                entry.grid(row=i+2, column=1)
        except ValueError:
            print('Please enter a valid number of resistors.')

    def clear_resistor_entries(self):
        for entry in self.resistor_entries:
            entry.grid_forget()
        self.resistor_entries = []

    def calculate_voltage(self):
        try:
            resistors = [float(entry.get()) for entry in self.resistor_entries]
            total_voltage = float(self.voltage_entry.get())

            if not resistors:
                raise ValueError('No resistors defined')

            # Calculate total resistance
            total_resistance = sum(resistors)

            # Calculate and display voltage across each resistor
            voltages = [total_voltage * (r / total_resistance) for r in resistors]
            self.result_label.config(text='\n'.join(f'Voltage across R{i+1}: {v:.2f}V' for i, v in enumerate(voltages)))
            for i, v in enumerate(voltages):
                self.lb.insert(tk.END, f'Voltage across R{i+1}: {v:.2f}V')
                mem.sto(f'Voltage across R{i+1}: {v:.2f}V')
        except ValueError as e:
            print('Error:', e)

nb001.add(ffr0, text='Ohms Laws Calc')
nb001.add(ffr1, text='Parallel/Series Calc')
nb001.add(ffr2, text = 'Reverse Parallel Resistor Calc')
nb001.add(ffr3, text='Voltage divder')
ohms = Ohms_Law(ffr0)
resistance_calculator = ResistanceCalculator(ffr1)
reverse_calc = ReverseParalellResistanceCalculator(ffr2)
voltage_divider = VoltageDividerTab(ffr3)


nb002 = ttk.Notebook(tab.f3)
ffm0 = ttk.Frame(nb002)
ffm1 = ttk.Frame(nb002)
ffm2 = ttk.Frame(nb002)
ffm3 = ttk.Frame(nb002)
ffm4 = ttk.Frame(nb002)
ffm5 = ttk.Frame(nb002)
ffm6 = ttk.Frame(nb002)
nb002.grid(row=2, column=0)
class Vswr:
    def __init__(self,ffm0):
        # Create widgets
        self.vswr_label = tk.Label(ffm0, text='Enter VSWR: example 1.5')
        self.vswr_entry = tk.Entry(ffm0)
        self.return_loss_label = tk.Label(ffm0, text='Enter Return Loss (dB): example -14')
        self.return_loss_entry = tk.Entry(ffm0)
        self.calculate_button = tk.Button(ffm0, text='Calculate', command=self.calculate)
        self.result_label = tk.Label(ffm0, text='Result')
        self.lb = tk.Listbox(ffm0)
        self.lb.grid(row=10,column=0)
        self.vswr_var = tk.BooleanVar(value=True)
        self.vswr_radio = tk.Radiobutton(ffm0, text='VSWR to Return Loss', variable=self.vswr_var, value=True, command=self.toggle_entry)
        self.return_loss_radio = tk.Radiobutton(ffm0, text='Return Loss to VSWR', variable=self.vswr_var, value=False, command=self.toggle_entry)

        # Arrange widgets using grid
        self.vswr_radio.grid(row=0, column=0, sticky='w')
        self.vswr_label.grid(row=5, column=0, sticky='w')
        self.vswr_entry.grid(row=6, column=0, padx=5, pady=5)
        self.return_loss_radio.grid(row=2, column=0, sticky='w')
        self.return_loss_label.grid(row=7, column=0, sticky='w')
        self.return_loss_entry.grid(row=8, column=0, padx=5, pady=5)
        self.calculate_button.grid(row=4, column=0, columnspan=2, pady=5)
        self.result_label.grid(row=5, column=0, columnspan=2)

        # Set the column configuration for alignment
        ffm0.grid_columnconfigure(0, weight=1)
        ffm0.grid_columnconfigure(1, weight=1)

        # Initialize the entry state
        self.toggle_entry()

    def toggle_entry(self):
        if self.vswr_var.get():
            self.vswr_entry.configure(state='normal')
            self.return_loss_entry.configure(state='disabled')
        else:
            self.vswr_entry.configure(state='disabled')
            self.return_loss_entry.configure(state='normal')

    def calculate(self):
        try:
            if self.vswr_var.get():
                vswr = float(self.vswr_entry.get())
                if vswr <= 1:
                    raise ValueError('VSWR must be greater than 1.')
                result = self.vswr_to_return_loss(vswr)
                self.result_label.config(text=f'Return Loss: {result:.2f} dB')
                self.lb.insert(END, f'Return Loss: {result:.2f} dB')
                mem.sto(self.lb.get(0,tk.END))
             
            else:
                return_loss = float(self.return_loss_entry.get())
                result = self.return_loss_to_vswr(return_loss)
                self.result_label.config(text=f'VSWR: {result:.2f}')
                self.lb.insert(END,f'VSWR: {result:.2f}')
                mem.sto(self.lb.get(0,tk.END))  
        except ValueError as e:
            self.result_label.config(text=f'Error: {e}')

    def vswr_to_return_loss(self, vswr):
        return -20 * math.log10((vswr - 1) / (vswr + 1))

    def return_loss_to_vswr(self, return_loss):
        return (1 + pow(10, return_loss / 20)) / (1 - pow(10, return_loss / 20))

SPEED_OF_LIGHT = 299792458  # Speed of light in meters per second

def freqency_wavelength(ffm1):
    def clear_lists():
        frequency_listbox.delete(0, END)
        unit_listbox.delete(0, END)

    def calculate_frequency(freq_value, unit):
       

        try:
            freq_value = float(freq_value)
            multiplier = FREQ.get(unit, 1)
            frequency = freq_value * multiplier
            convert_to_meters(frequency)
        except ValueError:
            print('Invalid frequency value')

    def convert_to_meters(frequency):
        wavelength_meters = SPEED_OF_LIGHT / frequency
        wavelength_feet = wavelength_meters * 3.28084
        frequency_listbox.insert(2, wavelength_meters)
        frequency_listbox.insert(3, wavelength_feet)
        unit_listbox.insert(2, 'm  Meters')
        unit_listbox.insert(3, 'ft  Feet')
        frequency_listbox.insert(1, frequency)
        unit_listbox.insert(1, 'Hz')
        mem.sto(wavelength_meters)
        mem.sto(wavelength_feet)
        mem.sto(frequency)

    # UI Elements
    frequency_label = tk.Label(ffm1, text='Frequency', font=('Arial', 12))
    frequency_label.grid(row=0, column=2)

    unit_label = tk.Label(ffm1, text='in', font=('Arial', 12))
    unit_label.grid(row=0, column=3)

    frequency_entry = tk.Entry(ffm1, bd=9, bg='cyan', font=('Arial', 8))
    frequency_entry.grid(row=1, column=2)

    unit_options = ['THz', 'GHz', 'MHz', 'kHz', 'Hz', 'mHz']
    unit_combobox = ttk.Combobox(ffm1, values=unit_options, font=('Arial', 8))
    unit_combobox.grid(row=1, column=3)
    unit_combobox.set('MHz')    

    frequency_listbox = tk.Listbox(ffm1, bd=10, bg='seashell')
    frequency_listbox.grid(row=10, column=2)

    unit_listbox = tk.Listbox(ffm1, bd=10, bg='snow')
    unit_listbox.grid(row=10, column=3)

    calculate_button = tk.Button(ffm1, text='Calculate', bg='orange', font=('Arial Black', 12), 
                                 command=lambda: calculate_frequency(frequency_entry.get(), unit_combobox.get()))
    calculate_button.grid(row=7, column=3)

    clear_button = tk.Button(ffm1, text='Clear', command=clear_lists)
    clear_button.grid(row=6, column=0)


def attenuator_calculator(ffm2):
    def calculate_attenuator_values():
        try:
            Rin = float(Rin_entry.get())
            Rout = float(Rout_entry.get())
            attenuation_dB = float(attenuation_entry.get())

            if Rin <= 0 or Rout <= 0:
                raise ValueError('Resistances must be greater than zero.')

            k = 10 ** (attenuation_dB / 10)
            
            # Tee Attenuator
            R1_Tee = Rin * (k - 1) / (k + 1)
            R2_Tee = Rout * (k - 1) / (k + 1)
            R3_Tee = (Rin * Rout * (k + 1)) / (Rin + Rout)

            # Pi Attenuator
            R1_Pi = (Rin * (k - 1)) / (k + 1)
            R2_Pi = (Rout * (k - 1)) / (k + 1)
            R3_Pi = (Rin + Rout) / (Rin * Rout * (k + 1))

            tee_result.set(f'R1: {R1_Tee:.2f} Ohm, R2: {R2_Tee:.2f} Ohm, R3: {R3_Tee:.2f} Ohm')
            pi_result.set(f'R1: {R1_Pi:.2f} Ohm, R2: {R2_Pi:.2f} Ohm, R3: {R3_Pi:.2f} Ohm')
            mem.sto(f'R1: {R1_Tee:.2f} Ohm, R2: {R2_Tee:.2f} Ohm, R3: {R3_Tee:.2f} Ohm')
            mem.sto(f'R1: {R1_Pi:.2f} Ohm, R2: {R2_Pi:.2f} Ohm, R3: {R3_Pi:.2f} Ohm')
            
            error_message.set('')
        except ValueError as e:
            error_message.set(str(e))
            tee_result.set('')
            pi_result.set('')


  

    # Create and place widgets
    tk.Label(ffm2, text='Input Resistance (Rin) in Ohms:').grid(row=0, column=0)
    Rin_entry = tk.Entry(ffm2)
    Rin_entry.grid(row=0, column=1)

    tk.Label(ffm2, text='Output Resistance (Rout) in Ohms:').grid(row=1, column=0)
    Rout_entry = tk.Entry(ffm2)
    Rout_entry.grid(row=1, column=1)

    tk.Label(ffm2, text='Attenuation in dB:').grid(row=2, column=0)
    attenuation_entry = tk.Entry(ffm2)
    attenuation_entry.grid(row=2, column=1)

    calculate_button = tk.Button(ffm2, text='Calculate', command=calculate_attenuator_values)
    calculate_button.grid(row=3, column=0, columnspan=2)

    error_message = tk.StringVar()
    tee_result = tk.StringVar()
    pi_result = tk.StringVar()

    tk.Label(ffm2, textvariable=error_message, fg='red').grid(row=4, column=0, columnspan=2)
    tk.Label(ffm2, text='Tee Attenuator Values:').grid(row=5, column=0)
    tk.Label(ffm2, textvariable=tee_result).grid(row=5, column=1)

    tk.Label(ffm2, text='Pi Attenuator Values:').grid(row=6, column=0)
    tk.Label(ffm2, textvariable=pi_result).grid(row=6, column=1)

   

# Run the attenuator calculator app




def rf_pwr_converter(ffm3):
    def clear_lists():
        lbox1.delete(0, END)
        lbox2.delete(0, END)
    
    def dBm_to_watts(dBm):
        watts = 10 ** (float(dBm) / 10) / 1000
        return watts

    def volts_rms(watts):
        return (watts * 0.2236, watts * 0.2236 * 1.414, watts * 0.2236 * 1.414 * 2)

    def convert_dBm_to_watts():
        dBm = num1.get()
        watts = dBm_to_watts(dBm)
        rms, peak, pkpk = volts_rms(watts)
        display_results(dBm, watts, rms, peak, pkpk)

    def watts_to_dBm(watts):
        return 10 * math.log10(watts * 1000)

    def convert_watts_to_dBm():
        watts = float(e4.get()) if eng.get() == 'mW' else float(e4.get()) * 1000
        dBm = watts_to_dBm(watts)
        rms, peak, pkpk = volts_rms(watts)
        display_results(dBm, watts, rms, peak, pkpk)

    def display_results(dBm, watts, rms, peak, pkpk):
        lbox1.insert(END, dBm)
        lbox1.insert(END, watts)
        lbox1.insert(END, rms)
        lbox1.insert(END, peak)
        lbox1.insert(END, pkpk)
        lbox2.insert(END, 'dBm')
        lbox2.insert(END, 'W')
        lbox2.insert(END, 'Volts RMS')
        lbox2.insert(END, 'Volts Peak')
        lbox2.insert(END, 'Volts PK-PK')
        mem.sto(lbox1.get(0, tk.END))
        mem.sto(lbox2.get(0, tk.END))
    # UI Setup
    num1 = tk.StringVar()
    e3 = tk.Entry(ffm3, textvariable=num1, bd=7, bg='cornsilk', justify='right', font=('Arial', 8))
    e3.grid(row=0, column=2)
    e3.focus()

    e4 = tk.Entry(ffm3, bg='azure', bd=7, justify='right', font=('Arial', 8))
    e4.grid(row=8, column=1)

    tk.Label(ffm3, text='dBm', justify='left', font=('Arial', 8)).grid(row=0, column=3)
    btn2 = tk.Button(ffm3, text='Convert to Watts', command=convert_dBm_to_watts)
    btn2.grid(column=1, row=1)

    eng = ttk.Combobox(ffm3, values=['mW', 'W'])
    eng.grid(row=8, column=3)
    eng.set('mW')

    btn4 = tk.Button(ffm3, text='Convert to dBm', command=convert_watts_to_dBm)
    btn4.grid(column=1, row=10)

    btn3 = tk.Button(ffm3, text='Clear', command=clear_lists)
    btn3.grid(row=7, column=1)

    lbox1 = tk.Listbox(ffm3, bd=6)
    lbox1.grid(column=2, row=3)

    lbox2 = tk.Listbox(ffm3, bd=6)
    lbox2.grid(column=3, row=3)

    tk.Label(ffm3, text='dBm to Watts, Voltage pkpk, rms', font=('Arial', 8)).grid(row=0, column=7)

class InductanceCalculator:
    def __init__(self, parent):
        self.parent= parent
        tk.Label(self.parent, text ='Air Core Inductor Calculator').grid(row=0,column=1)

        # Initialize GUI components
        tk.Label(parent, text='Number of Turns (N):').grid(row=2, column=1)
        self.number_of_turns_entry = tk.Entry(parent)
        self.number_of_turns_entry.grid(row=2, column=2)

        tk.Label(parent, text='Coil Radius:').grid(row=4, column=1)
        self.coil_radius_entry = tk.Entry(parent)
        self.coil_radius_entry.grid(row=7, column=1)
        self.radius_unit = tk.StringVar(value='inches')
        tk.Radiobutton(parent, text='Inches', variable=self.radius_unit, value='inches').grid(row=8, column=2)
        tk.Radiobutton(parent, text='Feet', variable=self.radius_unit, value='feet').grid(row=9, column=3)

        tk.Label(parent, text='Coil Length:').grid(row=10, column=1)
        self.coil_length_entry = tk.Entry(parent)
        self.coil_length_entry.grid(row=12, column=1)
        self.length_unit = tk.StringVar(value='inches')
        tk.Radiobutton(parent, text='Inches', variable=self.length_unit, value='inches').grid(row=12, column=2)
        tk.Radiobutton(parent, text='Feet', variable=self.length_unit, value='feet').grid(row=12, column=3)

        self.inductance_result = tk.StringVar()
        tk.Label(parent, text='Inductance (H):').grid(row=14, column=1)
        tk.Label(parent, textvariable=self.inductance_result).grid(row=14, column=1)

        calculate_button = tk.Button(parent, text='Calculate Inductance', command=self.calculate_inductance)
        calculate_button.grid(row=15, column=1, columnspan=4)

    def calculate_inductance(self):
        try:
            N = int(self.number_of_turns_entry.get())
            mem.sto(N)
            r = float(self.coil_radius_entry.get()) * (0.0254 if self.radius_unit.get() == 'inches' else 0.3048)
            mem.sto(r)
            l = float(self.coil_length_entry.get()) * (0.0254 if self.length_unit.get() == 'inches' else 0.3048)
            mem.sto(l)
            mu_0 = 4 * math.pi * 1e-7

            L = (mu_0 * N**2 * math.pi * r**2) / l
            mem.sto(L)
            self.inductance_result.set(f'{L:.6e} H')
            mem.sto(f'{L:.6e} H')
        except ValueError:
            self.inductance_result.set('Invalid input')


class PPM:
    def __init__(self, root):
        self.frequency_label = tk.Label(ffm5, text='Frequency', font=('Arial', 12))
        self.frequency_label.grid(row=0, column=2)
        self.frequency_label2 = tk.Label(ffm5, text='Frequency', font=('Arial', 12))
        self.frequency_label2.grid(row=4, column=2)
        self.ppm_label = tk.Label(ffm5, text='PPM', font=('Arial', 12))
        self.ppm_label.grid(row=7, column=2)

        self.unit_label = tk.Label(ffm5, text='', font=('Arial', 12))
        self.unit_label.grid(row=0, column=3)

        self.frequency_entry = tk.Entry(ffm5, bd=9, bg='cyan', font=('Arial', 8))
        self.frequency_entry.grid(row=1, column=2)
        self.frequency_entry2 = tk.Entry(ffm5, bd=9, bg='cyan', font=('Arial', 8))
        self.frequency_entry2.grid(row=5, column=2)
        self.ppm_entry = tk.Entry(ffm5, bd=9, bg='cyan', font=('Arial', 8))
        self.ppm_entry.grid(row=8, column=2)
        self.unit_options = ['THz', 'GHz', 'MHz', 'kHz', 'Hz', 'mHz']
        self.unit_combobox = ttk.Combobox(ffm5, values=self.unit_options, font=('Arial', 8))
        self.unit_combobox.grid(row=1, column=3)
        self.unit_combobox.set('MHz')    
        self.unit_combobox2 = ttk.Combobox(ffm5, values=self.unit_options, font=('Arial', 8))
        self.unit_combobox2.grid(row=5, column=3)
        self.unit_combobox2.set('MHz')    
        self.btn1 = tk.Button(ffm5, text='Convert to PPM', command=None)
        self.btn1.grid(row=19, column=0)
        self.clear_button = tk.Button(ffm5, text='Clear', command=self.clear_lists)
        self.clear_button.grid(row=19, column=1)
        self.btn2 = tk.Button(ffm5, text='Convert ton Freq', command=None)
        self.btn2.grid(row=19, column=2)

        self.lbox1 = tk.Listbox(ffm5, bd=6)
        self.lbox1.grid(row=16, column=3)

        self.lbox2 = tk.Listbox(ffm5, bd=6)
        self.lbox2.grid(row=16, column=4)



    

        self.btn1.config(command=self.convert_to_ppm)
        self.btn2.config(command=self.convert_to_frequency)
    
    def clear_lists(self):
        self.lbox1.delete(0, tk.END)
        self.lbox2.delete(0, tk.END)

    def convert_to_ppm(self):
        try:
            # Get frequency values from entries
            f1 = float(self.frequency_entry.get())
            f2 = float(self.frequency_entry2.get())

            # Convert frequencies to Hz based on selected unit
            f1_in_hz = self.convert_to_hz(f1, self.unit_combobox.get())
            f2_in_hz = self.convert_to_hz(f2, self.unit_combobox2.get())

            # Calculate PPM
            ppm = ((f2_in_hz - f1_in_hz) / f1_in_hz) * 1e6

            # Display result in the listbox
            self.lbox1.insert(tk.END, f"PPM: {ppm:.2f}")
        except ValueError:
            self.lbox1.insert(tk.END, "Invalid input! Please enter valid numbers.")

    def convert_to_frequency(self):
        try:
            # Get PPM and reference frequency
            ppm = float(self.ppm_entry.get())
            f1 = float(self.frequency_entry.get())

            # Convert frequency to Hz
            f1_in_hz = self.convert_to_hz(f1, self.unit_combobox.get())

            # Calculate the measured frequency in Hz
            f2_in_hz = f1_in_hz * (1 + ppm / 1e6)

            # Display the result in Hz regardless of the selected unit
            self.lbox2.insert(tk.END, f"Frequency: {f2_in_hz:.2f} Hz")
        except ValueError:
            self.lbox2.insert(tk.END, "Invalid input! Please enter valid numbers.")


    def convert_to_hz(self, frequency, unit):
        # Convert given frequency to Hz
        unit_multipliers = {
            'THz': 1e12,
            'GHz': 1e9,
            'MHz': 1e6,
            'kHz': 1e3,
            'Hz': 1,
            'mHz': 1e-3
        }
        return frequency * unit_multipliers[unit]

    def convert_from_hz(self, frequency_hz, unit):
        # Convert Hz back to the selected unit
        unit_multipliers = {
            'THz': 1e12,
            'GHz': 1e9,
            'MHz': 1e6,
            'kHz': 1e3,
            'Hz': 1,
            'mHz': 1e-3
        }
        return frequency_hz / unit_multipliers[unit]
class Intermod:
    def __init__(self, root):
        self.root = root
        tk.Label(self.root, text="IP3 Linear (Watts):").grid(row=0, column=0)
        self.ip3_linear_entry = tk.Entry(self.root)
        self.ip3_linear_entry.grid(row=0, column=1)
        self.ip3_dbm_result = tk.StringVar()
        tk.Label(self.root, text="IP3 (dBm):").grid(row=1, column=0)
        tk.Label(self.root, textvariable=self.ip3_dbm_result).grid(row=1, column=1)
        convert_button = tk.Button(self.root, text="Convert to dBm", command=self.calculate_ip3_dbm)
        convert_button.grid(row=2, column=0, columnspan=2)

        # Cascaded IP3 Calculation
        tk.Label(self.root, text="Input IP3 (dBm):").grid(row=3, column=0)
        self.ip3_input_entry = tk.Entry(self.root)
        self.ip3_input_entry.grid(row=3, column=1)
        tk.Label(self.root, text="Gain (dB):").grid(row=4, column=0)
        self.gain_entry = tk.Entry(self.root)
        self.gain_entry.grid(row=4, column=1)
        self.cascaded_ip3_result = tk.StringVar()
        tk.Label(self.root, text="Output IP3 (dBm):").grid(row=5, column=0)
        tk.Label(self.root, textvariable=self.cascaded_ip3_result).grid(row=5, column=1)
        calculate_cascaded_button = tk.Button(self.root, text="Calculate Cascaded IP3", command=self.calculate_cascaded_ip3)
        calculate_cascaded_button.grid(row=6, column=0, columnspan=2)

        # 1 dB Compression Point (P1dB) Calculation
        tk.Label(self.root, text="Input Power (dBm):").grid(row=7, column=0)
        self.input_power_entry = tk.Entry(self.root)
        self.input_power_entry.grid(row=7, column=1)
        self.p1db_result = tk.StringVar()
        tk.Label(self.root, text="P1dB (dBm):").grid(row=8, column=0)
        tk.Label(self.root, textvariable=self.p1db_result).grid(row=8, column=1)
        calculate_p1db_button = tk.Button(self.root, text="Calculate P1dB", command=self.calculate_p1db)
        calculate_p1db_button.grid(row=9, column=0, columnspan=2)

        # IP2 Calculation
        tk.Label(self.root, text="Input IP2 (dBm):").grid(row=10, column=0)
        self.ip2_input_entry = tk.Entry(self.root)
        self.ip2_input_entry.grid(row=10, column=1)
        self.ip2_result = tk.StringVar()
        tk.Label(self.root, text="Output IP2 (dBm):").grid(row=11, column=0)
        tk.Label(self.root, textvariable=self.ip2_result).grid(row=11, column=1)
        calculate_ip2_button = tk.Button(self.root, text="Calculate IP2", command=self.calculate_ip2)
        calculate_ip2_button.grid(row=12, column=0, columnspan=2)

    def calculate_ip3_dbm(self):
        try:
            ip3_linear = float(self.ip3_linear_entry.get())
            ip3_dbm = 10 * math.log10(ip3_linear)
            self.ip3_dbm_result.set(f"{ip3_dbm:.2f} dBm")
        except ValueError:
            self.ip3_dbm_result.set("Invalid input")

    def calculate_cascaded_ip3(self):
        try:
            ip3_input = float(self.ip3_input_entry.get())
            gain = float(self.gain_entry.get())
            ip3_output = ip3_input + gain
            self.cascaded_ip3_result.set(f"{ip3_output:.2f} dBm")
        except ValueError:
            self.cascaded_ip3_result.set("Invalid input")

    def calculate_p1db(self):
        try:
            input_power = float(self.input_power_entry.get())
            gain = float(self.gain_entry.get())
            p1db = input_power + gain - 1  # 1dB compression
            self.p1db_result.set(f"{p1db:.2f} dBm")
        except ValueError:
            self.p1db_result.set("Invalid input")

    def calculate_ip2(self):
        try:
            ip2_input = float(self.ip2_input_entry.get())
            gain = float(self.gain_entry.get())
            ip2_output = ip2_input + 2 * gain  # For IP2, the gain adds twice
            self.ip2_result.set(f"{ip2_output:.2f} dBm")
        except ValueError:
            self.ip2_result.set("Invalid input")

nb002.add(ffm0, text='Retrun Loss & VSWR')
nb002.add(ffm1, text='Frequency Wavelength')
nb002.add(ffm2, text='Attenuator Calculation')
nb002.add(ffm3, text = 'dBm & Watts')
nb002.add(ffm4, text ='air coil Inductor calc')
nb002.add(ffm5, text ='PPM')
nb002.add(ffm6, text ='IP3_IP2_dBm')

vswr = Vswr(ffm0)
freqency_wavelength(ffm1)
attenuator_calculator(ffm2)
rf_pwr_converter(ffm3)
coil_calc = InductanceCalculator(ffm4)
ppm = PPM(ffm5)
ip3 = Intermod(ffm6)
class ResonantCalcTab:
    def __init__(self, parent, title, units1, units2, label1, label2, calc_method):
        self.frame = ttk.Frame(parent)
        parent.add(self.frame, text=title)

        # Unit selection
        self.unit1 = ttk.Combobox(self.frame, values=units1, font=('Arial', 14))
        self.unit1.set(units1[0])  # Default value
        self.unit1.grid(row=1, column=3)

        self.unit2 = ttk.Combobox(self.frame, values=units2, font=('Arial', 14))
        self.unit2.set(units2[0])  # Default value
        self.unit2.grid(row=4, column=3)

        # Labels and Entries
        tk.Label(self.frame, text=label1, font=('Arial', 14)).grid(row=0, column=2)
        self.entry1 = tk.Entry(self.frame, bg='yellow', font=('Arial', 14))
        self.entry1.grid(row=1, column=2)

        tk.Label(self.frame, text=label2, font=('Arial', 14)).grid(row=3, column=2)
        self.entry2 = tk.Entry(self.frame, bg='light blue', font=('Arial', 14))
        self.entry2.grid(row=4, column=2)

        # Calculate button
        self.calc_button = tk.Button(self.frame, text='Calculate>>', bg='orange', font=('Arial Black', 12),
                                     command=lambda: calc_method(self.entry1.get(), self.entry2.get(),
                                                                 self.unit1.get(), self.unit2.get()))
        self.calc_button.grid(row=5, column=5)

        # Listboxes for results
        self.lb5 = tk.Listbox(self.frame, width=40)
        self.lb5.grid(row=16, column=4)
        self.lb6 = tk.Listbox(self.frame, width=40)
        mem.sto(self.lb5.get(0,tk.END))
        mem.sto(self.lb6.get(0,tk.END))        
class CapacitanceTab(ResonantCalcTab):
    def __init__(self, parent):
        super().__init__(parent, 'find capacitance', ['Hz', 'kHz', 'MHz', 'GHz', 'THz'], 
                         [' ', 'm', 'u', 'n', 'p'], 'Frequency Value', 'Inductance Value', self.cap_calc)
    def cap_calc(self, freq_val, ind_val, freq_unit, ind_unit):
        # Convert frequency to Hertz
        freq_multiplier = {'Hz': 1, 'kHz': 1e3, 'MHz': 1e6, 'GHz': 1e9, 'THz': 1e12}
        freq_in_hz = float(freq_val) * freq_multiplier[freq_unit]

        # Convert inductance to Henries
        ind_multiplier = {' ': 1, 'm': 1e-3, 'u': 1e-6, 'n': 1e-9, 'p': 1e-12}
        ind_in_henries = float(ind_val) * ind_multiplier[ind_unit]

        # Calculate capacitance in Farads
        if freq_in_hz != 0 and ind_in_henries != 0:
            capacitance = 1 / ((2 * math.pi * freq_in_hz)**2 * ind_in_henries)
        else:
            capacitance = 0

        # Present the results in various units
        self.lb5.delete(0, tk.END)  # Clear previous results
        self.lb6.delete(0, tk.END)  # Clear previous results

        self.lb5.insert(tk.END, f'{capacitance} F')  # Farad
        self.lb6.insert(tk.END, 'Farad (F)')

        self.lb5.insert(tk.END, f'{capacitance * 1e3} mF')  # Millifarad
        self.lb6.insert(tk.END, 'Millifarad (mF)')

        self.lb5.insert(tk.END, f'{capacitance * 1e6} uF')  # Microfarad
        self.lb6.insert(tk.END, 'Microfarad (uF)')

        self.lb5.insert(tk.END, f'{capacitance * 1e9} nF')  # Nanofarad
        self.lb6.insert(tk.END, 'Nanofarad (nF)')

        self.lb5.insert(tk.END, f'{capacitance * 1e12} pF')  # Picofarad
        self.lb6.insert(tk.END, 'Picofarad (pF)')
        mem.sto(self.lb5.get(0,tk.END))
        mem.sto(self.lb6.get(0,tk.END))        

class InductanceTab(ResonantCalcTab):
    def __init__(self, parent):
        super().__init__(parent, 'find inductance', ['Hz', 'kHz', 'MHz', 'GHz', 'THz'], 
                         [' ', 'm', 'u', 'n', 'p'], 'Frequency Value', 'Capacitance Value', self.ind_calc)

   
    def ind_calc(self, freq_val, cap_val, freq_unit, cap_unit):
        # Convert frequency to Hertz
        freq_multiplier = {'Hz': 1, 'kHz': 1e3, 'MHz': 1e6, 'GHz': 1e9, 'THz': 1e12}
        freq_in_hz = float(freq_val) * freq_multiplier[freq_unit]

        # Convert capacitance to Farads
        cap_multiplier = {' ': 1, 'm': 1e-3, 'u': 1e-6, 'n': 1e-9, 'p': 1e-12}
        cap_in_farads = float(cap_val) * cap_multiplier[cap_unit]

        # Calculate inductance in Henrys
        if freq_in_hz != 0 and cap_in_farads != 0:
            inductance = 1 / ((2 * math.pi * freq_in_hz)**2 * cap_in_farads)
        else:
            inductance = 0

        # Present the results in various units
        self.lb5.delete(0, tk.END)  # Clear previous results
        self.lb6.delete(0, tk.END)  # Clear previous results

        self.lb5.insert(tk.END, f'{inductance} H')  # Henry
        self.lb6.insert(tk.END, 'Henry (H)')

        self.lb5.insert(tk.END, f'{inductance * 1e3} mH')  # Millihenry
        self.lb6.insert(tk.END, 'Millihenry (mH)')

        self.lb5.insert(tk.END, f'{inductance * 1e6} uH')  # Microhenry
        self.lb6.insert(tk.END, 'Microhenry (uH)')      # Calculation logic here
        mem.sto(self.lb5.get(0,tk.END))
        mem.sto(self.lb6.get(0,tk.END))        



class FrequencyTab(ResonantCalcTab):
    def __init__(self, parent):
        super().__init__(parent, 'find frequency', [' ', 'm', 'u', 'n', 'p'], [' ', 'm', 'u', 'n', 'p'],
                         'Inductance Value', 'Capacitance Value', self.freq_calc)
    def freq_calc(self, ind_val, cap_val, ind_unit, cap_unit):
        # Convert inductance to Henries
        ind_multiplier = {' ': 1, 'm': 1e-3, 'u': 1e-6, 'n': 1e-9, 'p': 1e-12}
        ind_in_henries = float(ind_val) * ind_multiplier[ind_unit]

        # Convert capacitance to Farads
        cap_multiplier = {' ': 1, 'm': 1e-3, 'u': 1e-6, 'n': 1e-9, 'p': 1e-12}
        cap_in_farads = float(cap_val) * cap_multiplier[cap_unit]

        # Calculate frequency in Hertz
        if ind_in_henries != 0 and cap_in_farads != 0:
            frequency = 1 / (2 * math.pi * math.sqrt(ind_in_henries * cap_in_farads))
        else:
            frequency = 0

        # Present the results in various units
        self.lb5.delete(0, tk.END)  # Clear previous results
        self.lb6.delete(0, tk.END)  # Clear previous results

        self.lb5.insert(tk.END, f'{frequency} Hz')  # Hertz
        self.lb6.insert(tk.END, 'Hertz (Hz)')

        self.lb5.insert(tk.END, f'{frequency / 1e3} kHz')  # Kilohertz
        self.lb6.insert(tk.END, 'Kilohertz (kHz)')

        self.lb5.insert(tk.END, f'{frequency / 1e6} MHz')  # Megahertz
        self.lb6.insert(tk.END, 'Megahertz (MHz)')

        self.lb5.insert(tk.END, f'{frequency / 1e9} GHz')  # Gigahertz
        self.lb6.insert(tk.END, 'Gigahertz (GHz)')

 


nb003 = ttk.Notebook(tab.f4)
nb003.grid(row=1, column=0)

# Create each tab
cap_tab = CapacitanceTab(nb003)
ind_tab = InductanceTab(nb003)
freq_tab = FrequencyTab(nb003)

########################################
# SCIENTIFIC GUI BUTTON CALCULATOR
#########################################

def scientific_calculator():
    #code start for calculator which has 1470 lines of code
    answer_ee2 = 0
    cc_complete = 0
    #build frames to place entry
    frm1 = ttk.Frame(tab.f5, height=20, width=200)
    frm1.grid(row=0, column=1, columnspan=2)
    frm1.columnconfigure(0, weight=4)
    frm1.columnconfigure(1, weight=5)
    frm2 = ttk.Frame(tab.f5, height=300, width=600)
    frm2.grid(row=5, column=0, columnspan=2)     
    frm3 = ttk.Frame(tab.f5, height=100, width=600)
    frm3.grid(row=25, column=0, columnspan=2)
    tk.Label(frm3,text='Memory Storage').grid(row=26, column=0)
    lb = tk.Listbox(frm3)
    lb.grid(row=27, column=0)
    frm3.columnconfigure(0, weight=8)
    frm3.columnconfigure(1, weight=6)
    tk.Label(frm1, text='Entry 1').grid(row=0, column=0)
    tk.Label(frm1, text='Entry 2').grid(row=0, column=1)
    tk.Label(frm1, text='Entry 3').grid(row=0, column=2)
    tk.Label(frm1, text='Entry 4').grid(row=0, column=3)
    tk.Label(frm1, text='Answer from Entry 3&4').grid(row=2, column=3)
    tk.Label(frm1, text='Answer from Answer 1&2').grid(row=2, column=5)
    e1 = tk.Entry(frm1, bd=9, bg= 'wheat')
    e1.grid(row=1, column=0, padx=20, sticky='w')
    e2 = tk.Entry(frm1, bd=9, bg= 'light blue')
    e2.grid(row=1, column=1, padx=20, sticky='w')
    e3 = tk.Entry(frm1, bd=7, bg= 'light green')
    e3.grid(row=1, column=2, padx=20, sticky='w')
    e4 = tk.Entry(frm1, bd=7, bg= 'light pink')
    e4.grid(row=1, column=3, padx=20, sticky='w')
    e5 = tk.Entry(frm1,bd=5,bg= 'light pink')
    e5.grid(row=3, column=3, padx=20, sticky='w')
    tk.Label(frm1, text='Answer from Entry 1&2').grid(row=2, column=1)
    e6 = tk.Entry(frm1,bd=5, bg= 'wheat')
    e6.grid(row=3, column=1)
    e7 = tk.Entry(frm1, bd=5, bg= 'light pink')
    e7.grid(row=3, column=5, padx=20, sticky='w')
   
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
            


        eqbtn1 = tk.Button(frm1, text='  =  ', bd=5, bg= 'AntiqueWhite2', font=('URW Chancery L',15,'bold'), command=eq)
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
            tk.Label(frm1, text='-----answer------').grid(row=4, column=3)

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
            tk.Label(frm1, text='-----answer------').grid(row=4, column=1)
            return  e6.insert(END, answer)
            


        eqbtn1 = tk.Button(frm1, text='  =  ', bd=5, bg= 'AntiqueWhite2', font=('URW Chancery L',15,'bold'), command=eq)
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
                tk.Label(frm1, text='-----answer------').grid(row=4, column=3)
                
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
                tk.Label(frm1, text='-----answer------').grid(row=4, column=1)
                return  e6.insert(END, answer)
            
            
        eqbtn1 = tk.Button(frm1, text='  =  ', bd=5, bg='AntiqueWhite2', font=('URW Chancery L',15,'bold'), command=eq)
        eqbtn1.grid(row=3, column=0)
    def div():
        if not len(e4.get()) == 0:
            if not len(e3.get()) == 0:
                ee4 = float(e4.get())
                mem.sto(ee4)
                lb.insert(1, e4.get())
                e4.delete(0, END)
                ee3 = float(e3.get())
                mem.sto = ee3
                if ee3 == 0:
                    e5.insert(0, 'undefined')
                    tk.Label(frm1, text='   ----no answer----  ').grid(row=4, column=1)
                else:    
                    ee5 = float(ee4) / float(ee3)
                    e5.insert(END, float(ee5))
                    mem.sto(ee5)
                    tk.Label(frm1, text='   ----answer----  ').grid(row=4, column=1)
                    e3.delete(0, END)
        
        if not len(e2.get()) == 0:
            e3.insert(END, float(e2.get()))
            e2.delete(0, END)
            mem.sto(e2.get())
        if not len(e1.get()) == 0:    
            ee1 = float(e1.get())
            e2.insert(END, float(ee1))
            ee2 = float(e2.get())
            e1.delete(0, END)
            mem.sto(ee2)
            
           
       
        
        def eq():
            if not len(e6.get()) == 0:
                if not len(e5.get()) == 0:
                           ee5 = float(e5.get())
                           mem.sto(ee5)
                           ee6 = float(e6.get())
                           mem.sto(ee6)
                           if ee5 == 0:
                               e7.insert(END, 'Undefined')
                           else:
                               
                               ee7 = float(ee6) / float(ee5)
                               mem.sto(ee7)
                               e7.insert(END, float(ee7))
                                              
            elif not len(e1.get()) == 0:    
                e6.delete(0, END)
                ee1 = float(e1.get())
                ee2 = float(e2.get())
                mem.sto(ee1)
                mem.sto(ee2)
              
           
            if ee1 == 0:
                e6.insert(END, 'Undefined')
                tk.Label(frm1, text='-Infinite-').grid(row=4, column=1)
                tk.Label(frm1, text='---Value--').grid(row=5, column=1)
            else:    
                
                ans = float(ee2) / float(ee1)
                tk.Label(frm1, text='-----answer------').grid(row=4, column=1)
                
                return  e6.insert(END, float(ans))
        
            

        eqbtn1 = tk.Button(frm1, text='  =  ', bd=7, bg= 'AntiqueWhite3', font=('URW Chancery L',15,'bold'), command=eq)
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
        tk.Label(frm1, text='                           ').grid(row=2, column=0)
        tk.Label(frm1, text='                           ').grid(row=4, column=1)
        tk.Label(frm1, text='                           ').grid(row=4, column=3)
        tk.Label(frm1, text='                           ').grid(row=5, column=1)
        tk.Label(frm1, text='                           ').grid(row=5, column=3)
        tk.Label(frm1, text='                           ').grid(row=5, column=5)
        tk.Label(frm1, text='                           ').grid(row=4, column=5)

    def clear1():
        e1.delete(0, END)
        tk.Label(frm1, text='                           ').grid(row=4, column=1)
        tk.Label(frm1, text='                        ').grid(row=5, column=1)



    def clear2():
        e2.delete(0, END)
        tk.Label(frm1, text='                           ').grid(row=4, column=1)
        tk.Label(frm1, text='                           ').grid(row=4, column=1)
        tk.Label(frm1, text='                           ').grid(row=4, column=3)
        tk.Label(frm1, text='                           ').grid(row=5, column=1)
        tk.Label(frm1, text='                           ').grid(row=5, column=3)
        tk.Label(frm1, text='                           ').grid(row=5, column=5)
        tk.Label(frm1, text='                           ').grid(row=4, column=5)

    def clear3():
        e3.delete(0, END)
        tk.Label(frm1, text='                           ').grid(row=4, column=1)
         
    def clear4():
        e4.delete(0, END)
        tk.Label(frm1, text='                           ').grid(row=4, column=1)

    def clear6():
        e6.delete(0, END)
        tk.Label(frm1, text='                           ').grid(row=4, column=1)
        tk.Label(frm1, text='                           ').grid(row=4, column=3)
        tk.Label(frm1, text='                           ').grid(row=5, column=1)
        tk.Label(frm1, text='                           ').grid(row=5, column=3)
        tk.Label(frm1, text='                           ').grid(row=5, column=5)
        tk.Label(frm1, text='                           ').grid(row=4, column=5)       

    def clrmem():
        lb.delete(0, END)
        tk.Label(frm1, text='                           ').grid(row=4, column=1)
        tk.Label(frm1, text='                           ').grid(row=4, column=3)
        tk.Label(frm1, text='                           ').grid(row=5, column=1)
        tk.Label(frm1, text='                           ').grid(row=5, column=3)
        tk.Label(frm1, text='                           ').grid(row=5, column=5)
        tk.Label(frm1, text='                           ').grid(row=4, column=5)

    def recall_mem(event=None):
        try:
            mc = lb.curselection()[0]
            ee5 = lb.get(mc)
            e1.insert(END, ee5)
            mem.sto(ee5)
        except Exception as ex:
            tk.Label(frm1, text='nothing selected').grid(row=4, column=1)
            print(ex)


    lb.bind('<Double-Button-1>', recall_mem)
    lb.bind('<<ListboxSelect>>', recall_mem)

    def sto1():
        ee1 = e1.get()
        mem.sto(ee1)
        lb.insert(1, ee1)
        e1.delete(0, END)

    def stoans():
        lb.insert(1, e6.get())
        mem.sto(e6.get())
        e6.delete(0, END)


    def shift4():
        ee4 = e4.get()
        lb.insert(END, ee4)
        e4.delete(0, END)

    def to_mem():
        ee1 = e1.get()
        mem.sto(ee1)
        lb.insert(END, ee1)
        
    def shift3():
        ee3 = e3.get()
        mem.sto(ee3)
        e4.insert(END, ee3)
        e3.delete(0, END)
        
    def shift2():
        ee2 = e2.get()
        mem.sto(ee2)
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
            mem.st(ee6)
            e6.delete(0, END)
        def to_ent4():
            e4.delete(0, END)
            e4.insert(END, float(ee6))
            mem.sto(ee6)
            e6.delete(0, END)

        def to_ent5():
            e5.delete(0, END)
            e5.insert(END, float(ee6))
            mem.sto(ee6)
            e6.delete(0, END)
        def to_ent7():
            e7.insert(END, float(ee6))
            mem.sto(ee6)
            e6.delete(0, END)

        def to_ent1():
            e1.delete(0, END)
            e1.insert(END, float(ee6))
            mem.syo(ee6)
            e6.delete(0, END)
        def to_ent2():
            e2.delete(0, END)
            e2.insert(END, float(ee6))
            mem.sto(ee6)
            e6.delete(0, END)     

        btn1= tk.Button(top2, text='move answser to entry 3', command=to_ent3)
        btn1.grid(row=0, column=0)
        btn2= tk.Button(top2, text='move answser to entry 4', command=to_ent4)
        btn2.grid(row=1, column=0)
        btn3= tk.Button(top2, text='move answser to entry 5', command=to_ent5)
        btn3.grid(row=2, column=0)
        btn4= tk.Button(top2, text='move answser to entry 7', command=to_ent7)
        btn4.grid(row=3, column=0)
        btn5= tk.Button(top2, text='move answser to entry 1', command=to_ent1)
        btn5.grid(row=4, column=0)
        btn6= tk.Button(top2, text='move answser to entry 2', command=to_ent2)
        btn6.grid(row=5, column=0)
        
    def shift_mem():
        top3 = Toplevel()
        def to_e1(event=None):
            try:
                mc = lb.curselection()[0]
                ee1 = lb.get(mc)
                mem.sto(ee1)
                e1.delete(0, END)
                e1.insert(END, ee1)
            except Exception as ex:
                tk.Label(frm1, text='nothing selected').grid(row=4, column=1)
                print(ex)

        def to_e2(event=None):
            try:
                mc = lb.curselection()[0]
                ee1 = lb.get(mc)
                mem.sto(ee1)
                e2.delete(0, END)
                e2.insert(END, ee1)
            except Exception as ex:
                tk.Label(frm1, text='nothing selected').grid(row=4, column=1)
                print(ex)    
        def to_e3(event=None):
            try:
                mc = lb.curselection()[0]
                ee1 = lb.get(mc)
                mem.sto(ee1)
                e3.delete(0, END)
                e3.insert(END, ee1)
            except Exception as ex:
                tk.Label(frm1, text='nothing selected').grid(row=4, column=1)
                print(ex)
                
        def to_e4(event=None):
            try:
                mc = lb.curselection()[0]
                ee1 = lb.get(mc)
                mem.sto(ee1)
                e4.delete(0, END)
                e4.insert(END, ee1)
            except Exception as ex:
                tk.Label(frm1, text='nothing selected').grid(row=4, column=1)
                print(ex)            

        btn1= tk.Button(top3, text='memory selection to entry 1', command=to_e1)
        btn1.grid(row=0, column=0)
        btn2= tk.Button(top3, text='memory selection to entry 2', command=to_e2)
        btn2.grid(row=1, column=0)
        btn3= tk.Button(top3, text='memory selection to entry 3', command=to_e3)
        btn3.grid(row=2, column=0)
        btn4= tk.Button(top3, text='memory selection to entry 4', command=to_e4)
        btn4.grid(row=3, column=0)
       
 #####Closure Functions
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
        mem.sto(ee1)
        answer = math.factorial(ee1)
        mem.sto(answer)
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
        mem.sto(ee1)
        e2.insert(END, ee1)
        ee2 = float(e2.get())
        mem.sto(ee2)
        e1.delete(0, END)
        def eq():
             if not len(e6.get()) == 0:
                lb.insert(1, e6.get())
                e6.delete(0, END)
             ee1 = float(e1.get())
             mem.sto(ee1)
             ee2 = float(e2.get())
             mem.sto(ee2)
             answer = math.fmod(ee1, ee2)
             mem.sto(answer)
             
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
        mem.sto(answer)
        e6.insert(END, answer)
         
        return answer

    def point():
        if not len(e1.get()) == 0:
            ee1 = float(e1.get())
            e1.delete(0, END)
            e1.insert(END, float(ee1))
        else:
             tk.Label(frm1, text='Enter number first').grid(row=2, column=0)

    def pow2():
        if not len(e1.get()) == 0:
            ee1 = float(e1.get()) ** 2
            mem.sto(ee1)
            e1.delete(0, END)
            e1.insert(END, float(ee1))
        else:
             tk.Label(frm1, text='Enter number first').grid(row=2, column=0)
        
    def pow3():
        if not len(e1.get()) == 0:
            ee1 = float(e1.get()) ** 3
            mem.sto(ee1)
            e1.delete(0, END)
            e1.insert(END, float(ee1))
        else:
             tk.Label(frm1, text='Enter number first').grid(row=2, column=0)
        
    def pow4():
        if not len(e1.get()) == 0:
            ee1 = float(e1.get()) ** 4
            mem.sto(ee1)
            e1.delete(0, END)
            e1.insert(END, float(ee1))
        else:
             tk.Label(frm1, text='Enter number first').grid(row=2, column=0)
        
    def powpow():
        if not len(e1.get()) == 0:
            ee1 = float(e1.get()) ** float(e1.get())
            mem.sto(ee1)
            e1.delete(0, END)
            e1.insert(END, float(ee1))
        else:
             tk.Label(frm1, text='Enter number first').grid(row=2, column=0)
        
    def powpow3():
        if not len(e1.get()) == 0:
            if float(e1.get()) >= 5:
                e1.insert(END, 'too big>=5')
                mem.sto('too big >= 5')
            else:              
                ee1 = float(e1.get()) ** float(e1.get()) ** float(e1.get())
                e1.delete(0, END)
                mem.sto(ee1)
                e1.insert(END, float(ee1))
        else:
             tk.Label(frm1, text='Enter number first').grid(row=2, column=0)
        
    def sq_rt():
        if not len(e1.get()) == 0:
            ee1 = float(e1.get()) ** 0.5
            mem.sto(ee1)
            e1.delete(0, END)
            e1.insert(END, float(ee1))
        else:
             tk.Label(frm1, text='Enter number first').grid(row=2, column=0)
        
    def cu_rt():
        if not len(e1.get()) == 0:
            ee1 = float(e1.get()) ** 0.3
            e1.delete(0, END)
            e1.insert(END, float(ee1))
            mem.sto(ee1)
        else:
             tk.Label(frm1, text='Enter number first').grid(row=2, column=0)

    def pow_qt():
        if not len(e1.get()) == 0:
            ee1 = float(e1.get()) ** 0.25
            e1.delete(0, END)
            e1.insert(END, float(ee1))
            mem.sto(ee1)
        else:
             tk.Label(frm1, text='Enter number first').grid(row=2, column=0)

    def inv2():
        if not len(e1.get()) == 0:
            if e1.get() == 0:
                e1.insert(END, 'not 0')
            else:
                ee1 = 1 / float(e1.get())
                e1.delete(0, END)
                e1.insert(END, float(ee1))
                mem.sto(ee1)
        else:
             tk.Label(frm1, text='Enter number first').grid(row=2, column=0)
                
    def any_rt():
        tk.Label(frm1, text='base then root').grid(row=2, column=0)
        if not len(e4.get()) == 0:
            if not len(e3.get()) == 0:
                ee4 = float(e4.get())
                lb.insert(1, e4.get())
                e4.delete(0, END)
                ee3 = float(e3.get())
                if ee3 == 0:
                    e5.insert(0, 'undefined')
                    tk.Label(frm1, text='   ----no answer----  ').grid(row=4, column=1)
                else:    
                    ee5 = float(ee4) / float(ee3)
                    e5.insert(END, float(ee5))
                    mem.sto(ee5)
                    tk.Label(frm1, text='   ----answer----  ').grid(row=4, column=1)
                    e3.delete(0, END)
        
        if not len(e2.get()) == 0:
            e3.insert(END, float(e2.get()))
            e2.delete(0, END)
        if not len(e1.get()) == 0:    
            ee1 = float(e1.get())
            mem.sto(ee1)
            e2.insert(END, float(ee1))
            ee2 = float(e2.get())
            mem.sto(ee2)
            e1.delete(0, END)
       
        
        def eq():
            if not len(e6.get()) == 0:
                if not len(e5.get()) == 0:
                           ee5 = float(e5.get())
                           ee6 = float(e6.get())
                           mem.sto(ee5)
                           if ee5 == 0:
                               e7.insert(END, 'Undefined')
                           else:
                               rt5 = 1 / float(ee5)
                               
                               ee7 = float(ee6) ** float(rt5)
                               mem.sto(ee7)
                               e7.insert(END, float(ee7))
                                              
            elif not len(e1.get()) == 0:    
                e6.delete(0, END)
                ee1 = float(e1.get())
                ee2 = float(e2.get())
                mem.sto(ee1)
                mem.sto(ee2)
              
           
            if ee1 == 0:
                e6.insert(END, 'Undefined')
                tk.Label(frm1, text='----------Infinite-----------').grid(row=4, column=1)
                tk.Label(frm1, text='---Value--').grid(row=5, column=1)
            else:    
                rt1 = 1 / ee1
                ans = float(ee2) ** float(rt1)
                tk.Label(frm1, text='----------------answer-------------------').grid(row=4, column=1)
                
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
        mem.sto(answer)
        e6.insert(END, answer)
         
        return answer

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
        mem.sto(answer)
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
        tk.Label(frm1, text='Enter Base').grid(row=2, column=0)
        def eq():
            if not len(e6.get()) == 0:
                lb.insert(1, e6.get())
                e6.delete(0, END)
            ee1 = float(e1.get())
            ee2 = float(e2.get())
            answer = math.log(ee1, ee2)
            mem.sto(answer)
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
        mem.sto(answer)
        
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
        tk.Label(frm1, text='Enter number raised').grid(row=2, column=0)
        def eq():
             if not len(e6.get()) == 0:
                 lb.insert(1, e6.get())
                 e6.delete(0, END)
             ee1 = float(e1.get())
             ee2 = float(e2.get())
             answer = math.pow(ee1, ee2)
             e6.insert(END, answer)
             mem.sto(answer)
              
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
        mem.sto(answer)
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
                  e6.insert(END, 'Undefined')
                  tk.Label(frm1, text='----ERROR----').grid(row=2, column=1) 

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
        mem.sto(answer)
        
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
        mem.sto(answer)
        
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
        mem.sto(answer)
    
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
        mem.sto(answer)
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
        mem.sto(answer)
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
        mem.sto(answer)
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
        mem.sto(answer)
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
        mem.sto(answer)
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
        mem.sto(answer)
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
        mem.sto(answer)
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
        mem.sto(answer)
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
        mem.sto(answer)
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
                      e2.insert(0, float(ee2))
                      mem.sto(ee2)
                      
           
        ee1 = float(e1.get() * -1)
        mem.sto(ee1)
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
        tk.Label(frm1, text='').grid(row=2, column=0)
        def eq():
            if not len(e6.get()) == 0:
                lb.insert(1, e6.get())
                e6.delete(0, END)
            ee1 = float(e1.get())
            ee2 = float(e2.get())
            answer = math.hypot(ee1, ee2)
            mem.sto(answer)
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
        mem.sto(pie)
        return pie


    def absolute_value():
        if not len(e4.get()) == 0:
            lb.insert(0, e4.get())
            e4.delete(0, END)
        if not len(e3.get()) == 0:
            e4.insert(END, e3.get())
            e3.delete(0, END)
        if not len(e2.get()) == 0:
            lb.insert(1, e2.get())
            e2.delete(0, END)
        if not len(e6.get()) == 0:
            lb.insert(0, e6.get())
            e6.delete(0, END)
            ans = abs(float(e1.get()))

        e2.insert(END, ans)
        mem.sto(ans)



    def pi2():
        if not len(e4.get()) == 0:
            lb.insert(0, e4.get())
            e4.delete(0, END)
        if not len(e3.get()) == 0:
            e4.insert(END, e3.get())
            e3.delete(0, END)
        if not len(e2.get()) == 0:
            lb.insert(0, e2.get())
            e2.delete(0, END)
        if not len(e6.get()) == 0:
            lb.insert(0, e6.get())
            e6.delete(0, END)
       

        pi = float(math.pi)
        pi2 = pi * 2
        e2.insert(END, pi2)
        mem.sto(pi2)
        return pi2
    
    def half_pi():
        if not len(e4.get()) == 0:
            lb.insert(1, e4.get())
            e4.delete(0, END)
        if not len(e3.get()) == 0:
            e4.insert(END, e3.get())
            e3.delete(0, END)
        if not len(e2.get()) == 0:
            lb.insert(END, e2.get())
            e2.delete(0, END)
        if not len(e6.get()) == 0:
            lb.insert(1, e6.get())
            e6.delete(0, END)
       
        pi = float(math.pi)
        halfpi = float(pi) / 2
        e2.insert(END, halfpi)
        mem.sto(halfpi)
        return halfpi

    def quarter_pi():
        if not len(e4.get()) == 0:
            lb.insert(END, e4.get())
            e4.delete(0, END)
        if not len(e3.get()) == 0:
            e4.insert(END, e3.get())
            e3.delete(0, END)
        if not len(e2.get()) == 0:
            lb.insert(END, e2.get())
            e2.delete(0, END)
        if not len(e6.get()) == 0:
            lb.insert(END, e6.get())
            e6.delete(0, END)
            if not len(e2.get()) == 0:
                    lb.insert(END, e2.get())
                    e2.delete(0, END)
        pi = float(math.pi)
        quartpi = pi / 4
        e2.insert(END, quartpi)
        mem.sto(quartpi)
        return quartpi

    def eighth_pi():
        if not len(e4.get()) == 0:
            lb.insert(0, e4.get())
            e4.delete(0, END)
        if not len(e3.get()) == 0:
            e4.insert(END, e3.get())
            e3.delete(0, END)
        if not len(e2.get()) == 0:
            lb.insert(0, e2.get())
            e2.delete(0, END)
        if not len(e2.get()) == 0:
            lb.insert(0, e2.get())
            e2.delete(0, END)

        if not len(e6.get()) == 0:
                lb.insert(1, e6.get())
                e6.delete(0, END)
        pi = float(math.pi)
        eighthpi = pi / 8
        e2.insert(END, eighthpi)
        mem.sto(eighthpi)
        return eighthpi


    def pi_div16():
        if not len(e4.get()) == 0:
            lb.insert(0, e4.get())
            e4.delete(0, END)
        if not len(e3.get()) == 0:
            e4.insert(END, e3.get())
            e3.delete(0, END)
        if not len(e2.get()) == 0:
            lb.insert(0, e2.get())
            e2.delete(0, END)
        if not len(e6.get()) == 0:
            lb.insert(0, e6.get())
            e6.delete(0, END)

        
        pi = float(math.pi)
        sixteenthpi = pi / 16
        e2.insert(END, sixteenthpi)
        mem.sto(sixteenthpi)
        return sixteenthpi

    def eq1():
        
        def solver(a,b,c):
            ''' Solves quadratic equation and returns the result in formatted string '''
            D = b*b - 4*a*c
            if D >= 0:
                x1 = (-b + math.sqrt(D)) / (2*a)
                x2 = (-b - math.sqrt(D)) / (2*a)
                text = 'The discriminant is: %s \n X1 is: %s \n X2 is: %s \n' % (D, x1, x2)        
            else:
                text = 'The discriminant is: %s \n This equation has no solutions' % D 
            return text

        def inserter(value):
            ''' Inserts specified value into text widget '''
            output.delete('0.0','end')
            output.insert('0.0',value)    

        def clear(event):
            ''' Clears entry form '''
            caller = event.widget
            caller.delete('0', 'end')

        def handler():
            ''' Get the content of entries and passes result to the text '''
            try:
                # make sure that we entered correct values
                a_val = float(a.get())
                b_val = float(b.get())
                c_val = float(c.get())
                inserter(solver(a_val, b_val, c_val))
            except ValueError:
                inserter('Make sure you entered 3 numbers')

        top = Toplevel()
        top.title('Quadratic calculator')
        top.minsize(325,230)
        top.resizable(width=False, height=False)


        frame = Frame(top)
        frame.grid()

        a = Entry(frame, width=3)
        a.grid(row=1,column=1,padx=(10,0))
        a.bind('<FocusIn>', clear)
        a_lab = Label(frame, text='x**2+').grid(row=1,column=2)

        b = Entry(frame, width=3)
        b.bind('<FocusIn>', clear)
        b.grid(row=1,column=3)
        b_lab = Label(frame, text='x+').grid(row=1, column=4)

        c = Entry(frame, width=3)
        c.bind('<FocusIn>', clear)
        c.grid(row=1, column=5)
        c_lab = Label(frame, text='= 0').grid(row=1, column=6)

        but = Button(frame, text='Solve', command=handler).grid(row=1, column=7, padx=(10,0))

        output = Text(frame, bg='lightblue', font='Arial 12', width=35, height=10)
        output.grid(row=2, columnspan=8)

####Buttons for Function Calls##########################################################################################################
    btn1 = tk.Button(frm2, text='Factorial', bd=5, bg= 'CadetBlue3', font=('URW Chancery L',8,'bold'), command=factorial)
    btn1.grid(row=0, column=1)
    btn2 = tk.Button(frm2, text='FMOD', bd=5, bg= 'DarkOrchid1', font=('URW Chancery L',8,'bold'), command=fmod)
    btn2.grid(row=1, column=1)
    btn3 = tk.Button(frm2, text='EPX', bd=5, bg= 'DarkSlateGray1', font=('URW Chancery L',8,'bold'), command=epown)
    btn3.grid(row=2, column=1)
    btn4 = tk.Button(frm2, text='EPX -1', bd=5, bg= 'DeepSkyBlue2', font=('URW Chancery L',8,'bold'), command=epownm1)
    btn4.grid(row=3, column=1)
    btn5 = tk.Button(frm2, text='LOG e', bd=5, bg= 'DodgerBlue2', font=('URW Chancery L',8,'bold'), command=loge)
    btn5.grid(row=4, column=1)
    btn6 = tk.Button(frm2, text='LOG', bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=log)
    btn6.grid(row=5, column=1)
    btn7 = tk.Button(frm2, text='LOG10', bd=5, bg= 'cyan', font=('URW Chancery L',8,'bold'), command=log10)
    btn7 .grid(row=6, column=1)
    btn8 = tk.Button(frm2, text='POWER x,y', bd=5, bg= 'cornsilk', font=('URW Chancery L',8,'bold'), command=pow_of_var)
    btn8.grid(row=7, column=1)
    btn9 = tk.Button(frm2, text='1/X INV', bd=5, bg= 'wheat', font=('URW Chancery L',8,'bold'), command=inv2)
    btn9.grid(row=8, column=1)
    btn10 = tk.Button(frm2, text='SQU ROOT', bd=5, bg= 'lavender', font=('URW Chancery L',8,'bold'), command=sqrt)
    btn10.grid(row=9, column=1)
    btn11 = tk.Button(frm2, text='Pi', bd=5, bg= 'cornsilk', font=('URW Chancery L',8,'bold'), command=pi)
    btn11.grid(row=4, column=12)
    btn12 = tk.Button(frm2, text='2Pi', bd=5, bg= 'lime green', font=('URW Chancery L',8,'bold'), command=pi2)
    btn12.grid(row=6, column=12)
    btn13 = tk.Button(frm2, text='Pi/2', bd=5, bg= 'violet', font=('URW Chancery L',8,'bold'), command=half_pi)
    btn13.grid(row=5, column=12)
    btn15 = tk.Button(frm2, text='Pi/4', bd=5, bg= 'light blue', font=('URW Chancery L',8,'bold'), command=quarter_pi)
    btn15.grid(row=4, column=12)
    btn16a = tk.Button(frm2, text='Pi/8', bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=eighth_pi)
    btn16a.grid(row=3, column=12)
    btn15b = tk.Button(frm2, text='Pi/16', bd=5, bg= 'azure', font=('URW Chancery L',8,'bold'), command=quarter_pi)
    btn15b.grid(row=2, column=12)
    ##################
    btn62 = tk.Button(frm2, text='  7  ', bd=5, bg= 'azure', font=('URW Chancery L',8,'bold'), command=seven)
    btn62.grid(row=0, column=2)
    btn63 = tk.Button(frm2, text='  4  ', bd=5, bg= 'azure', font=('URW Chancery L',8,'bold'), command=four)
    btn63.grid(row=1, column=2)
    btn0064 = tk.Button(frm2, text='  1  ', bd=5, bg= 'azure', font=('URW Chancery L',8,'bold'), command=one)
    btn0064.grid(row=2, column=2)
    btn51 = tk.Button(frm2, text='^2', bd=5, bg= 'lawn green', font=('URW Chancery L',8,'bold'), command=pow2)
    btn51.grid(row=3, column=2)
    btn52 = tk.Button(frm2, text='^3', bd=5, bg= 'light blue', font=('URW Chancery L',8,'bold'), command=pow3)
    btn52.grid(row=9, column=13)
    btn53 = tk.Button(frm2, text='^4', bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=pow4)
    btn53.grid(row=8, column=13)
    btn54 = tk.Button(frm2, text='pow^pow', bd=5, bg= 'cyan', font=('URW Chancery L',8,'bold'), command=powpow)
    btn54.grid(row=7, column=13)
    btn55 = tk.Button(frm2, text='^pow^pow', bd=5, bg= 'violet', font=('URW Chancery L',8,'bold'), command=powpow3)
    btn55.grid(row=6, column=13)
    btn56 = tk.Button(frm2, text='sqrt2', bd=5, bg= 'cornsilk', font=('URW Chancery L',8,'bold'), command=sq_rt)
    btn56.grid(row=5, column=13)
    btn57 = tk.Button(frm2, text='cube rt', bd=5, bg= 'wheat', font=('URW Chancery L',8,'bold'), command=cu_rt)
    btn57.grid(row=4, column=13)
    btn58 = tk.Button(frm2, text='4th rt', bd=5, bg= 'light green', font=('URW Chancery L',8,'bold'), command=pow_qt)
    btn58.grid(row=2, column=13)
    btn59 = tk.Button(frm2, text='y ^ 1/x', bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=any_rt)
    btn59.grid(row=1, column=13)
    ############################################################################################################
    btn108 = tk.Button(frm2, text='  8  ', bd=5, bg= 'azure', font=('URW Chancery L',8,'bold'), command=eight)
    btn108.grid(row=0, column=3)
    btn109 = tk.Button(frm2, text='  5  ', bd=5, bg= 'azure',  font=('URW Chancery L',8,'bold'), command=five)
    btn109.grid(row=1, column=3)
    btn909 = tk.Button(frm2, text='  2  ', bd=5, bg= 'azure',  font=('URW Chancery L',8,'bold'), command=two)
    btn909.grid(row=2, column=3)
    btn188 = tk.Button(frm2, text=' +/-  ', bd=5, bg= 'light green', font=('URW Chancery L',8,'bold'), command=signchr)
    btn188.grid(row=3, column=3)
    btn189 = tk.Button(frm2, text='  0   ', bd=5, bg= 'light blue', font=('URW Chancery L',8,'bold'), command=zero)
    btn189.grid(row=4, column=3)   
    ############################################################################################################
    btn99 = tk.Button(frm2, text='Quadratic', bd=5, bg= 'light blue', font=('URW Chancery L',8,'bold'), command=eq1)
    btn99.grid(row=5, column=3)
    btn160 = tk.Button(frm2, text='  9  ', bd=5, bg= 'azure',font=('URW Chancery L',8,'bold'), command=nine)
    btn160.grid(row=0, column=4)
    btn161 = tk.Button(frm2, text='   6  ', bd=5, bg= 'azure', font=('URW Chancery L',8,'bold'), command=six)
    btn161.grid(row=1, column=4)
    btn1777 = tk.Button(frm2, text='  3  ', bd=5, bg= 'azure',font=('URW Chancery L',8,'bold'), command=three)
    btn1777.grid(row=2, column=4)
    btn147 = tk.Button(frm2, text='1/x ans', bd=5, bg= 'cornsilk', font=('URW Chancery L',8,'bold'), command=inv)
    btn147.grid(row=3, column=4)
    btn150 = tk.Button(frm2, text='Shift Ans', bd=5, bg= 'violet', font=('URW Chancery L',8,'bold'), command=shift_ans1)
    btn150.grid(row=4, column=4)
    btn151 = tk.Button(frm2, text='Mem move to', bd=5, bg= 'pink', font=('URW Chancery L',8,'bold'), command=shift_mem)
    btn151.grid(row=5, column=4)
    btn152 = tk.Button(frm2, text='Entry1 to Mem', bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=to_mem)
    btn152.grid(row=6, column=4)
    btn153 = tk.Button(frm2, text='Btn1', bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cmd)
    btn153.grid(row=7, column=4)
    btn167 = tk.Button(frm2, text='.', bd=5, bg= 'cyan', font=('URW Chancery L',8,'bold'), command=point)
    btn167.grid(row=0, column=5)
    btn200 = tk.Button(frm2, text='  /  ', bd=5, bg= 'cornsilk', font=('URW Chancery L',8,'bold'), command=div)
    btn200.grid(row=1, column=5)
    btn1499 = tk.Button(frm2, text=' X ', bd=5, bg= 'lavender',  font=('URW Chancery L',8,'bold'), command=mul)
    btn1499.grid(row=2, column=5)
    btn109 = tk.Button(frm2, text='  -  ', bd=5, bg= 'LightPink1', font=('URW Chancery L',8,'bold'), command=subtract)
    btn109.grid(row=3, column=5)
    btn140 = tk.Button(frm2, text='  +  ', bd=5, bg= 'light blue', font=('URW Chancery L',8,'bold'), command=add)
    btn140.grid(row=4, column=5)
    btn173 = tk.Button(frm2, text='SIN', bd=5, bg= 'pink', font=('URW Chancery L',8,'bold'), command=sin)
    btn173.grid(row=0, column=6)
    btn174 = tk.Button(frm2, text='COS', bd=5, bg= 'light blue', font=('URW Chancery L',8,'bold'), command=cos)
    btn174.grid(row=1, column=6)
    btn175 = tk.Button(frm2, text='TAN', bd=5, bg= 'cornsilk', font=('URW Chancery L',8,'bold'), command=tan)
    btn175.grid(row=2, column=6)
    btn176 = tk.Button(frm2, text='ASIN', bd=5, bg= 'light green', font=('URW Chancery L',8,'bold'), command=asin)
    btn176.grid(row=3, column=6)
    btn177 = tk.Button(frm2, text='ACOS', bd=5, bg= 'pink', font=('URW Chancery L',8,'bold'), command=acos)
    btn177.grid(row=4, column=6)
    btn178 = tk.Button(frm2, text='ATAN', bd=5, bg= 'cyan', font=('URW Chancery L',8,'bold'), command=atan)
    btn178.grid(row=8, column=11)
    btn179 = tk.Button(frm2, text='SINH', bd=5, bg= 'violet', font=('URW Chancery L',8,'bold'), command=sinh)
    btn179.grid(row=7, column=11)
    btn180 = tk.Button(frm2, text='COSH', bd=5, bg= 'orange', font=('URW Chancery L',8,'bold'), command=cosh)
    btn180.grid(row=6, column=11)
    btn181 = tk.Button(frm2, text='TANH', bd=5, bg= 'lavender', font=('URW Chancery L',8,'bold'), command=tanh)
    btn181.grid(row=5, column=11)
    btn182 = tk.Button(frm2, text='ASINH', bd=5, bg= 'seashell', font=('URW Chancery L',8,'bold'), command=asinh)
    btn182.grid(row=4, column=11)
    btn183 = tk.Button(frm2, text='ACOSH', bd=5, bg= 'seagreen', font=('URW Chancery L',8,'bold'), command=acosh)
    btn183.grid(row=3, column=11)
    btn184 = tk.Button(frm2, text='ATANH', bd=5, bg= 'cornsilk', font=('URW Chancery L',8,'bold'), command=atanh)
    btn184.grid(row=2, column=11)
    btn185= tk.Button(frm2, text='HYP', bd=5, bg= 'linen', font=('URW Chancery L',8,'bold'), command=hyp)
    btn185.grid(row=1, column=11)
    gg243 = tk.Button(frm2, text='CLR ALL', bd=5, bg= '#cbcdd8', font=('URW Chancery L',8,'bold'), command=clearall)
    gg243.grid(row=0, column=8)
    gg244 = tk.Button(frm2, text='CE1', bd=5, bg= '#cbcdd8', font=('URW Chancery L',8,'bold'), command=clear1)
    gg244.grid(row=1, column=8)
    gg245 = tk.Button(frm2, text='CE2', bd=5, bg= '#cbcdd8', font=('URW Chancery L',8,'bold'), command=clear2)
    gg245.grid(row=2, column=8)
    gg246 = tk.Button(frm2, text='CE3', bd=5, bg= '#cbcdd8', font=('URW Chancery L',8,'bold'), command=clear3)
    gg246.grid(row=3, column=8)
    gg247 = tk.Button(frm2, text='CE4', bd=5, bg= '#cbcdd8', font=('URW Chancery L',8,'bold'), command=clear4)
    gg247.grid(row=4, column=8)
    gg250 = tk.Button(frm2, text='CLR ANS', bd=5, bg= 'DarkOrchid1', font=('URW Chancery L',8,'bold'), command=clear6)
    gg250.grid(row=5, column=8)
    gg251 = tk.Button(frm2, text='CLR MEM', bd=5, bg= 'DeepSkyBlue2', font=('URW Chancery L',8,'bold'), command=clrmem)
    gg251.grid(row=6, column=8)
    gg252 = tk.Button(frm2, text='MEM ENTRY', bd=5, bg='LightGoldenrod1', font=('URW Chancery L',8,'bold'), command=sto1)
    gg252.grid(row=7, column=8)
    gg253 = tk.Button(frm2, text='MEM ANS', bd=5, bg= 'cornsilk', font=('URW Chancery L',8,'bold'), command=stoans)
    gg253.grid(row=6, column=10)
    gg254 = tk.Button(frm2, text='RECALL', bd=5, bg= 'ivory2', font=('URW Chancery L',8,'bold'), command=recall_mem)
    gg254.grid(row=5, column=10)
    gg255 = tk.Button(frm2, text='Shift1-2', bd=5, bg= 'ivory3', font=('URW Chancery L',8,'bold'), command=shift1)
    gg255.grid(row=4, column=10)
    gg256= tk.Button(frm2, text='Shift2-3', bd=5, bg= 'pink', font=('URW Chancery L',8,'bold'), command=shift2)
    gg256.grid(row=3, column=10)
    gg257 = tk.Button(frm2, text='Shift3-4', bd=5, bg= 'cornsilk', font=('URW Chancery L',8,'bold'), command=shift3)
    gg257.grid(row=2, column=10)
    gg258= tk.Button(frm2, text='Shift4-Mem', bd=5, bg= 'violet', font=('URW Chancery L',8,'bold'), command=shift4)
    gg258.grid(row=1, column=10)

scientific_calculator()

class StopWatchApp:
    def __init__(self):
        

        self.timer_running = False
        self.start_time = None
        self.last_time = 0  # Initialize last_time with 0

        self.time_entry = tk.Entry(tab.f6, font=('Arial', 20))
        self.time_entry.grid(row=6,rowspan=3, columnspan=6)

        self.start_button = tk.Button(tab.f6, text='Start', command=self.start_timer)
        self.start_button.grid(row=10, column=0)

        self.stop_button = tk.Button(tab.f6, text='Stop', command=self.stop_timer)
        self.stop_button.grid(row=10, column=1)

        self.reset_button = tk.Button(tab.f6, text='Reset', command=self.reset_timer)
        self.reset_button.grid(row=10, column=2)
        self.reset_button = tk.Button(tab.f6, text='Continue', command=self.continue_timer)
        self.reset_button.grid(row=10, column=3)
        # Listbox to display stopped times
        self.stopped_times_listbox = tk.Listbox(tab.f6, width=20, height=10)
        self.stopped_times_listbox.grid(row=20, columnspan=3)

    def start_timer(self):
        if not self.timer_running:
            self.start_time = time.time() - self.last_time
            self.update_timer()
            self.timer_running = True

    def stop_timer(self):
        if self.timer_running:
            elapsed_time = time.time() - self.start_time
            self.last_time = elapsed_time  # Save the elapsed time
            time_string = time.strftime('%H:%M:%S', time.gmtime(elapsed_time))
            self.stopped_times_listbox.insert(tk.END, time_string)
            mem.sto(time_string)
            self.timer_running = False

    def reset_timer(self):
        self.start_time = None
        self.timer_running = False
        self.last_time = 0  # Reset last_time to 0
        self.time_entry.delete(0, tk.END)
        self.stopped_times_listbox.delete(0, tk.END)

    def continue_timer(self):
        if not self.timer_running:
            self.start_time = time.time() - self.last_time
            self.update_timer()
            self.timer_running = True

    def update_timer(self):
        if self.timer_running:
            elapsed_time = time.time() - self.start_time
            minutes, seconds = divmod(int(elapsed_time), 60)
            hours, minutes = divmod(minutes, 60)
            milliseconds = int((elapsed_time - int(elapsed_time)) * 1000)
            time_string = f'{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}'
            self.time_entry.delete(0, tk.END)
            self.time_entry.insert(0,time_string)
            tk.Label(tab.f6,text= f'{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}').grid(row=24, column=4)
        nb.after(10, self.update_timer)


stopwatch = StopWatchApp()

class PercentageCalculatorTab:
    def __init__(self, parent):
        self.parent = parent
        self.create_widgets()

    def calculate_percentage(self):
        try:
            base_value = float(self.input_value_entry.get())
            percentage = float(self.input_percentage_entry.get()) / 100

            percentage_value = base_value * percentage
            lower_bound = base_value - percentage_value
            upper_bound = base_value + percentage_value
            range_value = abs(lower_bound - upper_bound)

            self.lower_bound_entry.delete(0, tk.END)
            self.upper_bound_entry.delete(0, tk.END)
            self.range_entry.delete(0, tk.END)
            self.percentage_value_entry.delete(0, tk.END)

            self.lower_bound_entry.insert(0, lower_bound)
            self.upper_bound_entry.insert(0, upper_bound)
            self.range_entry.insert(0, range_value)
            self.percentage_value_entry.insert(0, percentage_value)
            mem.sto(base_value)
            mem.sto(percentage)
            mem.sto(lower_bound)
            mem.sto(upper_bound)
            mem.sto(range_value)
            mem.sto(percentage_value)
                
        except Exception as ex:
            print('Error:', ex)

    def clear_entries(self):
        for entry in [self.input_value_entry, self.input_percentage_entry, 
                      self.lower_bound_entry, self.upper_bound_entry, 
                      self.range_entry, self.percentage_value_entry]:
            entry.delete(0, tk.END)

    def create_widgets(self):
        # Entry labels
        labels = ['Input Value', 'Input Percentage', 'Will be between', 'And', 'Value Range is', 'Percent Value']
        for i, text in enumerate(labels):
            tk.Label(self.parent, text=text).grid(row=i, column=0, padx=10, pady=5)

        # Entries
        self.input_value_entry = tk.Entry(self.parent, bd=7)
        self.input_percentage_entry = tk.Entry(self.parent, bd=7)
        self.lower_bound_entry = tk.Entry(self.parent, bd=7, bg='lavender')
        self.upper_bound_entry = tk.Entry(self.parent, bd=7, bg='lavender')
        self.range_entry = tk.Entry(self.parent, bd=7, bg='lavender')
        self.percentage_value_entry = tk.Entry(self.parent, bd=7, bg='lavender')

        entries = [self.input_value_entry, self.input_percentage_entry, 
                   self.lower_bound_entry, self.upper_bound_entry, 
                   self.range_entry, self.percentage_value_entry]

        for i, entry in enumerate(entries):
            entry.grid(row=i, column=1, padx=10, pady=5)

        # Buttons
        calculate_button = tk.Button(self.parent, text='Calculate', command=self.calculate_percentage)
        clear_button = tk.Button(self.parent, text='Clear', command=self.clear_entries)
        calculate_button.grid(row=8, column=1, pady=10)
        clear_button.grid(row=10, column=1, pady=10)


PercentageCalculatorTab(tab.f7)





class UnitConverter:
    def __init__(self, conversion_factors):
        self.conversion_factors = conversion_factors

    def convert(self, unit1, unit2, value):
        if unit1 in self.conversion_factors and unit2 in self.conversion_factors[unit1]:
            factor = self.conversion_factors[unit1][unit2]
            converted_value = value * factor
            return converted_value, unit2
        else:
            return None

class LengthUnitConverter(UnitConverter):
    def __init__(self):
        conversion_factors = {
             'cm': {'inch': 1 / 2.54, 'mm': 10, 'm': 0.01, 'ft': 1 / 30.48, 'mi': 1 / 160934.4},
             'inch': {'cm': 2.54, 'mm': 25.4, 'm': 0.0254, 'ft': 1 / 12,
        'mi': 1 / 63360},
             'm': {'cm': 100, 'inch': 39.37, 'mm': 1000, 'ft': 3.28084,
        'mi': 0.000621371},
             'ft': {'cm': 30.48, 'inch': 12, 'mm': 304.8, 'm': 0.3048,
        'mi': 1 / 5280},
             'km': {'mi': 0.621371, 'ft': 3280.84, 'inch': 39370.1,
        'cm': 100000, 'mm': 1000000, 'm': 1000},
         }
        super().__init__(conversion_factors)

class LiquidUnitConverter(UnitConverter):
    def __init__(self):
        conversion_factors = {
             'ml': {'liters': 0.001, 'fl oz': 0.033814, 'cup': 
0.00416667, 'pint': 0.00211338, 'quart': 0.00105669, 'gallon': 0.000264172},
             'liters': {'ml': 1000, 'fl oz': 33.814, 'cup': 4.16667,
'pint': 2.11338, 'quart': 1.05669, 'gallon': 0.264172},
             'fl oz': {'ml': 29.5735, 'liters': 0.0295735, 'cup': 
0.123223, 'pint': 0.0625, 'quart': 0.03125, 'gallon': 0.0078125},
             'cup': {'ml': 240, 'liters': 0.24, 'fl oz': 8.11537,
'pint': 0.50721, 'quart': 0.253605, 'gallon': 0.0634013},
             'pint': {'ml': 473.176, 'liters': 0.473176, 'fl oz': 16,
'cup': 1.97157, 'quart': 0.5, 'gallon': 0.125},
             'quart': {'ml': 946.353, 'liters': 0.946353, 'fl oz': 32,
'cup': 3.94314, 'pint': 2, 'gallon': 0.25},
             'gallon': {'ml': 3785.41, 'liters': 3.78541, 'fl oz': 128,
'cup': 15.7725, 'pint': 7.74597, 'quart': 4},
         }
        super().__init__(conversion_factors)

class WeightUnitConverter(UnitConverter):
    def __init__(self):
        conversion_factors = {
             'g': {'lbs': 0.00220462, 'kg': 0.001, 'tons': 0.000001,
'oz': 0.035274},
             'lbs': {'g': 453.592, 'kg': 0.453592, 'tons': 0.0005, 'oz': 
16},
             'kg': {'g': 1000, 'lbs': 2.20462, 'tons': 0.001, 'oz': 35.274},
             'tons': {'g': 1000000, 'lbs': 2000, 'kg': 1000, 'oz': 35274},
             'oz': {'g': 28.3495, 'lbs': 0.0625, 'kg': 0.0283495,
'tons': 0.0000283495},
         }
        super().__init__(conversion_factors)


class Weight_Length_Liquid_Temperature():
    def __init__(self, parent):

        self.parent = parent
       

        self.length_converter = LengthUnitConverter()
        self.liquid_converter = LiquidUnitConverter()
        self.weight_converter = WeightUnitConverter()

        nb004 = ttk.Notebook(self.parent)
        nb004.grid(row=1,column=1)
        length_frame = ttk.Frame(nb004)
        self.setup_length_conversion(length_frame)
        nb004.add(length_frame, text='Length')

        liquid_frame = ttk.Frame(nb004)
        self.setup_liquid_conversion(liquid_frame)
        nb004.add(liquid_frame, text='Liquid')

        weight_frame = ttk.Frame(nb004)
        self.setup_weight_conversion(weight_frame)
        nb004.add(weight_frame, text='Weight')
        temperature_frame = ttk.Frame(nb004)
        nb004.add(temperature_frame, text='Temperature')
        self.temp_converter = Temperature_converter(temperature_frame)
        basenum_frame=tk.Frame(nb004)
        nb004.add(basenum_frame, text='Base Number Convert')
        self.basernumber_converter =  BaseConverter(basenum_frame)      
    

    def setup_length_conversion(self, frame):
        from_units = list(self.length_converter.conversion_factors.keys())
        to_units = list(self.length_converter.conversion_factors.keys())

        tk.Label(frame, text='From:').grid(row=0, column=2)
        self.cb1_length = ttk.Combobox(frame, values=from_units)
        self.cb1_length.grid(row=0, column=3)

        tk.Label(frame, text='To:').grid(row=1, column=2)
        self.cb2_length = ttk.Combobox(frame, values=to_units)
        self.cb2_length.grid(row=1, column=3)

        tk.Label(frame, text='Value:').grid(row=2, column=2)
        self.e1_length = tk.Entry(frame, bd=5, bg='seashell')
        self.e1_length.grid(row=2, column=3)
        self.e2_length = tk.Entry(frame, bd=5, width=30, bg='seashell')
        self.e2_length.grid(row=4, column=3)
        self.e3_length = tk.Entry(frame, bd=5, width=30, bg='seashell')
        self.e3_length.grid(row=4, column=4)


        self.btn_length = tk.Button(frame, text='Calculate', bd=5, bg='light green', command=self.convert_length)
        self.btn_length.grid(row=6, column=2, columnspan=2)
        self.btn_liquid = tk.Button(frame, text='Clear', bd=5, bg='light green', command=self.clear_length)
        self.btn_liquid.grid(row=8, column=2, columnspan=2)
    def setup_liquid_conversion(self, frame):
        from_units = list(self.liquid_converter.conversion_factors.keys())
        to_units = list(self.liquid_converter.conversion_factors.keys())

        tk.Label(frame, text='From:').grid(row=0, column=2)
        self.cb1_liquid = ttk.Combobox(frame, values=from_units)
        self.cb1_liquid.grid(row=0, column=3)

        tk.Label(frame, text='To:').grid(row=1, column=2)
        self.cb2_liquid = ttk.Combobox(frame, values=to_units)
        self.cb2_liquid.grid(row=1, column=3)

        tk.Label(frame, text='Value:').grid(row=2, column=2)
        self.e1_liquid = tk.Entry(frame, bd=5, bg='seashell')
        self.e1_liquid.grid(row=2, column=3)
        self.e2_liquid = tk.Entry(frame, bd=5,width=30, bg='seashell')
        self.e2_liquid.grid(row=4, column=3)
        self.e3_liquid = tk.Entry(frame, bd=5,width=30, bg='seashell')
        self.e3_liquid.grid(row=4, column=4)

        self.btn_liquid = tk.Button(frame, text='Calculate', bd=5, bg='light green', command=self.convert_liquid)
        self.btn_liquid.grid(row=6, column=2, columnspan=2)

        self.btn_liquid = tk.Button(frame, text='Clear', bd=5, bg='light green', command=self.clear_liquid)
        self.btn_liquid.grid(row=8, column=2, columnspan=2)

    def setup_weight_conversion(self, frame):
        from_units = list(self.weight_converter.conversion_factors.keys())
        to_units = list(self.weight_converter.conversion_factors.keys())

        tk.Label(frame, text='From:').grid(row=0, column=2)
        self.cb1_weight = ttk.Combobox(frame, values=from_units)
        self.cb1_weight.grid(row=0, column=3)

        tk.Label(frame, text='To:').grid(row=1, column=2)
        self.cb2_weight = ttk.Combobox(frame, values=to_units)
        self.cb2_weight.grid(row=1, column=3)

        tk.Label(frame, text='Value:').grid(row=2, column=2)
        self.e1_weight = tk.Entry(frame, bd=5, bg='seashell')
        self.e1_weight.grid(row=2, column=3)
        self.e2_weight = tk.Entry(frame, bd=5, width=30, bg='seashell')
        self.e2_weight.grid(row=4, column=3)
        self.e3_weight = tk.Entry(frame, bd=5, width=30, bg='seashell')
        self.e3_weight.grid(row=4, column=4)


        self.btn_weight = tk.Button(frame, text='Calculate', bd=5, bg='light green', command=self.convert_weight)
        self.btn_weight.grid(row=6, column=2, columnspan=2)
        self.btn_liquid = tk.Button(frame, text='Clear', bd=5, bg='light green', command=self.clear_weight)
        self.btn_liquid.grid(row=8, column=2, columnspan=2)
    def convert_length(self):
        try:
            unit1 = self.cb1_length.get()
            unit2 = self.cb2_length.get()
            value = float(self.e1_length.get())

            result = self.length_converter.convert(unit1, unit2, value)
            mem.sto(unit1)
            mem.sto(unit2)
            mem.sto(result)
            if result is not None:
                converted_value, converted_unit = result
                self.e2_length.insert(0, converted_value)
                self.e3_length.insert(1, converted_unit)
                mem.sto(converted_value)
                mem.sto(converted_unit)

        except ValueError:
            print(ValueError)



    def convert_liquid(self):
        try:
            unit1 = self.cb1_liquid.get()
            unit2 = self.cb2_liquid.get()
            value = float(self.e1_liquid.get())

            result = self.liquid_converter.convert(unit1, unit2, value)
            mem.sto(unit1)
            mem.sto(unit2)
            mem.sto(result)
            if result is not None:
                converted_value, converted_unit = result
                self.e2_liquid.insert(0, converted_value)
                self.e3_liquid.insert(1, converted_unit)
                mem.sto(converted_value)
                mem.sto(converted_unit)

        except ValueError:
            print(ValueError)

    def convert_weight(self):
        try:
            unit1 = self.cb1_weight.get()
            unit2 = self.cb2_weight.get()
            value = float(self.e1_weight.get())

            result = self.weight_converter.convert(unit1, unit2, value)
            mem.sto(unit1)
            mem.sto(unit2)
            mem.sto(result)
            if result is not None:
                converted_value, converted_unit = result
                self.e2_weight.insert(0, converted_value)
                self.e3_weight.insert(1, converted_unit)
                mem.sto(converted_value)
                mem.sto(converted_unit)
        except ValueError:
            print(ValueError)


            
    def clear_length(self):
        self.e1_length.delete(0,END)
        self.e2_length.delete(0,END)
        self.e3_length.delete(0,END)

    def clear_liquid(self):
        self.e1_liquid.delete(0,END)
        self.e2_liquid.delete(0,END)
        self.e3_liquid.delete(0,END)

    def clear_weight(self):
        self.e1_weight.delete(0,END)
        self.e2_weight.delete(0,END)
        self.e3_weight.delete(0,END)

class Temperature_converter:
    def __init__(self, parent):
        self.root = parent
                
        self.flabel = tk.Label(self.root, text = 'Fahrenheit')
        self.flabel.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'e')

        self.clabel = tk.Label(self.root, text = 'Celsius')
        self.clabel.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = 'e')

        self.klabel = tk.Label(self.root, text = 'Kelvin')
        self.klabel.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'e')

        self.ftext = tk.StringVar()
        self.ftext.set('')
        self.fahrenheit_entry = tk.Entry(self.root, textvariable=self.ftext)
        self.fahrenheit_entry.grid(row = 0, column = 1, padx = 5, pady = 5)

        self.ctext = tk.StringVar()
        self.ctext.set('')
        self.celsius_entry = tk.Entry(self.root, textvariable=self.ctext)
        self.celsius_entry.grid(row = 1, column = 1, padx = 5, pady = 5)

        self.ktext = tk.StringVar()
        self.ktext.set('')
        self.kelvin_entry = tk.Entry(self.root, textvariable=self.ktext)
        self.kelvin_entry.grid(row = 2, column = 1, padx = 5, pady = 5)
 
        self.fgobutton = tk.Button(self.root, text = 'Go', command = self.convert_f)
        self.fgobutton.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = 'news')

        self.cgobutton = tk.Button(self.root, text = 'Go', command = self.convert_c)
        self.cgobutton.grid(row = 1, column = 2, padx = 5, pady = 5, sticky = 'nsew')

        self.kgobutton = tk.Button(self.root, text = 'Go', command = self.convert_k)
        self.kgobutton.grid(row = 2, column = 2, padx = 5, pady = 5, sticky = 'nesw')

      
        self.clear= tk.Button(self.root, text = 'Clear All', command = self.clear)
        self.clear.grid(row=7, column=0, sticky='ew')
                   
    def convert_f(self):
        try :
            words = float(self.ftext.get())
            self.ftemp = float(words)
                 
            self.celsius_entry.delete(0, END)
            self.celsius_entry.insert(0, '%.2f' % (self.tocel(self.ftemp)))
            mem.sto(self.celsius_entry.get())
            
            self.kelvin_entry.delete(0, END)
            self.kelvin_entry.insert(0, '%.2f' % (self.tokel(self.tocel(self.ftemp))))
            mem.sto(self.kelvin_entry.get())
            mem.sto(self.ftemp)
        except ValueError :
            print('The value entered was a string.') 
        return

       
    def convert_c(self):
        try:
            words = self.ctext.get()
            self.ctemp = float(words)
            self.fahrenheit_entry.delete(0, END)
            self.fahrenheit_entry.insert(0, '%.2f' % (self.tofahr(self.ctemp)))
            mem.sto(self.fahrenheit_entry.get())
            self.kelvin_entry.delete(0, END)
            self.kelvin_entry.insert(0, '%.2f' % (self.tokel(self.ctemp)))
            mem.sto(self.kelvin_entry.get())
            mem.sto(self.ctemp)
        except ValueError :
             print('The value entered was a string.') 
    def convert_k(self):
        try:
            words = self.ktext.get()
            self.ktemp = float(words)
            self.fahrenheit_entry.delete(0, END)
            self.fahrenheit_entry.insert(0, '%.2f' % (self.tofahr(self.ktoc(self.ktemp))))
            mem.sto(self.fahrenheit_entry.get())
            mem.sto(self.ktemp)
            self.celsius_entry.delete(0, END)
            self.celsius_entry.insert(0, '%.2f' % (self.ktoc(self.ktemp)))
            mem.sto(self.celsius_entry.get())
        except ValueError :
            print('The value entered was a string.')        

    def tocel(self,fahr):
        return (fahr-32) * 5.0 / 9.0

    def tofahr(self,cel):
        return cel * 9.0 / 5.0 + 32

    def ktoc(self,kel):
        return kel - 273.15

    def tokel(self,cel):
        return cel + 273.15
    def clear(self):
         self.fahrenheit_entry.delete(0, END)
         self.celsius_entry.delete(0, END)
         self.kelvin_entry.delete(0, END)



class BaseConverter:
    def __init__(self, nb004):
        self.root = nb004      
        self.create_widgets()

    def create_widgets(self):
        # Number input
        label_number = tk.Label(self.root, text="Enter the number:")
        label_number.grid(row=0, column=0, padx=10, pady=10)
        self.entry_number = tk.Entry(self.root, bd=5)
        self.entry_number.grid(row=0, column=1, padx=10, pady=10)

        # Base of the number
        label_base_from = tk.Label(self.root, text="Base of the number (2-36):")
        label_base_from.grid(row=1, column=0, padx=10, pady=10)
        self.entry_base_from = tk.Entry(self.root, bd=5)
        self.entry_base_from.grid(row=1, column=1, padx=10, pady=10)

        # Target base
        label_base_to = tk.Label(self.root, text="Convert to base (2-36):")
        label_base_to.grid(row=2, column=0, padx=10, pady=10)
        self.entry_base_to = tk.Entry(self.root, bd=5)
        self.entry_base_to.grid(row=2, column=1, padx=10, pady=10)

        # Convert button
        button_convert = tk.Button(self.root, text="Convert", bd=6, command=self.convert)
        button_convert.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Result label
        label_result = tk.Label(self.root, text="Result: ")
        label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Result entry
        self.result_entry = tk.Entry(self.root, bd=10)
        self.result_entry.grid(row=5, column=1, padx=10, pady=10)

    def base_check(self, xnumber, xbase):
        valid_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:int(xbase)]
        for char in xnumber.upper():
            if char not in valid_chars:
                return False
        return True

    def convert_from_10(self, xnumber, xbase):
        arr = []
        while xnumber > 0:
            remainder = xnumber % xbase
            arr.append("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[remainder])
            xnumber = xnumber // xbase
        return ''.join(arr[::-1]) if arr else "0"

    def convert_to_10(self, xnumber, xbase):
        xnumber = xnumber.upper()
        return sum("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(char) * (xbase ** idx) for idx, char in enumerate(xnumber[::-1]))

    def convert(self):
        number = self.entry_number.get().upper()
        base_from = int(self.entry_base_from.get())
        base_to = int(self.entry_base_to.get())
        mem.sto(number)
        mem.sto(base_from)
        mem.sto(base_to)

        # Check if the input number is valid for the source base
        if not self.base_check(number, base_from):
            tk.messagebox.showerror("Invalid Input", f"{number} is not a valid base {base_from} number.")
            return
        
        # Convert to base 10 first
        if base_from == 10:
            number_in_10 = int(number)
        else:
            number_in_10 = self.convert_to_10(number, base_from)
        
        # Convert from base 10 to the target base
        if base_to == 10:
            result = str(number_in_10)
        else:
            result = self.convert_from_10(number_in_10, base_to)
        
        # Display the result in the result entry box
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, result)
        mem.sto(result)




unit_convert = Weight_Length_Liquid_Temperature(tab.f8)




nb.mainloop()

