"""
первы вид программы - приводим эту программу к сетевому виду
while 1:
    op = input('Operation? ')
    if op.lower() == 'q':
        break
    op1 = float(input('Operand1 '))
    op2 = float(input('Operand2 '))

    if op == '+':
        print(op1 + op2)
    elif op == '-':
        print(op1 - op2)
    else:
        print('Invalid operation')

"""
'''utility - Telnet, service - SSH'''

import socket


class NetworkView:
    def __init__(self):
        s = socket.socket()
        s.bind(('localhost', 5001))
        s.listen(5)
        self.c, a = s.accept()
        print('Connecnted: ', a)
        s.close()

    def input(self, msg):
        self.print(msg)
        res = self.c.recv(1024).decode('utf-8')[:-2]
        print(repr(res))
        return res

    def print(self, msg):
        self.c.sendall(str(msg).encode('UTF-8'))


class ConsoleView:

    def input(self, msg):
        return input(msg)

    def print(self, msg):
        print(msg)

# view = ConsoleView()
view = NetworkView()

while 1:
    op = view.input('\nOperation? ')
    if op.lower() == 'q':
        break
    op1 = float(view.input('Operand1 '))
    op2 = float(view.input('Operand2 '))

    if op == '+':
        view.print(op1 + op2)
    elif op == '-':
        view.print(op1 - op2)
    else:
        view.print('Invalid operation')