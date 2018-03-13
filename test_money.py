from unittest import TestCase
from money import dollar, franc, MoneyTypeError, Bank


class TestMoney(TestCase):
    def test_multiplication(self):
        self.assertEqual(dollar(5).times(2).amount, 10)
        self.assertEqual(15, dollar(5).times(3).amount)

    def test_equality(self):
        self.assertEqual(dollar(5), dollar(5))
        self.assertEqual(dollar(5).times(6), dollar(6).times(5))
        self.assertNotEqual(dollar(1), dollar(0))

    def test_currency(self):
        self.assertEqual('USD', dollar(1).currency)
        self.assertEqual('CHF', franc(1).currency)
        self.assertEqual(dollar(1).currency, dollar(2).currency)
        self.assertNotEqual(dollar(3).currency, franc(3).currency)

    def test_plus_money(self):
        self.assertEqual(dollar(1) + dollar(2), dollar(3))
        self.assertEqual(dollar(2).plus(dollar(1)), dollar(3))
        self.assertEqual(franc(2).plus(franc(2)), franc(4))


class TestBank(TestCase):
    def test_plus_money(self):
        money = Bank.sum(dollar(3), dollar(4), currency='USD')
        self.assertEqual(money, dollar(7))
        self.assertEqual(money.currency, 'USD')

        money = Bank.sum(franc(3), franc(4), currency='CHF')
        self.assertEqual(money, franc(7))
        self.assertEqual(money.currency, 'CHF')

        money = Bank.sum(dollar(3), franc(4), currency='USD')
        self.assertEqual(money, dollar(5))
        self.assertEqual(money.currency, 'USD')
