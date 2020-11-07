import tkinter as tk

root = tk.Tk()

def tekan_tombol(*args):
    rupiah = int(rupiah_input.get())
    hasil = rupiah / 15000
    dollar_output = tk.Label(text='dollar : ' + str(hasil))
    dollar_output.grid(row=4, column=0)

text_rupiah = tk.Label(root, text='RUPIAH')
rupiah_input = tk.Entry(root)
tombol = tk.Button(root, text='ENTER',
                   command=tekan_tombol)
text_rupiah.grid(row=0)
rupiah_input.grid(row=1)
rupiah_input.bind('<Return>', tekan_tombol)
tombol.grid(row=2)

root.mainloop()

















