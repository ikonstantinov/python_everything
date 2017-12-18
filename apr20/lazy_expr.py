"""
ленивые вычисления
"""

def infinity_list():
    i = 0
    while True:
        yield i
        i += 1

g = infinity_list()
print(next(g))

for i in infinity_list():
    if i*i > 50:
        break
    else:
        print(i, i*i)


"""itertools examples"""
import itertools

d = itertools.takewhile(lambda x: x < 50, (x * x for x in itertools.count(0)))
print(list(d))



"""алгоритм сжатия: groupby -> itertools"""
l = [0] * 5 + [1] * 2 + [0] * 3 + [1] * 5
for i, j in itertools.groupby(l):
    print(i, len(list(j)))


"""решето Эратосфена, см в книге"""
def filter_multi(n, gen):
    for i in gen:
        if i % n:
            yield i

def get_prime():
    c = itertools.count(2)
    while 1:
        prime = next(c)
        c = filter_multi(prime, c)
        yield prime

c = list(itertools.islice(get_prime(), 0, 10))
print(c)