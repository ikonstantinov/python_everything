import socket
import select

"""
multiclients ssycnronyze server - like Nginx

"""

def handle(c):
    data = c.recv(1024)
    if not data:
        connections.remove(c)
        c.close()
        return
    print('Data: ', data)
    c.sendall(data)


s = socket.socket()
s.bind(('localhost', 5000))
s.setblocking(False)
s.listen(5)
print('Waiting on client...')
connections = [s]

while True:
    r_s, _, _ = select.select(connections, [], [])
    for r in r_s:
        if r == s:
            c, a = s.accept()
            # c - client socket, a - address
            print('Connected: ', a)
            connections.append(c)
        else:
            handle(r)
