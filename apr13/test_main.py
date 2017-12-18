import unittest
import unittest.mock

from apr13 import main

'''
pytest
unittest
CI tool - continuous integration
buildbot.net
'''


class TestMain(unittest.TestCase):
    def setUp(self):
        self.m = main.Maxer([1, 2, 3])
        print('Set Up')

    @unittest.mock.patch('apr13.main.f')
    def testMax1(self, a):
        a.side_effect = [0]
        self.assertEqual(self.m.max(), 3, 'max({})'.format(self.m.data))


    def testMax2(self):
        self.m.append(5)
        self.assertEqual(self.m.max(), 5)

    def tearDown(self):
        print('TearDown')