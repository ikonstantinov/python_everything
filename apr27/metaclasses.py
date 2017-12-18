"""metaclasses"""
# как создать класс еще

A = type('A', (object, ), {'q': 1})

print(A)


class Meta(type):
    def __new__(cls, name, parents, props):
        new_props = {}
        for name, value in props.items():
            if not name.startswith('unused_'):
                new_props[name] = value
        return super().__new__(cls, name, parents, new_props)


class A(metaclass=Meta):
    a = 1
    unused_a = 2



print(dir(A))
print(A.__call__())