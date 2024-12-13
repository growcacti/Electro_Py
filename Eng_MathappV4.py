import tkinter as tk
from tkinter import ttk, END, Toplevel,Frame,Entry,Label,Text,Button
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Combobox
from datetime import datetime
import math
import time
import itertools
import threading
import pickle
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
        self.f1 = nb.add_tab('IterCalc')
        ttk.Label(self.f1, text='Iter Calc').grid(row=1,column=1)
        self.f2 = nb.add_tab('OhmsLaw')
        ttk.Label(self.f2, text='O').grid(row=1,column=1)
        self.f3 = nb.add_tab('RF Calc')
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
        ttk.Label(self.f8, text='Common Unit & Number Conversions').grid(row=1,column=1)
        self.f9 = nb.add_tab("Temperature")
        self.f10 = nb.add_tab("Base Number Convert")
        self.f11 = nb.add_tab("Complex Numbers")


        self.f13 = nb.add_tab('MEM')
        ttk.Label(self.f13, text='Memory History').grid(row=0,column=1)
        ttk.Label(self.f13, text='Load Previous Stored History').grid(row=0,column=10)
        self.f14 = nb.add_tab('')
        ttk.Label(self.f14, text='').grid(row=1,column=1)
        self.f15 = nb.add_tab('Other Convert')
        ttk.Label(self.f15, text='Create Convert List').grid(row=0,column=2)
        
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




CACHE_FILE = "resistance_cache.pkl"

