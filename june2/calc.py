import tkinter as tk
from tkinter import messagebox


def calculate():
    try:
        resv.set(xv.get() + yv.get())
    except tk.TclError:
        messagebox.showerror('Errrr', 'Ypure asas')

root = tk.Tk()
root.geometry('250x250')


xv = tk.IntVar()
yv = tk.IntVar()
resv = tk.IntVar()

l1 = tk.Label(root, text='X: ')
l1.grid(row=0, column=0)
x = tk.Entry(root, textvariable=xv)
x.grid(column=1, row=0)

l2 = tk.Label(root, text='Y: ')
l2.grid(row=1, column=0)
y = tk.Entry(root, textvariable=yv)
y.grid(column=1, row=1)

b = tk.Button(root, text='Calculate', command=calculate)
b.grid(row=2, column=1)

res = tk.Label(root, text='Result', textvariable=resv)
res.grid(row=2, column=0)

root.mainloop()