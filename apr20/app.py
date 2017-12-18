class MyList:
    def __init__(self, l=[]):
        self._l = list(l)

    def __repr__(self):
        return repr(self._l)

    def add(self, a):
        self._l.append(a)

    def __len__(self):
        return len(self._l)

    def __bool__(self):
        return bool(self._l)

    def __contains__(self, item):
        return item in self._l

    def __setitem__(self, key, value):
        self._l[key] = value

    def __getitem__(self, item): #item == index
        # return self._l[item]
        #print(item)
        """"""
        if isinstance(item, int):
            return self._l[item]
        elif isinstance(item, tuple):
            return [self._l[i] for i in item]
        elif item == ...:
            return self._l.copy()
        else:
            raise IndexError

    """new style iterator"""




a = MyList([1, 2, 4])
l = [1, 2, 3]
l1 = MyList(l)
print(l1)

l[0]=12
print(l1)
l2 = MyList([22, 33, 44, 66, 77])

print(l2)
"""add"""
l2.add(3)
print(l2)
print(len(l2))

"""bool"""
l3 = MyList([])
print(bool(l3))
if l3:
    print("Not empty")

l3.add([1])
if l3:
    print("Not empty")

"""set item"""
l3[0] = 1

"""get item"""
#l3[1, 2, 3, 4, 5, 6]

#l3[2:3]

"""slice"""
s = slice(2, 5)
range(10)[s]
print(list(range(10)[s]))

"""ellipsis"""
print(...)
l4 = [...]
print(l4)
print('...' == ...)

"""get item is instance"""
l5 = MyList(range(10))
print(l5[3])
print(l5[1, 3, 5, 7])
print(l5[...])
for i in l5:
    pass
#    print(i)

"""iter"""
l6 = [1, 2, 3]
#print(dir(l6))
print(iter(l6))
i = iter(l6)
print(i.__next__())
print(next(i))
print(i)