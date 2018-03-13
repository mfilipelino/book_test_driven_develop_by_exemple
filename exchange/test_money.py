from unittest import TestCase

from exchange.money import dollar, franc, Exchange, CHF, USD


class TestMoney(TestCase):
    def test_multiplication(self):
        self.assertEqual(dollar(5).times(2).amount, 10)
        self.assertEqual(15, dollar(5).times(3).amount)

    def test_equality(self):
        self.assertEqual(dollar(5), dollar(5))
        self.assertEqual(dollar(5).times(6), dollar(6).times(5))
        self.assertNotEqual(dollar(1), dollar(0))

    def test_currency(self):
        self.assertEqual(USD, dollar(1).currency)
        self.assertEqual(CHF, franc(1).currency)
        self.assertEqual(dollar(1).currency, dollar(2).currency)
        self.assertNotEqual(dollar(3).currency, franc(3).currency)

    def test_plus_money(self):
        self.assertEqual(dollar(1) + dollar(2), dollar(3))
        self.assertEqual(franc(2) + franc(2), franc(4))


class TestExchange(TestCase):

    def test_plus_money(self):

        Exchange.add_rate(USD, 2, CHF)
        self.assertEqual(Exchange.convert(franc(2), USD), dollar(1))
        self.assertEqual(Exchange.convert(dollar(2), CHF), franc(4))
        self.assertEqual(Exchange.convert(franc(2), USD) + dollar(2), dollar(3))

        Exchange.add_rate(USD, 3, CHF)
        self.assertEqual(Exchange.convert(franc(3), USD), dollar(1))

