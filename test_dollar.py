from unittest import TestCase
from dollar import Dollar


class TestDollar(TestCase):

    def test_multiplication(self):
        dollar_5 = Dollar(5)
        dollar_10 = dollar_5.times(2)
        self.assertEqual(10, dollar_10.amount)
        dollar_15 = dollar_5.times(3)
        self.assertEqual(15, dollar_15.amount)

    def test_equality(self):
        d1 = Dollar(5)
        d2 = Dollar(5)
        self.assertEqual(d1, d2)
