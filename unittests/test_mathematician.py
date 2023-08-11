import unittest
from mathematician import Mathematician

class TestMathematician(unittest.TestCase):

    def test_square_nums(self):
        result = Mathematician.square_nums([1, 2, 6, 8])
        self.assertEqual(result, [1, 4, 36, 64])

    def test_remove_positives(self):
        result = Mathematician.remove_positives([5, -1, 0, 3, -7]) # ноль вважається додатним числом
        self.assertEqual(result,[-1, -7 ])

    def test_filter_leaps(self):
        result = Mathematician.filter_leaps([2020,1700,2021,2024])
        self.assertEqual(result, [2020,2024])


if __name__ == '__main__':
    unittest.main()