import socket
import threading

def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            c.close()
            break    
        print "Received: " + data
        c.sendall(data)
    

s = socket.socket()
s.bind(('localhost', 8000))
s.listen(5)
print "Server starts..."
try:
    while True:
        c, a = s.accept()
        print "Connected: {}".format(a)
        t = threading.Thread(target=handle, args=(c,))
        t.start()
finally:
    s.close()
