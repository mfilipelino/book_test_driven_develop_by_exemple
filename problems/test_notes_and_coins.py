from unittest import TestCase

from problems.notes_and_coins import (
    change_coin,
    number_of_coins,
    remaining_value,
    change_coins,
    out_notas
)


class TestNotesAndCoins(TestCase):

    def test_precision_divise(self):
        self.assertEqual(3.0, round(0.0300000 // 0.0100000000, 2))

    def test_number_of_coins(self):
        self.assertEqual(number_of_coins(100.00, 100.00), 1)
        self.assertEqual(number_of_coins(100.00, 90.00), 1)
        self.assertEqual(number_of_coins(100.00, 40.00), 2)
        self.assertEqual(number_of_coins(1.00, 0.50), 2)

    def test_remaining_value(self):
        self.assertEqual(remaining_value(100.00, 100.00), 0)
        self.assertEqual(remaining_value(100.00, 90.00), 10)
        self.assertEqual(remaining_value(1.00, 0.30), 0.10)

    def test_change(self):
        self.assertEqual(change_coin(150, 100), (1, 50))
        self.assertEqual(change_coin(150, 50), (3, 0))
        self.assertEqual(change_coin(40, 50), (0, 40))
        self.assertEqual(change_coin(10, 10), (1, 0))

    def test_return_change_of_money(self):
        self.assertEqual(change_coins(money=110, coins=[100, 10]), [1, 1])
        self.assertEqual(change_coins(money=10, coins=[10, 1]), [1, 0])
        self.assertEqual(change_coins(money=17, coins=[10, 5, 1]), [1, 1, 2])
        result = change_coins(money=576.73, coins=[100, 50, 20, 10, 5, 2])
        self.assertEqual(result, [5, 1, 1, 0, 1, 0])

    def test_return_change_of_coins(self):
        self.assertEqual(change_coins(money=17, coins=[10, 5, 1]), [1, 1, 2])
        result = change_coins(money=1.73, coins=[1.0, 0.5, 0.25, 0.10, 0.05, 0.01])
        self.assertEqual(result, [1, 1, 0, 2, 0, 3])

    def test_out_notas(self):
        # prepare
        notas = """NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
"""
        # act
        result = change_coins(money=576.73, coins=[100, 50, 20, 10, 5, 2])

        # assert
        self.assertEqual(out_notas(result), notas)

    def test_one(self):
        # prepare
        out_one = """NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01
"""

        self.assertEqual(notes_and_coins(576.73), out_one)
