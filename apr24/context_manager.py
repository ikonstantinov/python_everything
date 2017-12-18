#socket, mutex


class A:
    def __init__(self):
        self.a = 1

    def __enter__(self):
        print('Enter')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exit')

with A() as f:
    print('AAA')