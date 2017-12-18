import multiprocessing
import time

a = 0


def f():
    global a
    for a in range(1000):
        a += 1
    print('A: ', a)

ps=[]
for i in range(2):
    p = multiprocessing.Process(target=f)
    p.start()
    ps.append(p)


for p in ps:
    p.join()

print('A: ', a)

"""
IPC (POSIX): 4 mechanism:
1. Pipe
2. Message Queue
3. Shared Memory
4. Socket
"""