class D:
    def __init__(self):
        print('D', self)
        super().__init__()

class A(D):
    def __init__(self):
        print('A', self)
        super().__init__()


class B:
    def __init__(self):
        print('B', self)
        super().__init__()


class C(A, B):
    def __init__(self):
        print('C', self)
        super().__init__()


C()