class ReverseParallelResistanceCalculator:
    def __init__(self, ffr2):
        self.ffr2 = ffr2       
        self.var_standard_values_list = tk.BooleanVar()
        self.series_var = tk.StringVar(self.ffr2)
        self.series_var.set('All')  # default option
        self.tolerance_var = tk.DoubleVar(self.ffr2)
        self.tolerance_var.set(0.001)  # default tolerance
        self.var_multiple_resistors = tk.IntVar()
        self.values = []
        
        # Generate values from 1.00 to 9.99 with 0.01 step
        self.base_standard_values = [round(x * 0.01, 2) for x in range(100, 1000)]
        self.multipliers = [1, 10, 100, 1000, 10000, 1000000, 10000000, 100000000]
        self.standard_values = [value * multiplier for value in self.base_standard_values for multiplier in self.multipliers]
        self.base_standard_values_list = [
            1.00, 1.01, 1.02, 1.04, 1.05, 1.06, 1.07, 1.09, 1.10,
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
            9.65, 9.76, 9.88, 2.20, 2.70, 3.00, 3.30, 3.60, 3.90,
            4.30, 5.10, 5.60, 6.20, 6.80, 8.20, 9.10, 1.00, 2.00,
            3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00
        ]

        self.standard_values_list = [value * multiplier for value in self.base_standard_values_list for multiplier in self.multipliers]

        self.cache = self.load_cache()
        self.create_widgets()

    def create_widgets(self):
        # Create and place widgets
        self.status_label = tk.Label(self.ffr2, text="")
        self.status_label.grid(row=16, column=0, columnspan=2, pady=10)
        self.resistor_entries = []
        self.entry_label = tk.Label(self.ffr2, text="Enter Desired Resistance (Ω):")
        self.entry_label.grid(row=0, column=1, padx=10, pady=10)
        self.entry_desired_resistance = tk.Entry(self.ffr2)
        self.entry_desired_resistance.grid(row=1, column=1, padx=10, pady=10)
        self.checkbutton_for_standard_values_list = tk.Checkbutton(self.ffr2, text="Use standard resistors in list", variable=self.var_standard_values_list, command=self.toggle_standard_resistor_list)
        self.checkbutton_for_standard_values_list.grid(row=5, column=1, columnspan=2)
        self.checkbutton_multiple_resistors = tk.Checkbutton(self.ffr2, text="Use multiple resistors", variable=self.var_multiple_resistors, command=self.toggle_resistor_entry)
        self.checkbutton_multiple_resistors.grid(row=4, column=0, columnspan=2)

        self.entry_num_resistors = tk.Entry(self.ffr2)
        self.entry_num_resistors.grid(row=8, column=1, padx=10, pady=10)
        self.entry_num_resistors.insert(0, "2")  # Default number of resistors
        self.entry_num_resistors.config(state=tk.DISABLED)

        self.label_num_resistors = tk.Label(self.ffr2, text="Number of Resistors:")
        self.label_num_resistors.grid(row=10, column=0, padx=10, pady=10)

        self.submit_button = tk.Button(self.ffr2, text="Calculate", command=self.on_submit)
        self.submit_button.grid(row=13, column=0, columnspan=2, pady=10)

        self.clear_button = tk.Button(self.ffr2, text="Clear", command=self.clear_text_area)
        self.clear_button.grid(row=14, column=0, columnspan=2, pady=10)

        self.text_area = tk.Text(self.ffr2, height=10, width=50)
        self.text_area.grid(row=15, column=0, columnspan=2, padx=10, pady=10)

        self.update_resistor_entries(2)

    def update_resistor_entries(self, num_resistors):
        # Clear existing entries
        for entry in self.resistor_entries:
            entry.destroy()

        self.resistor_entries = []
        for i in range(num_resistors):
            entry = tk.Entry(self.ffr2, state=tk.NORMAL if self.var_multiple_resistors.get() else tk.DISABLED)
            entry.grid(row=17 + i, column=1, padx=10, pady=2)
            self.resistor_entries.append(entry)

    def toggle_standard_resistor_list(self):
        # Toggle between the standard values list and base standard values
        if self.var_standard_values_list.get():
            self.standard_values = self.standard_values_list
        else:
            self.standard_values = [value * multiplier for value in self.base_standard_values for multiplier in self.multipliers]

    def on_submit(self):
        self.status_label.config(text="Calculating... Please wait.")
        calculation_thread = threading.Thread(target=self.start_calculation, daemon=True)
        calculation_thread.start()

    def generate_combinations(self, desired_resistance, max_num_resistors, tolerance=0.001):
        found_combinations = False
        cache_key = (desired_resistance, max_num_resistors, tolerance)

        # Check if the combination is already in the cache
        if cache_key in self.cache:
            for combination in self.cache[cache_key]:
                yield combination
            return

        # If not in cache, calculate it
        self.cache[cache_key] = []
        for num_resistors in range(2, max_num_resistors + 1):
            for combination in itertools.combinations_with_replacement(self.standard_values, num_resistors):
                combined_resistance = self.parallel_resistance(combination)
                error = abs((combined_resistance - desired_resistance) / desired_resistance)
                if error <= tolerance:
                    print(f"Testing combination {combination}: {combined_resistance}Ω, Error: {error}")  # Debug print
                    found_combinations = True
                    result = (*combination, combined_resistance, error)
                    self.cache[cache_key].append(result)
                    yield result
            if found_combinations:
                break

        if not found_combinations:
            self.cache[cache_key].append(None)
            yield None

        # Save the updated cache to the file
        self.save_cache()

    def parallel_resistance(self, resistors):
        inverse_sum = sum(1/r for r in resistors)
        return 1 / inverse_sum if inverse_sum != 0 else float('inf')

    def insert_text(self, text):
        self.text_area.insert(tk.END, text)

    def clear_text_area(self):
        self.text_area.delete('1.0', tk.END)

    def start_calculation(self):
        try:
            desired_resistance = float(self.entry_desired_resistance.get())
            max_num_resistors = int(self.entry_num_resistors.get())
            self.combinations_found = False

            for combination in self.generate_combinations(desired_resistance, max_num_resistors):
                if combination is None:
                    if not self.combinations_found:
                        self.ffr2.after(0, self.insert_text, "No combinations found within the specified tolerance.\n")
                    break

                self.combinations_found = True
                res = combination[-2]
                err = combination[-1]
                resistors = ", ".join(f"{r}Ω" for r in combination[:-2])
                display_text = f"{resistors} -> {res:.2f}Ω (Error: {err*100:.2f}%)\n"
                self.ffr2.after(0, self.insert_text, display_text)

            if not self.combinations_found:
                self.ffr2.after(0, self.insert_text, "Checked all combinations. No matches found.\n")

            # Update the status label to indicate completion
            self.ffr2.after(0, self.update_status, "Calculation complete.")
        except ValueError:
            self.ffr2.after(0, self.update_status, "Invalid input. Please enter valid numbers.")

    def toggle_resistor_entry(self):
        if self.var_multiple_resistors.get() == 1:
            # Checkbutton is checked, enable the entry field
            self.entry_num_resistors.config(state=tk.NORMAL)
        else:
            # Checkbutton is unchecked, disable the entry field and reset its value
            self.entry_num_resistors.config(state=tk.DISABLED)
            self.entry_num_resistors.delete(0, tk.END)
            self.entry_num_resistors.insert(0, "2")  # Default value when disabled

    def update_status(self, message):
        self.status_label.config(text=message)

    def load_cache(self):
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, 'rb') as f:
                return pickle.load(f)
        return {}

    def save_cache(self):
        with open(CACHE_FILE, 'wb') as f:
            pickle.dump(self.cache, f)









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
reverse_calc = ReverseParallelResistanceCalculator(ffr2)
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

