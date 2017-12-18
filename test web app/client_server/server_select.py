import socket
import select

def handle(c):
    data = c.recv(1024)
    if not data:
        connections.remove(c)
        c.close()
        return
    print "Received: " + data
    c.sendall(data)
    

s = socket.socket()
s.bind(('localhost', 8000))
s.setblocking(0)
s.listen(5)
connections = [s]
print "Server starts..."
try:
    while True:
        sockets_read, _, _ = select.select(connections, [], [])
        for sock in sockets_read:
            if sock == s:
                c, a = s.accept()
                print "Connected: {}".format(a)
                connections.append(c)
            else:
                handle(sock)
finally:
    s.close()
