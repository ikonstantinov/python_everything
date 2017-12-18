class Meta(type):
    """метод кол - меняет экземпляр класса"""
    def __call__(self, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        instance.a = 1
        return instance

class A(metaclass=Meta):
    pass

a = A()
print(a.a)
print(vars(a))

print('*'*35)


class Meta2(type):
    def __call__(*args, **kwargs):
        print('Call')
        return type.__call__(*args, **kwargs)

    def __new__(*args, **kwargs):
        print('New')
        return type.__new__(*args, **kwargs)

    def __init__(*args, **kwargs):
        print('Init')
        type.__init__(*args, **kwargs)


class B(Meta2):
    pass


b = B()
