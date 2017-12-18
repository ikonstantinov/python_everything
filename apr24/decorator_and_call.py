class scale:
    def __init__(self, n):
        self._n = n

    def __call__(self, f):
        def wrapper(x):
            return f(x - self._n)
        return wrapper


@scale(5)
def get_area(x):
    return x * x

print(get_area(1))
#print(get_area(1))
