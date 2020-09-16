import unittest

from src.compare import compare, compare2

class TestCompare(unittest.TestCase):

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))

    def test_compare_2_14_returns_2_is_less_than_14(self):
        self.assertEqual("2 is less than 14", compare2(2, 14))

    def test_compare_7_9_returns_7_is_less_than9(self):
        self.assertEqual("7 is less than 9", compare2(7, 9))

    def test_compare_10000_2_returns_10000_is_greater_than_2(self):
        self.assertEqual("10000 is greater than 2", compare(10000, 2))