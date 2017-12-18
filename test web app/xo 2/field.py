class GameField:

    def __init__(self):
        self._field = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]

    def __repr__(self):
        return (5*"-" + '\n').join(['|'.join([cell for cell in row]) + '\n'
                           for row in self._field])

    def set_sign(self, x, y, sign):
        self._field[x][y] = sign

    def check_rows(self, field):
        for row in field:
            if row == ['X', 'X', 'X'] or row == ['0', '0', '0']:
                return True
        return False

    def game_over(self):
        return self.check_rows(self._field) or \
               self.check_rows([list(row) for row in zip(*self._field)])


def a():
    return 5


def add(x):
    return a() + x