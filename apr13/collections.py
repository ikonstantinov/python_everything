import collections as collect


class MyList(collect.UserList):
    def sum(self):
        s = 0
        for i in self.data:
            s += i
        return s

l = MyList([1, 2, 4])
print(l)

print(l.sum())