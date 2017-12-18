import weakref # слабая ссылка, которая не изменяет счетчик ссылок
import sys


class A:
    pass


a = A()
print(sys.getrefcount(a))

#weak reference
b = weakref.ref(a)
print(sys.getrefcount(a))
print(b())
