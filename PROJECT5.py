#This is a simple calculator using python---

import tkinter as tk
from tkinter import messagebox

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Error")
            messagebox.showerror("Error", "Invalid Operation")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen.get() + text)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold")
screen.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', '',
    '1', '2', '3', '-', '',
    '0', '.', '=', '+', ''
]

row_val = 0
col_val = 0

for button in buttons:
    if button != '':
        btn = tk.Button(button_frame, text=button, font="lucida 15 bold", width=5, height=2)
        btn.grid(row=row_val, column=col_val, padx=5, pady=5)
        btn.bind("<Button-1>", click)
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

root.mainloop()                                                                                                                                                                                                          