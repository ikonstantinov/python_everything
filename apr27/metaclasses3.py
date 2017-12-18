"""metaclasses"""


class Meta(type):
    def __new__(cls, name, parents, props):
        new_cls =  super().__new__(cls, name, parents, props)
        if hasattr(cls, 'children'):
            cls.children[name] = new_cls
        else:
            cls.children = {}
        return new_cls


class A(metaclass=Meta):
    pass

class B(A):
    pass

class C(B):
    pass

print(A.children)



