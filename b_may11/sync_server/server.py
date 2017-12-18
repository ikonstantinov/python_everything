import socket
import threading

"""
multiclients sycnronyze server - like Apache

"""

def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            c.close()
            break
        print('Data: ', data)
        c.sendall(data)


s = socket.socket()
s.bind(('localhost', 5000))
s.listen()
print('Waiting on client...')

while True:
    c, a = s.accept()
    # c - client socket, a - address
    print('Connected: ', a)
    t = threading.Thread(target=handle, args=(c, ))
    t.start()