nb002.add(ffm0, text='Retrun Loss & VSWR')
nb002.add(ffm1, text='Frequency Wavelength')
nb002.add(ffm2, text='Attenuator Calculation')
nb002.add(ffm3, text = 'dBm & Watts')
nb002.add(ffm4, text ='air coil Inductor calc')
nb002.add(ffm5, text ='PPM')
nb002.add(ffm6, text =' ')

vswr = Vswr(ffm0)
freqency_wavelength(ffm1)
attenuator_calculator(ffm2)
rf_pwr_converter(ffm3)
coil_calc = InductanceCalculator(ffm4)
ppm = PPM(ffm5)

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
    tk.Label(frm1, text='Answer from Entry 3&4 Answer6').grid(row=2, column=3)
    tk.Label(frm1, text='From Answer 5&6 ').grid(row=2, column=5)
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
    tk.Label(frm1, text='Answer from Entry 1&2 Answer5').grid(row=2, column=1)
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


unit_conversions = {
    "Length": {
        "inch_to_centimeter": 2.540,
        "millimeter_to_inch": 0.03937,
        "foot_to_centimeter": 30.4878,
        "centimeter_to_inch": 0.3937,
        "yard_to_meter": 0.9144028,
        "meter_to_foot": 3.281,
        "mile_to_kilometer": 1.6093419,
        "kilometer_to_mile": 0.621372,
        "statute_mile_to_kilometer": 1.6093,
        "nautical_mile_to_kilometer": 1.8520,
        "foot_to_meter": 0.3048,
        "yard_to_meter": 0.9144,
        "inch_to_centimeter_2": 2.54,
        "angstrom_to_centimeter": 10**-8,
        "angstrom_to_meter": 10**-10
    },
    "Area": {
        "sq_inch_to_sq_centimeter": 6.4516,
        "sq_centimeter_to_sq_inch": 0.1550,
        "sq_foot_to_sq_meter": 0.0929,
        "sq_meter_to_sq_yard": 1.195986,
        "sq_yard_to_sq_meter": 0.83613,
        "sq_kilometer_to_sq_mile": 0.386101,
        "sq_mile_to_sq_kilometer": 2.589999,
        "hectare_to_acre": 2.471044,
        "acre_to_hectare": 0.404687,
        "sq_kilometer_to_sq_meter": 10**6,
        "sq_kilometer_to_hectare": 100,
        "hectare_to_sq_meter": 10000,
        "acre_to_sq_meter": 4047,
        "acre_to_hectare_2": 0.4047
    },
    "Mass": {
        "grain_to_scruple": 0.05,
        "grain_to_dram": 0.016667,
        "grain_to_ounce": 0.00208,
        "ounce_to_gram": 28.3495,
        "gram_to_ounce": 0.03527396,
        "pound_to_ounce": 16,
        "pound_to_kilogram": 0.4535924,
        "kilogram_to_pound": 2.2046223,
        "short_ton_to_metric_ton": 0.892857,
        "metric_ton_to_short_ton": 1.1200,
        "long_ton_to_metric_ton": 1.01605,
        "metric_ton_to_kilogram": 1000,
        "pound_to_kilogram_2": 0.4535924,
        "ounce_to_gram_2": 28.3495
    },
    "Volume": {
        "teaspoon_to_milliliter": 5,
        "milliliter_to_fluid_ounce": 0.0338147,
        "tablespoon_to_milliliter": 15,
        "liter_to_pint": 2.11342,
        "liter_to_cubic_centimeter": 1000,
        "fluid_ounce_to_milliliter": 30,
        "liter_to_quart": 1.05671,
        "liter_to_gallon": 0.264178,
        "gallon_to_liter": 3.785332,
        "gallon_to_cubic_inch": 231,
        "cup_to_liter": 0.23658,
        "pint_to_liter": 0.473167,
        "cubic_meter_to_cubic_foot": 35.3144,
        "cubic_meter_to_cubic_yard": 1.30794,
        "cubic_foot_to_cubic_meter": 0.0283170,
        "cubic_yard_to_cubic_meter": 0.764559,
        "milliliter_to_cubic_centimeter": 1,
        "cubic_meter_to_liter": 1000,
        "quart_to_liter": 0.9461,
        "gallon_to_liter_2": 3.7854,
        "pint_to_liter_2": 0.4723,
        "fluid_ounce_to_milliliter_2": 29.6
    },
    "Temperature": {
        "fahrenheit_to_celsius": lambda F: (F - 32) * 5/9,
        "celsius_to_fahrenheit": lambda C: (C * 9/5) + 32,
        "celsius_to_kelvin": lambda C: C + 273.15
    },
    "Pressure": {
        "pascal_to_newton_per_square_meter": 1,
        "bar_to_atmosphere": 0.98692,
        "bar_to_pascal": 10**5,
        "psi_to_millibar": 68.97,
        "psi_to_pascal": 6897
    },
    "Energy": {
        "joule_to_newton_meter": 1,
        "calorie_to_joule": 4.184,
        "kWh_to_joule": 3.6 * 10**6,
        "kWh_to_calorie": 8.60 * 10**5
    },
    "Power": {
        "watt_to_joule_per_second": 1,
        "watt_to_calories_per_minute": 14.34
    }
}

