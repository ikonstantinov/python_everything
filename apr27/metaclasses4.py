import abc


class A(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def f(self):
        pass

    @abc.abstractmethod
    def g(self):
        pass

    @abc.abstractmethod
    def h(self):
        pass


# a = A() - will be error because f is not implemented: TypeError


class B(A):
    def g(self):
        super().g()

    def f(self):
        super().f()

    def h(self):
        super().h()


b = B()