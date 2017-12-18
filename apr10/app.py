"""
magic methods
"""

#print(dir(object))

"""
class A:
    def __setattr__(self, key, value):
        print('Setattr:', key, '=', value)
        super().__setattr__(key, value)

a = A()
a.x = 2
print(a.x)

"""

class A:
    def __init__(self):
        self.x = 1

    """
    def __setattr__(self, key, value):
        if key == 'x' and hasattr(self, key):
            raise AttributeError('x is read-only')
        super().__setattr__(key, value)

    def __delattr__(self, key):
        if key == 'x':
            raise AttributeError('x cannot be deleted')
        super().__delattr__(key)
        """

    def __getattr__(self, key):
        print('Get attr ', key)
        return 42


    def __getattribute__(self, key):
        print('Get attribute ', key)
        return super().__getattribute__(key)


a = A()
print(a.x)
a.y
#a.x = 3
#print(a.__dict__)
#delattr(a, 'x')