def convert(value, conversion_key):
    """
    Converts a value using the given conversion key.

    Parameters:
    value (float): The value to be converted.
    conversion_key (str): The conversion key (e.g., "inch_to_centimeter").

    Returns:
    float: The converted value.
    """
    # Special case for temperature conversions
    if conversion_key in ["fahrenheit_to_celsius", "celsius_to_fahrenheit", "celsius_to_kelvin"]:
        return unit_conversions["Temperature"][conversion_key](value)
    
    # Find the appropriate conversion factor in the dictionary
    for category in unit_conversions:
        if conversion_key in unit_conversions[category]:
            conversion_factor = unit_conversions[category][conversion_key]
            return value * conversion_factor

    raise ValueError("Conversion not found in the dictionary")

# Define the GUI application
class UnitConverter:
    def __init__(self, root):
        self.root = root
        
        # Create and set the layout
        self.create_widgets()
    
    def create_widgets(self):
        # Input value
        tk.Label(self.root, text="Value:").grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.value_entry = tk.Entry(self.root, bd=9,bg="seashell")
        self.value_entry.grid(row=0, column=1, padx=10, pady=5)
        
        # Category
        ttk.Label(self.root, text="Category:").grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.category_combobox = ttk.Combobox(self.root, values=list(unit_conversions.keys()))
        self.category_combobox.grid(row=3, column=1, padx=10, pady=5)
        self.category_combobox.bind("<<ComboboxSelected>>", self.update_conversion_options)
        
        # Conversion key
       
        self.conversion_combobox = ttk.Combobox(self.root)
        self.conversion_combobox.grid(row=4, column=1, padx=10, pady=5)
        
        # Convert button
        self.convert_button = tk.Button(self.root, text="Convert", command=self.perform_conversion)
        self.convert_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
        
        # Result
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
        self.e2 = tk.Entry(self.root,bd=11,bg="wheat",width=40)
        self.e2.grid(row=8, column=1)
    def update_conversion_options(self, event):
        selected_category = self.category_combobox.get()
        if selected_category in unit_conversions:
            self.conversion_combobox['values'] = list(unit_conversions[selected_category].keys())
    
    def perform_conversion(self):
        try:
            value = float(self.value_entry.get())
            conversion_key = self.conversion_combobox.get()
            result = convert(value, conversion_key)
            to_unit = conversion_key.split("_to_")[1]
            self.result_label.config(text=f"Result: {result:.6f} {to_unit}")
            self.e2.delete(0, END)
            self.e2.insert(END, f"{result:.6f}")
            mem.sto(self.e2.get())
        except ValueError as e:
            messagebox.showerror("Conversion Error", f"Error: {e}")


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


unit_convert = UnitConverter(tab.f8)
temp_convert = Temperature_converter(tab.f9)




