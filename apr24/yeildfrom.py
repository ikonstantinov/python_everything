import collections

s = 'aa bb cc aa bb aa'


def coroutine(f):
    def wrapper(*n):
        gen = f(*n)
        next(gen)
        return gen
    return wrapper

w = collections.defaultdict(int)


@coroutine
def word_counter():
    yield

    while True:
        word = yield from word_getter()
        if not word:
            return
        w[word] += 1


@coroutine
def word_getter():
    yield
    w = ''
    while True:
        try:
            s = yield
        except GeneratorExit:
            return ''
        if s == ' ':
            return w
        w += s

wc = word_counter()
next(wc)
for c in s:
    wc.send(c)

wc.close()
print(w)
# def word_gen():
#     word = ''
#     for c in s:
#         if c == ' ':
#             yield word
#         word += c
#
