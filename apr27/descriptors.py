"""descriptor - это класс, который реализует методы set / get"""

class Length:
    """
    instance - obj
    owner - objtype
        
    """
    def __set__(self, instance, value):
        instance._l = value * 10

    def __get__(self, instance, owner):
        return instance._l / 10


class Line:
    l = Length()
    def __init__(self):
        self._l = 0

a = Line()
a.l = 10
#print(a.l)
#print(a._l)

'''class with only get'''
class Volume:
    def __get__(self, instance, owner):
        return instance._l * instance._w * instance._h

class Box:
    volume = Volume()
    def __init__(self, h, w, l):
        self._h, self._w, self._l = h, w, l



b = Box(10, 20, 30)
print(b.volume)


"""
import collections

d1 = {'a':1, 'b':2, 'c': 3}
d2 = {'c':18, 'a':2, 'b': 3}
d3 = {'x':11, 'b':22, 'c': 10}

d = collections.ChainMap(d1, d2, d3)
print(d['b'])
print(d['x'])
"""