class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("Init")

    def __cmp__(self, other):
        print("Cmp")
        if self.a == other:
            return 'Equals'

    def __del__(self):
        print("del")

class Word(str):
    '''Класс для слов, определяющий сравнение по длине слов.'''

    def __new__(cls, word):
        # Мы должны использовать __new__, так как тип str неизменяемый
        # и мы должны инициализировать его раньше (при создании)
        if ' ' in word:
            print("Value contains spaces. Truncating to first space.")
            word = word[:word.index(' ')] # Теперь Word это все символы до первого пробела
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)
    def __eq__(self, other):
        return self in other

aa = Word('asd iund')
print(aa == 'asg')