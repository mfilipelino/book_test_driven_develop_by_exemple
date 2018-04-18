from unittest import TestCase

from urionlinejudge.notes_and_coins import (
    notes_and_coins,
    number_of_coins,
    remaining_value
)

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


class TestNotesAndCoins(TestCase):
    def test_number_of_coins(self):
        self.assertEqual(number_of_coins(100.00, 100.00), 1)
        self.assertEqual(number_of_coins(100.00, 90.00), 1)
        self.assertEqual(number_of_coins(100.00, 40.00), 2)
        self.assertEqual(number_of_coins(1.00, 0.50), 2)

    def test_remaining_value(self):
        self.assertEqual(remaining_value(100.00, 100.00), 0)
        self.assertEqual(remaining_value(100.00, 90.00), 10)
        self.assertEqual(remaining_value(1.00, 0.30), 0.10)

    def test_one(self):
        self.assertEqual(notes_and_coins(576.73), out_one)
