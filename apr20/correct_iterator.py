"""correct iterator
"""

"""incorrect iterator"""


class Mylist:
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

    def __getitem__(self, item):  # item == index
        # return self._l[item]
        # print(item)
        """"""
        if isinstance(item, int):
            return self._l[item]
        elif isinstance(item, tuple):
            return [self._l[i] for i in item]
        elif item == ...:
            return self._l.copy()
        else:
            raise IndexError

    def __iter__(self):
        #return MyListIterator(self._l)
        #or
        #return iter(self._l)
        #or
        for i in self._l:
            yield i



class MyListIterator:
    def __init__(self, l):
        self._l = l
        print('Iter')
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        print('Next')
        self._i += 1
        if self._i == len(self._l) + 1:
            raise StopIteration
        return self._l[self._i - 1]

l = Mylist([1, 2, 3])


# for i in l:
#     for j in l:
#         print(i, j)
#

def f():
    for i in range(5):
        yield i
        print("I'm here")
for i in f():
    print(i)


"""
для чего нужен yield

1. Iterators
2. Lazy calculations (ленивые вычисления)
3. Coroutine (сопрограммы)
"""