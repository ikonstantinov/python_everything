from Tkinter import *

root = Tk()

cx = cy = None

def show(e):
    l.config(text="{} {}".format(e.x, e.y))
    
    
def draw(e):
    global cx, cy
    if cx is None:
        cx = e.x
        cy = e.y
    c.create_line(cx, cy, e.x, e.y)
    cx, cy = e.x, e.y
    show(e)

def release(e):
    global cx, cy
    cx = cy = None

c1 = StringVar()
c1.set('0')
def timer():
    global c1
    c1.set(str(int(c1.get()) + 1))
    l1.after(1000, timer)

screen_width = int(0.5*root.winfo_screenwidth())
screen_height = int(0.5*root.winfo_screenheight())

root.geometry("{}x{}".format(screen_width, screen_height))

c = Canvas()
c.pack(fill=BOTH, expand=1)
l = Label(text="")
l.pack()
l1 = Label(text="0", textvariable=c1)
l1.pack()
l1.after(1000, timer)

c.bind('<Motion>', show)
c.bind('<B1-Motion>', draw)
c.bind('<ButtonRelease-1>', release)

root.mainloop()
