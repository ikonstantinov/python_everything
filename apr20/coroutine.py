"""coroutine, read async programming"""

def coroutine(f):
    gen = f()
    next(gen)
    return gen

#f is coroutine
@coroutine
def f():
    i = yield
    print("f_i = ", i)
    i = yield i + 1
    print("f_i = ", i)
    i = yield i + 1
    print("f_i = ", i)
    i = yield i + 1
    print("f_i = ", i)
    i = yield i + 1

def main():
    i = f.send(0)
    print("main_i", i)
    i = f.send(i + 1)
    print("main_i", i)
    i = f.send(i + 1)
    print("main_i", i)
    i = f.send(i + 1)
    print("main_i", i)


main()