import tkinter as tk
import math
from tkinter import messagebox as mssg

master = tk.Tk()
master.title('Pythagoras Calc')
master.geometry('300x200')

variable = tk.StringVar(master)
variable.set('c')

option = tk.OptionMenu(master, variable, 'c', 'a', 'b')

def c(a, b, *args):
    try:
        int_a = int(a.get())
        int_b = int(b.get())
        res = tk.Label(master, text=f'Result : {math.sqrt(int_a**2+int_b**2)}')
        res.place(x=32, y=150)
    except ValueError:
        mssg.showerror('Error', 'Please Input Number')
        callback()
def a(c, b, *args):
    try:
        int_c = int(c.get())
        int_b = int(b.get())
        res = tk.Label(master, text=f'Result : {math.sqrt(int_c**2-int_b**2)}')
        res.place(x=80, y=150)
    except ValueError:
        mssg.showerror('Error', 'Please Input Number')
        callback()
def b(a, c, *args):
    try:
        int_a = int(a.get())
        int_c = int(c.get())
        res = tk.Label(master, text=f'Result : {math.sqrt(int_c**2-int_a**2)}')
        res.place(x=80, y=150)
    except ValueError:
        mssg.showerror('Error', 'Please Input Number')
        callback()

def callback(*args):
    list = master.place_slaves()
    for l in list:
        l.destroy()
    option = tk.OptionMenu(master, variable, 'c', 'a', 'b')
    option.place(x=20, y=80)
    if variable.get() == 'c':
        a_label = tk.Label(master, text='a', width=1)
        a_entry = tk.Entry(master)
        b_label = tk.Label(master, text='b', width=1)
        b_entry = tk.Entry(master)
        a_label.place(x=160, y=20)
        a_entry.place(x=83, y=40)
        b_label.place(x=160, y=65)
        b_entry.place(x=83, y=85)
        process_button = tk.Button(master, text='Process', command=lambda : c(a_entry, b_entry))
        process_button.place(x=125, y=110)
    elif variable.get() == 'a':
        c_label = tk.Label(master, text='c', width=1)
        c_entry = tk.Entry(master)
        b_label = tk.Label(master, text='b', width=1)
        b_entry = tk.Entry(master)
        c_label.place(x=160, y=20)
        c_entry.place(x=83, y=40)
        b_label.place(x=160, y=65)
        b_entry.place(x=83, y=85)
        process_button = tk.Button(master, text='Process', command=lambda : a(c_entry, b_entry))
        process_button.place(x=125, y=110)
    else:
        a_label = tk.Label(master, text='a', width=1)
        a_entry = tk.Entry(master)
        c_label = tk.Label(master, text='c', width=1)
        c_entry = tk.Entry(master)
        a_label.place(x=160, y=20)
        a_entry.place(x=83, y=40)
        c_label.place(x=160, y=65)
        c_entry.place(x=83, y=85)
        process_button = tk.Button(master, text='Process', command=lambda : b(a_entry, c_entry))
        process_button.place(x=125, y=110)

callback()
option.place(x=20, y=80)
variable.trace('w', callback)
master.mainloop()
