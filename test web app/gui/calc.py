from Tkinter import *

root = Tk()

def get_func(i):
    def handler():
        t.set(t.get() + str(i))
    return handler

x = 0
def plus():
    global x
    x = int(t.get())
    t.set('')
    op = '+'
    
def eq():
    t.set(str(int(t.get()) + x))
    
t = StringVar()
t.set('')
l = Label(textvariable=t)
l.grid(row=4, column=0, columnspan=3)

for i in range(10):
    b = Button(text=str(i), command=get_func(i))
    b.grid(row=i / 3, column=i % 3)
    
bp = Button(text="+", command=plus)
bp.grid(row=3, column=1)
br = Button(text="=", command=eq)
br.grid(row=3, column=2)

root.mainloop()
