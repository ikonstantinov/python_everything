import pickle


class A:
    def __init__(self, f):
        self.f = f
        self.a = 1

    def __getstate__(self):
        print('get state')
        d = self.__dict__.copy()
        del d['f']
        return d

    def __setstate__(self, state):
        print('set state')
        self.__dict__ = state
        self.f = lambda x: 2 * x


#a = A(lambda x: 2 * x)
#print(vars(a))
#s = pickle.dumps(a)
#print(s)
#b = pickle.loads(s)
#print(vars(b))
#we can't serialize and deserialize without setstate/getstate
#pickle.dumps(a)


"""magic method - call"""
class Multiplier:
    def __init__(self, n):
        self._n = n

    def __call__(self, x):
        print('Call')
        return self._n * x

double = Multiplier(2)
print(double(2))