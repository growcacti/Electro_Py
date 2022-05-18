import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import tkinter.font
import math
import subprocess
import os
import runpy
from tkinter import filedialog as fd, messagebox
from tkinter.scrolledtext import ScrolledText
 
 
r = tk.Tk()
r.geometry('1200x800')
r.title("Electro PY Engineering Application")
notebook = ttk.Notebook(r)
f0 = ttk.Frame(notebook)
notebook.grid(row=0, column=0)
def titlepage():
    t_str=""" Electro Py Engineering Caculation Program """
notebook.add(f0, text="MAIN")
f1 = ttk.Frame(notebook)
notebook.add(f1, text='Ohms Law')
def fontfamily():
    pass
def foo():
 
    runpy.run_module('font2list')
    
    
def codeview():
    
    runpy.run_module('codeview')
def spec():
    
    runpy.run_module('spec')
          
#------------------------------------------------
# TAB1 & 2 create
#------------------------------------------------
f2 = ttk.Frame(notebook)

notebook.add(f2, text='Sci_Calc')
def lc():
    runpy.run_module('SciCalcV3')
    
def keypad():
    runpy.run_module('symbol_pad_JH')

#--------------------------------------------------------
# TAB 3 - 10 Create
#---------------------------------------------------------
f3 = ttk.Frame(notebook, height=100, width=200)
notebook.add(f3, text='Base # Converter')
f4 = ttk.Frame(notebook, height=100, width=100)
notebook.add(f4, text='Resonant Freq Calc')


def sinewave():
    runpy.run_module('sinewave')
def cosine():
    runpy.run_module('cosine')
def waveform1():
     runpy.run_module('waveform1')
def waveform2():
     runpy.run_module('waveform2')
     
def waveform3():
     runpy.run_module('waveform3')

def waveform4():
     runpy.run_module('waveform4')


def waveform5():
     runpy.run_module('waveform5')
f5 = ttk.Frame(notebook)
notebook.add(f5, text='Adj Graphs Experimental')

label113 = tk.Label(f5, text="Adjustable Graph Experiment on Canvas Widget", font=("Arial", 16)).grid(row=0, column=3)
label21 = tk.Label(f5, text="   ", font=("Arial", 14)).grid(row=2, column=1)
label22 = tk.Label(f5, text="   ", font=("Arial", 14)).grid(row=1, column=2)
bt113=tk.Button(f5, text='Adj Sinewave graph', bd=7, bg="ivory2", command=sinewave)
bt113.grid(column=3, row=3)
bt224=tk.Button(f5, text='Adj Cosine Graph', bd=7, bg="cornsilk", command=cosine)
bt224.grid(column=3, row=4)
bt334=tk.Button(f5, text='Adj waveform1', bd=7, bg="orange", command=waveform1)

bt334.grid(column=3, row=5)
bt445=tk.Button(f5, text='Adj waveform2', bd=7, bg="light green", command=waveform2)

bt445.grid(column=3, row=6)
bt556=tk.Button(f5, text='Adj waveform3', bd=7, bg="violet", command=waveform3)

bt556.grid(column=3, row=7)
bt667=tk.Button(f5, text='Adj waveform4', bd=7, bg="cyan", command=waveform4)
bt667.grid(column=3, row=8)
bt668=tk.Button(f5, text='Adj waveform5', bd=7, bg="hot pink", command=waveform5)
bt668.grid(column=3, row=9)
f6 = ttk.Frame(notebook)
notebook.add(f6, text='Digital Info')


														
info_str = """	AND Gate					OR Gate					NOR			
														
	Input1	Input2		Output		Input1	Input2		Output		Input1	Input2		Output
	0	0		0		0	0	0	0		0	0	0	1
	0	1		0		0	1	1	1		0	1	1	0
	1	0		0		1	0	1	1		1	0	1	0
	1	1		1		1	1	2	1		1	1	1	0
														
														
	NAND					XOR					XNOR			
														
	Input1	Input2		Output		Input1	Input2		Output		Input1	Input2		Output
	0	0	0	1		0	0	0	0		0	0	0	1
	0	1	0	1		0	1	1	1		0	1	1	0
	1	0	0	1		1	0	1	1		1	0	1	0
	1	1	1	0		1	1	2	0		1	1	2	1
														
	NOT													
														
	Input1		Output											
	0		1											
	1		0  """

