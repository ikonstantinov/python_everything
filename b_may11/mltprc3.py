"""smth like pipe / queue"""

import multiprocessing
import time

a = multiprocessing.Value('i', 0)

def f():
    for i in range(100):
        a.value += 1

q = multiprocessing.Queue()
ps = []
for i in range(8):
    p = multiprocessing.Process(target=f)
    p.start()
    ps.append(p)


for p in ps:
    p.join()

print(a.value)
