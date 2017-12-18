class A:
    def f(self):
        print('A')


class C:
    def f(self):
        print('C')


class B(A, C):
    pass

a = B()
a.f()

print(B.__base__)

'''-------------------------'''


class Shape:
    def __init__(self, x, y):
        self.x, self.y = x, y


class Circle(Shape):
    def __init__(self, x, y,r):
        super().__init__(x, y)
        self.r = r

c = Circle(1, 2, 3)
print(vars(c))
print(repr(c))

Circle.__repr__ = lambda self: 'Circle({}, {}, {})'.format(self.x, self.y, self.r)
print(c)

#Circle.__str__ = lambda self: 'Circle: x={}, y={}, r={}'.format(self.x, self.y, self.r)
#c
print(c)

""" class Mixin, которые можно подменшивать к другим классам и которые содержат минимум функционала """


class ReprMixin:
    def __repr__(self):
        return '{} ({})'.format(
            self.__class__.__name__,
            ', Value '.join(['{} = {}'.format(name, value) for name, value in self.__dict__.items()]))


class Cube(ReprMixin):
    def __init__(self, a, b):
        self.a, self.b = a, b

a = Cube(100, 200)
print(a)


class CircleWithRepr(ReprMixin, Circle):
    pass

print('------------------')
ff = CircleWithRepr(1, 2, 3)
print(ff)
print(CircleWithRepr.__mro__)


"""
для множественного наследования - методолигия MRO
алгоритм С3
"""