textbox = tk.Text(f6, height= 40, width=400, bg="azure")
textbox.grid(row=1, column=1)

textbox.insert('1.0', info_str)

f7 = ttk.Frame(notebook)
notebook.add(f7, text='RF PWR & Freq')
f8 = ttk.Frame(notebook)
notebook.add(f8, text='LED Calc')
f9 = ttk.Frame(notebook)
notebook.add(f9, text='VSWR to RL')



def command():
    pass

def mod1():
    runpy.run_module('Ohms_Law_Singlecalc_v2')
def mod2():
    runpy.run_module('RPcalc')

def mod3():
    runpy.run_module('IPcalc')

def mod4():
    runpy.run_module('VPcalc')
  
def lc_freq():
    runpy.run_module('LC_Freq')
def scicalc():
    runpy.run_module('SciCalcV3')
def cc():
    runpy.run_module('Custom_Calc')
    
def lm317t():
     runpy.run_module('LM317T_calc')
def vdiv():
     runpy.run_module('Vdiv')
def parallel_res():
    runpy.run_module('select_resistor')                   

label1 = tk.Label(f0, text="              ", font=("Arial", 14)).grid(row=2, column=0)
label2 = tk.Label(f0, text="              ", font=("Arial", 14)).grid(row=1, column=0)
label3 = tk.Label(f0, text="              ", font=("Arial", 14)).grid(row=3, column=0)
####
label1 = tk.Label(f0, text="Electro PY Calculation Application", bg="light blue", font=("Chancery Uralic", 18)).grid(row=0, column=5)
label2 = tk.Label(f0, text="JH APPS", bg="light blue", font=("Chancery Uralic", 18)).grid(row=1, column=5)
label3 = tk.Label(f0, text=" Various Tabs have different engineering calculators", bg="light green", font=("Chancery Uralic", 14)).grid(row=3, column=5)
####
tkbtn1 = tk.Button(f0, text='Calculate +\- Spec', bd=10, bg="ivory2", command=spec)
tkbtn1.grid(column=5, row=5)
######
tkbtn2 = tk.Button(f0, text='CodeView', bd=10, bg="ivory", command=codeview)
tkbtn2.grid(column=5, row=6)
######
tkbtn3 = tk.Button(f0, text='Char Keypad', bd=10, bg="plum", command=keypad)
tkbtn3.grid(column=5, row=7)
######
tkbtn4 = tk.Button(f0, text='Button', bd=10, bg="lawn green", command=foo)
tkbtn4.grid(column=5, row=8)
######
    
btn1=tk.Button(f1, text='Ohms Law Calc', bd=10, bg="azure", command=mod1)
btn1.grid(column=0, row=3)
btn2=tk.Button(f1, text='Calc Resistance & Pwr', bd=10, bg="lavender", command=mod2)
btn2.grid(column=0, row=4)
btn3=tk.Button(f1, text='Calc Current & Pwr', bd=10, bg="cyan2", command=mod3)
btn3.grid(column=0, row=5)
btn4=tk.Button(f1, text='Volts & Pwr', bd=10, bg="violet", command=mod4)
btn4.grid(column=0, row=6)
btn5=tk.Button(f1, text='Parallel Resistor Calc', bd=10, bg="lime green", command=parallel_res)
btn5.grid(column=0, row=7)
btn6=tk.Button(f1, text='LM317T Reg Calc 2 Resistor', bd=10, bg="orange", command=lm317t)
btn6.grid(column=0, row=8)
btn6=tk.Button(f1, text='Resistor Voltage Divider Calc ', bd=10, bg="orange", command=vdiv)
btn6.grid(column=0, row=9)
awg_str ="""  """
#--------------------------------------
#   TAB2 STUFF Sci Calc Eng, Info Label  
#--------------------------------------

