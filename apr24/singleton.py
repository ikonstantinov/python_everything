class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

aa = Singleton()
bb = Singleton()
print(aa == bb)


class A:
    db_conn = ...
