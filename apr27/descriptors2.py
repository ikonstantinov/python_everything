"""decorators with property"""

class Line:
    def __init__(self):
        self._l = 0
    @property
    def l(self):
        return self._l / 9

    @l.setter
    def l(self, value):
        self._l = 9 * value


a = Line()
a.l = 1
print(a.l)
print(a._l)


class Box:
    def __init__(self, h, w, l):
        self._h, self._w, self._l = h, w, l
    @property
    def volume(self):
        return self._l * self._h * self._w

b = Box(1, 2, 4)
print(b.volume)
