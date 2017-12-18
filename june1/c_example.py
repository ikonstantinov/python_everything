import ctypes

hello = ctypes.CDLL('../hello.so')
hello.hello()
print(dir(hello))
print(hello.add(2, 3))

hello.add.argtypes = (ctypes.c_int, ctypes.c_int)
hello.add.restype = ctypes.c_int

print(hello.add(11, 4))