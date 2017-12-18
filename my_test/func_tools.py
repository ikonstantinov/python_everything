"""
list comprehensions
"""


def f():
    return [i for i in range(5) if i % 2]

#print(f())


import functools


def f2():
    return (
        functools.reduce(lambda x, y: x+y, range(3, 5), i)
        for i in range(7, 9) if i % 2 == 0)

ff = f2()
#print(ff.__next__())
#print(ff)


def z():
    return [functools.reduce(lambda x, y: x + y, range(7))]

#print(z())
#print(functools.reduce(lambda x, y: x + y, range(1,3)))


def f3():
    return (i for i in range(3))

v = f3()
#print(v.__next__())
#print(v.__next__())
#print(v.__next__())


def ite():
    v = (yield 2)
    print('Recieved ', v)


try:
    r = ite()
    print('Sent 1:', r.send(None))
    print('Sent 2: ', r.send(10))
    #print("Next 1: ", next(r))
    #print("Next 2: ", next(r))
    print('Sent 3: ', r.send(123))
    p#rint("Next 3: ", next(r))
    print('Sent 4: ', r.send(202))
    #print("Next 4: ", next(r))
except StopIteration:
    print("StopIteration")

