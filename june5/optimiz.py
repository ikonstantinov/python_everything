l = []

'slow version'
def f():
    for i in range(100):
        l.append(i)

'fast version'
def z():
    p = l.append
    for i in range(1000):
        p(i)



'another example'

e = list(range(10000))
'need to make dict'
d = dict.fromkeys(e)
'we can check if element exists in list'
print(d[11])
print(1 in d)