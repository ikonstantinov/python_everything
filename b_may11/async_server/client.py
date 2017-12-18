import socket, time

s = socket.socket()
s.connect(('localhost', 5000))
while True:

    s.sendall(b'Hello')
    data = s.recv(1024)
    print('Data:', data)
    time.sleep(2)

