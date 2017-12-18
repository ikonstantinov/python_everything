class AS:
    __slots__ = ('_a', '_b')
    def __init__(self):
        self._a = 1
        self._b = 90

a = AS()
#print(a.__dict__)
print([{i: getattr(a, i)} for i in a.__slots__])
print(a._a)
print(a._b)
for i in [i for i in a.__slots__]:
    print(i)