class A:
    pass

a = A()
a.__dict__['x'] = 1
print(vars(a)) # vars is used istead of a.__dict__

class A:
    def f(self):
        print(self)
        self.x = 1


class B:
    pass

a = A()
b = B()

A.f(b)

"""------------------"""

class C:
    def f(self):
        print('C')

class D:
    def f(self):
        print('D')

c = C()
c.f()
c.__class__ = D

c.f()

"""------------------"""
