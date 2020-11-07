from tkinter import *
import tkinter.messagebox
master = Tk()
master.title('Basic Calculator')
large_font = ('Verdana', 10)
isi_input = StringVar()

input_place = Entry(master, textvariable=isi_input, borderwidth=5, width=50, font=large_font)
input_place.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
input_place.focus()
def button_add(number):
    input_place.insert(len(input_place.get()), number)
def clear():
    input_place.delete(0, END)
def equal(event=None):
    try:
        global isi_input
        total = str(eval(input_place.get()))
        isi_input.set(total)
    except:
        tkinter.messagebox.showinfo('error', 'angka perhitungan anda mungkin salah')
def undo():
    global angka_sebelumnya
    angka_sebelumnya = ''
    input_place.delete(len(input_place.get())-1)
    angka_sebelumnya = str(input_place.get())
input_place.bind('<Return>', equal)
button_undo = Button(master, text='<', padx=45, fg='black', relief='flat', pady=10, command=undo)
button_clear = Button(master, text='clear', padx=45, fg='black', relief='flat', pady=10, width=1, command=clear)
button_clear.grid(row=0, column=4)
button_undo.grid(row=0, column=3)

button_7 = Button(master, text='7', padx=60, fg='black', relief='flat', pady=20, command=lambda:button_add(7))
button_8 = Button(master, text='8', padx=60, fg='black', relief='flat', pady=20, command=lambda:button_add(8))
button_9 = Button(master, text='9', padx=60, fg='black', relief='flat', pady=20, command=lambda:button_add(9))
button_parenthesis_1 = Button(master, text='(', padx=45, fg='black', relief='flat', pady=20, command=lambda:button_add('('))
button_parenthesis_2 = Button(master, text=')', padx=45, fg='black', relief='flat', pady=20, command=lambda:button_add(')'))

button_4 = Button(master, text='4', padx=60, fg='black', relief='flat', pady=20, command=lambda:button_add(4))
button_5 = Button(master, text='5', padx=60, fg='black', relief='flat', pady=20, command=lambda:button_add(5))
button_6 = Button(master, text='6', padx=60, fg='black', relief='flat', pady=20, command=lambda:button_add(6))
button_X = Button(master, text='x', padx=45, fg='black', relief='flat', pady=20, width=1, command=lambda:button_add('*'))
button_divide = Button(master, text='/', padx=45, fg='black', relief='flat', pady=20, command=lambda:button_add('/'))

button_1 = Button(master, text='1', padx=60, fg='black', relief='flat', pady=20, command=lambda:button_add(1))
button_2 = Button(master, text='2', padx=60, fg='black', relief='flat', pady=20, command=lambda:button_add(2))
button_3 = Button(master, text='3', padx=60, fg='black', relief='flat', pady=20, command=lambda:button_add(3))
button_addition = Button(master, text='+', padx=45, fg='black', relief='flat', width=0, pady=20, command=lambda:button_add('+'))
button_substract = Button(master, text='-', padx=45, fg='black', relief='flat', pady=20, command=lambda:button_add('-'))

button_0 = Button(master, text='0', padx=60, fg='black', relief='flat', pady=20, command=lambda:button_add(0))
button_coma = Button(master, text=',', padx=62, fg='black', relief='flat', pady=20, command=lambda:button_add('.'))
button_power = Button(master, text='power', padx=44, fg='black', relief='flat', pady=20, command=lambda:button_add('**'))
button_equal = Button(master, text='=', padx=98, fg='black', relief='flat', pady=20, width=1, command=equal)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_addition.grid(row=3, column=3)
button_substract.grid(row=3, column=4)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_X.grid(row=2, column=3)
button_divide.grid(row=2, column=4)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_parenthesis_1.grid(row=1, column=3)
button_parenthesis_2.grid(row=1, column=4)

button_0.grid(row=4, column=0)
button_coma.grid(row=4, column=1)
button_power.grid(row=4, column=2)
button_equal.place(y=240, x=434)

master.mainloop()