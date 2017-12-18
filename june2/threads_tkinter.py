import tkinter as tk
import urllib.request
import threading

x = 0
is_interrupted = False
PB_LENGTH = 50
REQUESTS = 20
completed = 0

def run():
    b.config(text='Stop', command=stop)
    t = threading.Thread(target=get)
    t.start()


def stop():
    global is_interrupted
    is_interrupted = True


def get():
    global x, is_interrupted, completed
    print('x is ', x)
    for i in range(REQUESTS):
        if is_interrupted:
            break
        r = urllib.request.urlopen('http://itea.ua')
        r.read()
        completed = i
        x  = x + 1
    is_interrupted = False
    b.config(text='Run', command=run)


def pb_update():
    spaces = int((PB_LENGTH/REQUESTS) * completed)
    l.config(text=spaces*' ')
    l.after(1000, pb_update)

root = tk.Tk()
root.geometry('300x200')
b = tk.Button(root, text='Run', command=run)
b.pack()
l = tk.Label(root, text='', bg='red')
l.pack()
l.after(1000, pb_update)


root.mainloop()