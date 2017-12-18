class A(object):
    def __init__(self):
        print "A"
        super(A, self).__init__()
        
    def f(self):
        super(A, self).f()

class B(object):
    def __init__(self):
        print "B"
        super(B, self).__init__()
        
    def f(self):
        #super(B, self).f()

class C(object):
    def __init__(self):
        print "C"
        super(C, self).__init__()

class D(A, B):
    def __init__(self):
        print "D"
        super(D, self).__init__()
        
    def f(self):
        super(D, self).f()

class E(D, C): 
    def __init__(self):
        print "E"
        super(E, self).__init__()
        
class H(A, C):
    def __init__(self):
        print "H"
        super(H, self).__init__()
    