frm1 = tk.Frame(f2, width=1000, height=40, background="snow")
frm1.grid(row=0, column=0, columnspan=6)
tkbtn4 = tk.Button(frm1, text='Calculator', bd=10, bg="pink", command=scicalc)
tkbtn4.grid(column=5, row=8)
tkbtn5 = tk.Button(frm1, text='Custom Step Calculator', bd=10, bg="lime green", command=cc)
tkbtn5.grid(column=6, row=8)
##frm2 = tk.Frame(f2, width=300, height=300, background="light blue")
##frm2.grid(row=3, column=2)
##frm3 = tk.Frame(f2, width=500, height=100, background="wheat")
##frm3.grid(row=6, column=5)
##frm4 = tk.Frame(f2, width=300, height=300, background="light green")
##frm4.grid(row=8, column=8)


##txt_str= """''tera'   : (1000000000000, 10**12),
##'giga'   : (1000000000, 10**9),
##'mega'   : (1000000, 10**6),
##'kilo'   : (1000, 10**3),
##'hecta'  : (100, 10**2),
##'deca'   : (10, 10),
##'base'   : (1,1),
##'deci'   : (0.1, 10**-1),
##'centi'  : (0.01, 10**-2),
##'milli'  : (0.001, 10**-3),
##'micro'  : (0.000001, 10**-6),
##'nano'   : (0.000000001, 10**-9)
##'pico'   : (0.000000000001, 10**-12)
##
##"""
##tk.Label(f2, text=txt_str).grid(row=3, column=3)
#
#----------------------------------------------
#  TAB3  Number Base Converter
#----------------------------------------------

def bin2dec():
    runpy.run_module('FBIN')
    #subprocess.run("python3", "FBIN") 
def fromhex():
    runpy.run_module('FHEX')
def fromoct():
    runpy.run_module('FOCT')
def frombase():
    runpy.run_module('DEC_2_36')
def dectobin():
    runpy.run_module('Dec2Bin')
def infosec():
    runpy.run_module('Info_Section')
        
btn11=tk.Button(f3, text='Decimal to Base 2 to 36', bd=10, bg="lawn green", command=frombase)
btn11.grid(column=3, row=3)
btn22=tk.Button(f3, text='HEX to DEC BIN OCT', bd=10, bg="hot pink", command=fromhex)
btn22.grid(column=3, row=4)
btn33=tk.Button(f3, text='OCTAL TO DEC, HEX, BIN', bd=10, bg="violet", command=fromoct)
btn33.grid(column=3, row=5)
btn44=tk.Button(f3, text='BIN TO OCT, DEC, HEX', bd=10, bg="light blue", command=bin2dec)
btn44.grid(column=3, row=6)
btn55=tk.Button(f3, text='DEC to BIN', bd=10, bg="wheat", command=dectobin)
btn55.grid(column=3, row=7)
btn66=tk.Button(f3, text='INFO', bd=10, bg="magenta", command=infosec)
btn66.grid(column=3, row=8)
tk.Label(f3, text="Base Converter").grid(column=3, row=1)


#--------------------------------------
#   TAB4 Resonant Frequency Calc
#--------------------------------------
def lc_freq():
    runpy.run_module('LC_Freq')

def lfreq():
    runpy.run_module('Freq_L_find_C')

def cfreq():
    runpy.run_module('Freq_C_find_L')


def air_core():
    runpy.run_module('Air_Core')
    

btn77 = tk.Button(f4, text="LC Resonant Freq Calc",  bd=10, bg="orange", command=lc_freq)
btn77.grid(column=3, row=3)
btn78 = tk.Button(f4, text="Freq L Calc find C", bd=10, bg="violet", command=lfreq)
btn78.grid(column=3, row=4)
btn79 = tk.Button(f4, text="Freq C Calc find L", bd=10, bg="light blue", command=cfreq)
btn79.grid(column=3, row=5)
btn80 = tk.Button(f4, text="Air Core Inductor Calculator", bd=10, bg="cyan2", command=air_core)
btn80.grid(column=3, row=6)


tk.Label(f7, text="RF PWR Convert").grid(column=3, row=1)

def wv():
    
    runpy.run_module('dbm2w_v_rmsv2')



def dbm():
    runpy.run_module('mW2dBm')

def led():
    runpy.run_module('LED_Current_Limit_calc')

def vswr():
    runpy.run_module('vswer_to_Returnlossv4')


def open_file():
    """Open a file for editing."""
    filepath = fd.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
def save_file():
    """Save the current file as a new file."""
    filepath = fd.asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
def clear():
    txt_edit.delete("1.0", tk.END)




def fmf():
    runpy.run_module('Frequency2Meters')


