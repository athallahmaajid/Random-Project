import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
from tkinter import messagebox
from ttkthemes import ThemedTk
saved = ''
class App(ThemedTk):
    def __init__(self, *kwargs):
        super().__init__(*kwargs)
        self['theme'] = 'clam'
        self.geometry('750x500')
        
#-------Menu Area-------------------------------------------------------------------------------------------------
        self.menu = tk.Menu(self)
        self.file_menu = tk.Menu(self.menu, tearoff=0)
#-------Command Area----------------------------------------------------------------------------------------------
        self.file_menu.add_command(label='New File', accelerator='Ctrl+N', command=self.new_file)
        self.file_menu.add_command(label='Open', accelerator='Ctrl+O', command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Save', accelerator='Ctrl+S', command=self.save_file)
        self.file_menu.add_command(label='Save as', accelerator='Ctrl+Shift+S', command=self.saveas_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit', accelerator='Ctrl+Q', command=self.exit)
        self.filename = ''
        self.title('Untitled - Text Editor')
        self.menu.add_cascade(label='File', menu=self.file_menu)
        self.config(menu=self.menu)
#-------Bind Area-------------------------------------------------------------------------------------------------
        self.bind('<Control-o>', self.open_file)
        self.bind('<Control-s>', self.save_file)
        self.bind('<Control-Shift-S>', self.saveas_file)
        self.bind('<Control-q>', self.exit)
#-------Text Area-------------------------------------------------------------------------------------------------
        self.text_area = tk.Text(self, tabs=4)
        self.scroll_bar = ttk.Scrollbar(self, orient='vertical', command=self.text_area.yview)
#-------Control Area----------------------------------------------------------------------------------------------
        self.text_area.pack(side='left', fill='both', expand=True)
        self.scroll_bar.pack(side='right', fill='y')
#---Function Area-------------------------------------------------------------------------------------------------
    def new_file(self, *args):
        self.text_area.delete('1.0', 'end')
        self.title('Untitled - Text Editor')
        self.filename = ''

    def open_file(self, *args):
        self.filename = filedialog.askopenfilename(title='Open File', filetypes=(('All File', '*.*'),
                                                                            ('Python File', '*.py'),
                                                                            ('HTML File', '*.html'),
                                                                            ('CSS File', '*.css'),
                                                                            ('Javascript File', '*.js')))
        
        print(self.filename)
        if self.filename in (tuple(), ''):
            pass
        else:
            self.text_area.delete('1.0', 'end')
            opened_file = open(self.filename, 'r')
            stuff = opened_file.read()
            self.text_area.insert('1.0', stuff)
            opened_file.close()
            self.title(f'{self.filename} - Text Editor')
    def save_file(self, *args):
        if self.filename in (tuple(), ''):
            self.saveas_file()
        else:
            saved_file = open(f'{self.filename}', 'w')
            saved_file.write(self.text_area.get('1.0', 'end'))
            saved_file.close()
            self.title(f'{self.filename} - Text Editor')

    def saveas_file(self, *args):
        self.filename = filedialog.asksaveasfilename(title='Save File', filetypes=(('All File', '*.*'),
                                                                                    ('Python File', '*.py'),                                                                                ('HTML File', '*.html'),
                                                                                    ('CSS File', '*.css'),
                                                                                    ('Javascript File', '*.js')))
        if self.filename in (tuple(), ''):
            pass
        else:
            savedas_file = open(self.filename, 'w')
            savedas_file.write(self.text_area.get('1.0', 'end'))
            savedas_file.close()
            self.title(f'{self.filename} - Text Editor')
    def exit(self, *args):
        if saved == self.text_area.get('1.0', 'end'):
            self.destroy()
        else:
            confirm = messagebox.askyesnocancel(title='Quit', message='You haven\'t saved your projects, Do you want to save it?',
                                                default=messagebox.YES, parent=self)
            if confirm:
                self.save_file()
                self.destroy()
            elif confirm is None:
                return None
            else:
                self.destroy()
#------------------------------------------------------App End----------------------------------------------------

master = App()
master.mainloop()
