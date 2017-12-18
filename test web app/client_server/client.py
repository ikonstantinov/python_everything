import socket
import time
import threading

def client(i):
    s = socket.socket()
    s.connect(("localhost", 8000))
    print "Connected"
    try:
        while True:
            s.sendall("Hello: " + str(i))
            data = s.recv(1024)
            print data
            time.sleep(1)
    finally:
        s.close()

client(1)
#for i in range(20): 
#    t = threading.Thread(target=client, args=(i,))
#    t.start()
