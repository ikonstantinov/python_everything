import unittest
import unittest.mock
import field


class TestField(unittest.TestCase):

    def setUp(self):
        self.g = field.GameField()

    def test_set(self):
        self.g.set_sign(0, 0, 'X')
        self.assertEqual(self.g._field[0][0], 'X')

    def test_check_row(self):
        self.g.set_sign(1, 0, 'X')
        self.g.set_sign(1, 1, 'X')
        self.g.set_sign(1, 2, 'X')
        self.assertTrue(self.g.game_over())

    def test_check_column(self):
        self.g.set_sign(0, 1, 'X')
        self.g.set_sign(1, 1, 'X')
        self.g.set_sign(2, 1, 'X')
        self.assertTrue(self.g.game_over())
        self.g.set_sign(0, 1, '0')
        self.g.set_sign(1, 1, 'X')
        self.g.set_sign(2, 1, 'X')
        self.assertFalse(self.g.game_over())

    @unittest.mock.patch("field.a")
    def test_a(self, b):
        b.side_effect = [2, 3, 4]
        self.assertEqual(field.add(2), 4)
        self.assertEqual(field.add(2), 5)
        self.assertEqual(field.add(2), 6)
