import functools
def get_area(x):
    return x*x


def scale(f):
    def wrapper(x):
        return f(x*10)
    return wrapper

get_area = scale(get_area)
print(get_area(1))

@scale
def get_area2(x):
    return x * x

print(get_area(1))
print(get_area2(1))
print(functools.wraps.__doc__)
