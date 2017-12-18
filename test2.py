import functools, operator


def odd(x):
    return x % 2

#print(list(filter(odd, [1, 2, 3, 4])))
#print(functools.reduce(odd, [1, 2, 3, 4]))

#print([(x,y) for x in [1, 2, 3] for y in [4,5,6]])

#print(list(map(lambda x: 2 * x, range(10))))

# carring

double = functools.partial(operator.mul, 2)
#print(double(3))

# composition
def comp(f, g):
    return lambda x: f(g(x))

#print(odd(3))

even = comp(odd, functools.partial(operator.add, 1))

#print(even(3))


l = [(2,1), (3,2), (1,4), (4,6), (7,2)]
l.sort()
print(l)
l.sort(key=lambda x: x[1])
print(l)

l.sort(key=operator.itemgetter(1))
print(l)

a = [1, 'asv', 3.4, 2,3, 'aer', 4.5]
a.sort(key=str)
print(a)

#zamikanie / closing


def f (a):
    def g(x):
        return a * x
    return g
double = f(2)
triple = f(3)
print(double(5))
print(triple(3))

#functools.wraps()


def r(a):
    def g(x):
        return a * x
    def set_a(x):
        nonlocal a
        a = x
    g.set_a = set_a
    return g

double = r(2)
print("11111111")
print(double(3))
print("separator")

l = []

for i in range(10):
    def f(x, a=i):
        return a*x
    l.append(f)

print(l[0](1))
print(l[1](2))