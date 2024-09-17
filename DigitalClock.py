# This is a simple python project Digital Clock--

from tkinter import Tk, Label
from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor='center')

time()
root.mainloop()