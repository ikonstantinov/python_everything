class A: pass


class B(A): pass


class C(A): pass


class D(C): pass


class E(C): pass


class F(B, D): pass


class G(D, E): pass


class H(F, G): pass

print(H.__mro__)
print("-----------------")
print(H.__bases__)