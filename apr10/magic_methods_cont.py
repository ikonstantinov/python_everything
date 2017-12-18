class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Person({}, {})'.format(self.name, self.age)

    #оператор сравнения равенства
    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        return hash(self.name)

    #set orderable
    def __lt__(self, other):
        return self.name < other.name

#p = Person('Bill', 32)
#p1 = Person('Bill', 32)

# see how eq works
#print(p == p1)
# see how NonImplemented works
# print(p == 1)

#l = [Person('Bob', 12), Person('Bill', 10),Person('John', 13)]
#print(l.index(Person('Bill', 10)))

#пример как нельзя использовать мьютабл элементы для ключей словаря
s = {Person('Bob', 12), Person('Bill', 10), Person('Kent', 121), Person('Bill', 23)}
#print(s)
p = Person('Bill', 21)
d = {p:1}
#print(d)
#print(d[p])
p.name = 'Mary'
#print(d)
#print(d[p])

l = [Person('Zob', 12), Person('Bill', 10), Person('John', 13)]
l.sort()
print(l)
print(l[0])