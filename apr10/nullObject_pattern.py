#obj = NullObject


class NullObject:
    def __getattr__(self, name):
        return object()


a = NullObject()
print(a)
print(a.x)