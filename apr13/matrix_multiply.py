import numbers


class Number:
    def __init__(self, n):
        self._n = n

    def __repr__(self):
        return "Number ({})".format(self._n)

    def __add__(self, other):
        if isinstance(other, (numbers.Number)):
            return  Number(self._n + other)
        return Number(self._n + other._n)

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        return self.__add__(other)


aa = Number(5)
print(aa)
bb = Number(12)
print(aa + bb)
print(Number(1) + Number(98))
print(Number(1) + 9)
print(12 + Number(33))
aa += 100
