import unittest
import unittest.mock
import add
import io


class TestAdder(unittest.TestCase):

    def setUp(self):
        self.a = add.Adder(5)

    @unittest.mock.patch('add.a')
    def test_add1(self, b):
        b.return_value = 0
        self.assertEqual(self.a.add(5), 10)
        self.a.x = 7
        self.assertEqual(self.a.add(5), 12)

    @unittest.mock.patch('add.a')
    def test_add2(self, b):
        b.return_value = 0
        self.assertEqual(self.a.add(7), 12)

    def test_words(self):
        s = io.StringIO('aaa bbb aaa bbb aaa ccc aaa')
        self.assertEqual(add.word_counter(s, open=lambda x, m: x)[0][0], 'aaa')

    def test_words1(self):
        m = unittest.mock.mock_open(read_data='aaa bbb aaa bbb aaa ccc aaa')
        with unittest.mock.patch('{}.open'.format(__name__), m, create=True):
            self.assertEqual(add.word_counter()[0][0], 'aaa')

    @unittest.mock.patch('add.file_')
    def test_words2(self, f):
        f.read.return_value = 'aaa bbb aaa bbb aaa ccc aaa'
        self.assertEqual(add.word_counter1()[0][0], 'aaa')

    def tearDown(self):
        print('tearDown')
