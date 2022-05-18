#!/usr/bin/env python

import tkinter as tk
from tkinter import WORD
#Brought to you from JH APPS
root = tk.Tk()

keys = [
     "\u03C8",  "\u03C1", "\u03C2", "\u03BF", "\u03F0", "\u03F4", "\u03CE" , "\u03DE", "\u03DF", "\u03C0", "\u0394",
    '\u2211', '\u2220','\u222A', '\u2210', '\u221A', '\u221B', '\u221C',  '\u221D','\u2128', '\u2122', '\u2125', '\u223F', '\u00AE',
    '\u00B0', '\u00B5', '\u00BF', '\u00A3', '\u2150', '\u2151', '\u2152', '\u22BF', '\u2154', '\u2155', '\u2156',
    '\u2157', '\u2158', '\u2159', '\u215A', '\u215B', '\u215C', '\u215D', '\u1E9F', '\u2123', '\u222B', '\u0395',
    '\u03bE',
]

curBut = [-1,-1]
buttonL = [[]]
frm = tk.Frame(root)
frm.grid(row=10, column=5, columnspan=10)
sp = tk.Spinbox(frm, from_ = 12, to = 120, increment=1)
sp.grid(row=10, column=0)

entry = tk.Text(root, width=15, height=3)
entry.configure(wrap=WORD)
entry.grid(row=0, column=0, columnspan=20)
entry.configure(font=("Ariel", sp.get()))
varRow = 1
varColumn = 0
# add menu bar with clipboard options
def use_clipboard(paste_text=None):
    clipboard_text = entry.get(tk.END, '1.0')
    #root.withdraw()
    if type(clipboard_text) == str: # Set clipboard text.
        root.clipboard_clear()
        root.clipboard_append(clipboard_text)
        print(clipboard_text)
    try:
        clipboard_text = root.clipboard_get()
    except tk.TclError:
        clipboard_text = ''
    root.update() # Stops a few errors (clipboard text unchanged, command line program unresponsive, window not destroyed).
    #root.destroy()
    
    return clipboard_text

    
    
def chg_font():
    size = sp.get()
    entry.configure(font=("Ariel", size))
    

def leftKey(event):
    if curBut == [-1,-1]:
        curBut[:] = [0,0]
        buttonL[0][0].configure(highlightbackground='red')
    elif curBut[0] == 4:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
        curBut[:] = [0,10]
        buttonL[0][10].configure(highlightbackground='red')
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
        curBut[:] = [curBut[0], (curBut[1]-1)%11]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
    buttonL[curBut[0]][curBut[1]].focus_set()

def rightKey(event):
    if curBut == [-1,-1]:
        curBut[:] = [0,0]
        buttonL[0][0].configure(highlightbackground='red')
    elif curBut[0] == 4:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
        curBut[:] = [0,0]
        buttonL[0][0].configure(highlightbackground='red')
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
        curBut[:] = [curBut[0], (curBut[1]+1)%11]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
    buttonL[curBut[0]][curBut[1]].focus_set()

def upKey(event):
    if curBut == [-1,-1]:
        curBut[:] = [0,0]
        buttonL[0][0].configure(highlightbackground='red')
    elif curBut[0] == 0:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
        curBut[:] = [(curBut[0]-1)%5, 0]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
    elif curBut[0] == 4:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
        curBut[:] = [(curBut[0]-1)%5, 5]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
        curBut[:] = [(curBut[0]-1)%5, curBut[1]]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
    buttonL[curBut[0]][curBut[1]].focus_set()

def downKey(event):
    if curBut == [-1,-1]:
        curBut[:] = [0,0]
        buttonL[0][0].configure(highlightbackground='red')
    elif curBut[0] == 3:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
        curBut[:] = [(curBut[0]+1)%5, 0]
        buttonL[curBut[0]][curBut[1]%11].configure(highlightbackground='red')
    elif curBut[0] == 4:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
        curBut[:] = [(curBut[0]+1)%5, 5]
        buttonL[curBut[0]][curBut[1]%11].configure(highlightbackground='red')
    else:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
        curBut[:] = [(curBut[0]+1)%5, curBut[1]]
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='red')
    buttonL[curBut[0]][curBut[1]].focus_set()

def select(value, x, y):
    if curBut != [-1,-1]:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground='#d9d9d9')
        buttonL[curBut[0]][curBut[1]].configure(highlightcolor='#d9d9d9')
    curBut[:] = [x,y]
    buttonL[x][y].configure(highlightbackground='red')
    buttonL[x][y].configure(highlightcolor='red')
    if value == "DEL":
        input_val = entry.get("1.0", 'end-2c')
        entry.delete("1.0", "end")
        entry.insert("1.0", input_val, "end")
    elif value == "SPACE":
        entry.insert("insert", ' ')
    elif value == "TAB":
        entry.insert("insert", '   ')
    else:
        entry.insert("end", value)
# Below us the for loop that kicks out the keyboard like buttons
# variable but and current button is butcur
for button in keys:
 
    but = tk.Button(root, text=button, width=5, bg="#000000", fg="#ffffff", highlightthickness=4, 
                   activebackground="gray65", highlightcolor='red', activeforeground="#000000", relief="raised", padx=12,
                   pady=4, bd=7, command=lambda x=button, i=varRow-1, j=varColumn + 1: select(x, i, j))
    but.bind('<Return>', lambda event, x=button, i=varRow-1, j=varColumn: select(x, i, j))
    buttonL[varRow-1].append(but)
    but.grid(row=varRow, column=varColumn)

  

    varColumn += 1
    if varColumn > 10:
        varColumn = 0
        varRow += 1
        buttonL.append([])
#b1 = tk.Button(root, text="CopytoClipboard", command=use_clipboard)
#b1.grid(row=10, column=1)
b2 = tk.Button(frm, text="change fontsize", command=chg_font)
b2.grid(row=11, column=0)
tk.Label(frm, text="Highlight text in text box area with mouse").grid(row=12, column=0)
tk.Label(frm, text="and hit ctrl + c to copy then miouse click destination area").grid(row=13, column=0)
tk.Label(frm, text="ex: notepad then ctrl + v").grid(row=14, column=0)
root.bind('<Left>', leftKey)
root.bind('<Right>', rightKey)
root.bind('<Up>', upKey)
root.bind('<Down>', downKey)

root.mainloop()