def lenghttofreq():
    runpy.run_module('LenghttoFreq')
    
def temperature():
    runpy.run_module('temperature_converter')
def mikm():
    runpy.run_module('km_mi')
def incm():
    runpy.run_module('inch_cm_mm')

def collatz():
    runpy.run_module('collatz_conjecture')    




    
f10 = ttk.Frame(r)
notebook.add(f10, text='Text Edit')
btn111=tk.Button(f7, text='dBm to Watts & Volts', bd=10, bg="orange", command=wv)
btn111.grid(column=1, row=3)
btn333=tk.Button(f7, text='Millwatts to dBm', bd=10, bg="cyan", command=dbm)
btn333.grid(column=1, row=5)
btn777=tk.Button(f7, text='Frequency to Meters', bd=10, bg="magenta", command=fmf)
btn777.grid(column=1, row=7)

btn778=tk.Button(f7, text='Length to Frequency', bd=10, bg="pink", command=lenghttofreq)
btn778.grid(column=1, row=8)

tt = tk.Label(f8, text="LED Resistor Calc", bg="magenta2")
tt.grid(row=0, column=1)
btn888=tk.Button(f8, text='LED Current Limit Resistor Calc', bd=10, bg="orange", command=led)
btn888.grid(column=1, row=3)

ttt=tk.Label(f9, text="VSWR to Return Loss dB Conversion", bg="ivory")
ttt.grid(row=0, column=1)
btn999=tk.Button(f9, text='Load Vswr to RL', bd=10, bg="seashell", command=vswr)
btn999.grid(column=1, row=3)

def ggtxt():
   
    
    a = """
AC power conversion table
		
Vp-p	Vrms	dBm
1.00	0.35	3.97
2.00	0.71	10.00
3.00	1.06	13.52
4.00	1.41	16.02
5.00	1.77	17.95
6.00	2.12	19.54
7.00	2.47	20.88
8.00	2.83	22.04
9.00	3.18	23.06
10.00	3.53	23.97
11.00	3.89	24.80
12.00	4.24	25.56
13.00	4.59	26.25
14.00	4.95	26.90
15.00	5.30	27.50
16.00	5.65	28.06
17.00	6.01	28.58
18.00	6.36	29.08
19.00	6.71	29.55
20.00	7.07	30.00
		"""
    txt_edit.insert(tk.END, a)

txt_edit = tk.Text(f10, height=500, width=500)
fr_buttons = tk.Frame(f10, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", bd=10, bg="orange", command=open_file)
btn_open.grid(row=1, column=0)
btn_save = tk.Button(fr_buttons, text="Save As...", bd=10, bg="light blue", command=save_file)
btn_save.grid(row=2, column=0)
btn_clear = tk.Button(fr_buttons, text="Clear", bd=10, bg="light green", command=clear)
btn_clear.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_grab = tk.Button(fr_buttons, text="Grab", bd=10, bg="pink", command=ggtxt)
btn_grab.grid(row=4, column=0)
#btn_find = tk.Button(fr_buttons, text="Find", command=find_func)
#btn_find.grid(row=5, column=0)
#btn_replace = tk.Button(fr_buttons, text="Replace", command=replace)
#btn_replace.grid(row=6, column=0)
#btn_s.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
f11 = ttk.Frame(notebook)
notebook.add(f11, text='Unit Convert')

bt1=tk.Button(f11, text='Temperature Converter °F & °C', bd=5, bg="cornsilk", command=temperature)
bt1.grid(column=1, row=3)
bt3=tk.Button(f11, text='Miles & Kilometers',bd=5, bg="light blue", command=mikm)
bt3.grid(column=1, row=5)
bt4=tk.Button(f11, text='inch & cm with mm', bd=5, bg="orange", command=incm)
bt4.grid(column=1, row=7)


f12 = ttk.Frame(r)
notebook.add(f12, text='Experimental')
tk.Label(f12, text="This an experimental part of this application").grid(row=0, column=0)
tk.Label(f12, text="Unpredictable results may occur").grid(row=1, column=0)
bt711=tk.Button(f12, text='Random Collatz Conjecture Fun!!', bd=10, bg="cyan2", command=collatz)
bt711.grid(column=0, row=3)
if __name__ == '__main__':
    r.mainloop()