class BaseConverter:
    def __init__(self, root):
        self.root = root
        tk.Label(root, text="Number:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_number = tk.Entry(root)
        self.entry_number.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="From Base (2-36):").grid(row=1, column=0, padx=10, pady=10)
        self.entry_from_base = tk.Entry(root)
        self.entry_from_base.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(root, text="To Base (2-36):").grid(row=2, column=0, padx=10, pady=10)
        self.entry_to_base = tk.Entry(root)
        self.entry_to_base.grid(row=2, column=1, padx=10, pady=10)

        button_convert = tk.Button(root, text="Convert", command=self.convert)
        button_convert.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.label_result = tk.Label(root, text="Result:")
        self.label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    # Function to convert a number from one base to another
    def base_convert(self, number, from_base, to_base):
        # Convert the number to base 10
        try:
            base10_number = int(number, from_base)
        except ValueError:
            return None
        
        # Convert the base 10 number to the target base
        if base10_number == 0:
            return '0'
        
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        
        while base10_number > 0:
            result = digits[base10_number % to_base] + result
            base10_number //= to_base
        
        return result

    # Function to handle the convert button click
    def convert(self):
        number = self.entry_number.get().strip()
        from_base = self.entry_from_base.get().strip()
        to_base = self.entry_to_base.get().strip()
        
        # Validate the input
        if not number or not from_base or not to_base:
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return
        
        try:
            from_base = int(from_base)
            to_base = int(to_base)
        except ValueError:
            messagebox.showerror("Input Error", "Bases must be integers.")
            return
        
        if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
            messagebox.showerror("Input Error", "Bases must be between 2 and 36.")
            return
        
        # Perform the conversion
        converted = self.base_convert(number, from_base, to_base)
        if converted is None:
            messagebox.showerror("Conversion Error", "Invalid number for the specified base.")
        else:
            self.label_result.config(text=f"Result: {converted}")


base_number_converter =BaseConverter(tab.f10)


import tkinter as tk
from tkinter import messagebox
import math


class ComplexCalculatorGUI:
    def __init__(self, parent):
        self.parent = parent   
        self.create_widgets()
        
    def create_widgets(self):
        # Input fields for the first complex number
        tk.Label(self.parent, text="First Complex Number (a+bi):").grid(row=0, column=0, columnspan=2)
        tk.Label(self.parent, text="Real:").grid(row=1, column=0)
        self.real1_entry = tk.Entry(self.parent)
        self.real1_entry.grid(row=1, column=1)
        tk.Label(self.parent, text="Imaginary:").grid(row=2, column=0)
        self.imag1_entry = tk.Entry(self.parent)
        self.imag1_entry.grid(row=2, column=1)

        # Input fields for the second complex number
        tk.Label(self.parent, text="Second Complex Number (a+bi):").grid(row=3, column=0, columnspan=2)
        tk.Label(self.parent, text="Real:").grid(row=4, column=0)
        self.real2_entry = tk.Entry(self.parent)
        self.real2_entry.grid(row=4, column=1)
        tk.Label(self.parent, text="Imaginary:").grid(row=5, column=0)
        self.imag2_entry = tk.Entry(self.parent)
        self.imag2_entry.grid(row=5, column=1)

        # Operation buttons
        tk.Button(self.parent, text="+", command=lambda: self.operate('+')).grid(row=6, column=0)
        tk.Button(self.parent, text="-", command=lambda: self.operate('-')).grid(row=6, column=1)
        tk.Button(self.parent, text="*", command=lambda: self.operate('*')).grid(row=7, column=0)
        tk.Button(self.parent, text="/", command=lambda: self.operate('/')).grid(row=7, column=1)
        tk.Button(self.parent, text="Mod", command=self.modulus).grid(row=8, column=0, columnspan=2)

        # Label to display the result
        self.result_label = tk.Label(self.parent, text="Result will be shown here")
        self.result_label.grid(row=9, column=0, columnspan=2)

    def operate(self, operation):
        try:
            c1 = Complex(float(self.real1_entry.get()), float(self.imag1_entry.get()))
            c2 = Complex(float(self.real2_entry.get()), float(self.imag2_entry.get()))
            if operation == '+':
                result = c1 + c2
            elif operation == '-':
                result = c1 - c2
            elif operation == '*':
                result = c1 * c2
            elif operation == '/':
                result = c1 / c2
            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

    def modulus(self):
        try:
            c1 = Complex(float(self.real1_entry.get()), float(self.imag1_entry.get()))
            result = c1.mod()
            self.result_label.config(text=f"Modulus: {result.real:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

complex_nubers = ComplexCalculatorGUI(tab.f11)


nb.mainloop()

