@profile
def f():
    l = [0] * 10000000
    l1 = [1] * 500000
    del l
    del l1

print(f())

'python -m memory_profiler june5/profiling_test.py'