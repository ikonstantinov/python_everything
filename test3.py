import functools


def a(f):
    def _(*args, **kwargs):
        print('It is a before')
        r = f(*args, **kwargs)
        print('It is a after')
        return r
    return _


def c(f):
    @functools.wraps(f)
    def _():
        print('It is c before')
        r = f()
        print('It is c after')
        return r
    return _


def d(f):
    @functools.wraps(f)
    def _():
        print('It is d before')
        r = f()
        print('It is d after')
        return r
    return _


rr = 0


@d
@c
@a
def b():
    global rr
    rr += 1
    print('It is b')

b()
print(rr)
b()
print(rr)