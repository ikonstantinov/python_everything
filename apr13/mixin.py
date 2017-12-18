class ReprMixin:
    def __repr__(self):
        return "{}({})".format(
            self.__class__.__name__,
            ','.join(["{}={}".format
                                   (name, value) for name, value in self.__dict__.items()]
                               )
                            )
class EqualMixin:
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__dict__ == other.__dict__

class Person(ReprMixin, EqualMixin):
    def __init__(self, name, age):
        self.name, self.age = name, age


p = Person('Bill', 231)
print(p)
z = Person('Bill', 231)
print(z)
print(p == z)
print(Person('Bill', 231) == Person('Bill', 231))
print('Lambda', '---'*10)
Person.__eq__ = lambda self, other: self.name == other.name
print(Person('Bill', 231) == Person('Bill', 222))
