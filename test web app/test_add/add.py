import collections

def a():
    return 1

file_ = open('test.txt', 'rt')

class Adder:
    def __init__(self, x):
        self.x = x

    def add(self, y):
        return y + self.x + a()


def word_counter(filename='test.txt', open=open):
    with open(filename, 'rt') as f:
        words = f.read().split()
    c = collections.Counter(words)
    return c.most_common(1)


def word_counter1():
    words = file_.read().split()
    c = collections.Counter(words)
    return c.most_common(1)

if __name__ == '__main__':
    print(word_counter())
