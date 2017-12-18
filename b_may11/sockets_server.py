import socket
#echoserver
s = socket.socket()
s.bind(('localhost', 5000))
s.listen()
print('Waiting on client...')

c, a = s.accept()
# c - client socket, a - address

print('Connected: ', a)
print(c, c is s)
data = c.recv(1024)
print('Data: ', data)
c.sendall(data)
c.close()
s.close()