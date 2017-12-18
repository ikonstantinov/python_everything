def f():
    for i in range(5):
        yield i

g = f()
#print(next(g))


def f2():
    fn = open('test.txt', 'rt')
    for line in fn:
        try:
            yield line
        except GeneratorExit:
            fn.close()
            break
            #we should always add break in this case

g2 = f2()
print(next(g2))

g2.throw(ValueError)
# как бросать exception в генератор