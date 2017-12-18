def a():
    print('a')

def b():
    print('b')

def c():
    print('c')



class Notifier:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        self.observers.append(observer)

    def unregister(self, observer):
        self.observers.remove(observer)

    def __call__(self, f):
        def _(*args, **kwargs):
            res = f(*args, **kwargs)
            for observer in self.observers:
                observer()
            return res

        return _

notifier = Notifier()

@notifier
def f():
    return 42

print(f())
notifier.register(a)
notifier.register(c)
print(f())
notifier.unregister(a)
notifier.register(b)
print(f())