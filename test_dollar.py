from unittest import TestCase
from dollar import Dollar


class TestDollar(TestCase):

    def test_multiplication(self):
        dollar_five = Dollar(5)
        self.assertEqual(dollar_dive, Dollar(10))
        dollar_c = dollar_a.times(3)
        self.assertEqual(Dollar(15), dollar_c)

    def test_equality(self):
        d1 = Dollar(5)
        d2 = Dollar(5)
        d3 = Dollar(6)
        self.assertEqual(d1, d2)
        self.assertNotEqual(d1, d3)
