from Tkinter import *
import tkMessageBox

root = Tk()

root.geometry('300x200')

def add(x, y):
    return x + y

def hello():
    try:
        nx = float(x.get())
        ny = float(y.get())
    except ValueError:
        tkMessageBox.showerror("Error", "Invalid x or y")
        return
    res = add(nx, ny)
    r.config(text=str(res))

x = Entry()
x.grid(row=0, column=0)
y = Entry()
y.grid(row=1, column=0)
b = Button(text="Ok", command=hello)
b.place(relx=0, rely=0.3)
r = Label(text='')
r.grid(row=0, column=1)
root.mainloop()


