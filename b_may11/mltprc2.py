"""smth like pipe / queue"""

import multiprocessing
import time

a = 0


def f():
    global a
    for a in range(1000):
        a += 1
    q.put(a)

q = multiprocessing.Queue()

ps = []
for i in range(20):
    p = multiprocessing.Process(target=f)
    p.start()


for i in range(1):
    a += q.get()

print('A: ', a)
