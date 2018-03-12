from unittest import TestCase
from money import dollar, franc


class TestMoney(TestCase):
    def test_multiplication(self):
        dollar_five = dollar(5)
        self.assertEqual(dollar_five.times(2).amount, 10)
        dollar_c = dollar_five.times(3)
        self.assertEqual(15, dollar_c.amount)

    def test_equality(self):
        m1 = dollar(5)
        m2 = franc(5)
        m4 = dollar(5)
        m5 = franc(6)
        self.assertEqual(m1, m4)
        self.assertEqual(m2.times(6), m5.times(5))
        self.assertNotEqual(m2, m1)

    def test_currency(self):
        m1 = dollar(3)
        m2 = franc(4)
        self.assertEqual('USD', m1.currency)
        self.assertEqual('CHF', m2.currency)

    def test_plus_money(self):
        m1 = dollar(1)
        m2 = dollar(2)
        m3 = m1 + m2
        self.assertEqual(m3, dollar(3))
        self.assertEqual(m2.plus(dollar(1)), dollar(3))