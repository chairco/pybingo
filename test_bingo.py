# -*- coding: utf-8 -*-
import unittest

try:
    from . import bingo
except Exception as e:
    import bingo


class TestBingo(unittest.TestCase):

    def log(self, msg):
        objid = hex(id(self))
        print("<{}>: {} -- {}".format(objid, msg, self._testMethodName))

    def setUp(self):
        self.data = [10, 5, 24, 6, 18, 11, 3, 13, 7, 15, 12,
                      2, 16, 23, 21, 14, 20, 19, 17, 0, 9, 4, 22, 8, 1]  # user's bingo
        self.num = [19, 23, 9, 7, 6, 10, 14, 8, 15, 2, 20, 18,  # answer's bingo
               13, 4, 17, 21, 12, 0, 22, 1, 3, 11, 5, 16, 24]

    def tearDown(self):
        self.log('tearDownnvoked.')

    def test_column(self):
        for i in range(0, len(self.num)):
            self.data[self.data.index(self.num[i])] = True
            if i == 12:
                assert bingo.check_column(self.data) == 0
            if i == 14:
                assert bingo.check_column(self.data) == 1
            if i == 21:
                assert bingo.check_column(self.data) == 2
            if i == 22:
                assert bingo.check_column(self.data) == 3

    def test_row(self):
        for i in range(0, len(self.num)):
            self.data[self.data.index(self.num[i])] = True
            if i == 12:
                assert bingo.check_column(self.data) == 0
            if i == 16:
                assert bingo.check_column(self.data) == 1
            if i == 21:
                assert bingo.check_column(self.data) == 2
            if i == 23:
                assert bingo.check_column(self.data) == 3

    def test_bingo_search(self):
        assert bingo.bingo_search(num=self.num, data=self.data) == 22


if __name__ == '__main__':
    unittest.main()
