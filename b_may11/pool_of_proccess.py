import multiprocessing, time


def double(x):
    if x % 3:
        time.sleep(1)
    return 4 * x

p = multiprocessing.Pool(3)
print(p.map(double, range(10)))