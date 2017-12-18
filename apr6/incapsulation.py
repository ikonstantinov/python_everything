class A:
    def __init__(self):
        self.x = 0
        self._x = 0
        self.__x = 0

a = A()
a.x
a._x
a._A__x


print("-----------------")

class B:
    def __init__(self):
        self.__x = 1

    def f(self):
        print(self.__x)


class C(B):
    def __init__(self):
        self.__x = 2
        super().__init__()

    def g(self):
        print(self.__x)


c = C()
c.f()
print(vars(c))
print("-----------------")


'''для static method we can use @staticmethod / @classMethod'''

class HH:
    def __init__(self):
        self.a = 1

    a = 2
    @staticmethod
    def g():
        print(HH.a)

    @classmethod
    def h(cls):
        print(cls.a)


ff = HH()
ff.g()
ff.h()
HH.g()
HH.h()


print("-----------------")
class Z:
    a = 1
    @classmethod
    def f(cls):
        print(cls.a)

    @staticmethod
    def g():
        print(Z.a)

class W(Z):
    a = 22

Z.f()
W.f()
Z.g()
W.g()