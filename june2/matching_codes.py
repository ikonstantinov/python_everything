import timeit


def f():
    return 42

# print(timeit.timeit('__main__.f()', number=1, setup='import __main__'))


print('Map vs List compr')
print(timeit.timeit('map(lambda x: x*2, range(100))', number=100, setup='import __main__'))


print(timeit.timeit('[2*x for x in range(100)]', number=100, setup='import __main__'))
