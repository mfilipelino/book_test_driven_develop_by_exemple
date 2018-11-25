from unittest import TestCase
from maths.log2 import log2


class TestCaseLog2(TestCase):

    def test_case_base(self):
        self.assertEqual(log2(1), 0)
        self.assertEqual(log2(2), 1)

    def test_case_1(self):
        self.assertEqual(log2(4), 2)
        self.assertEqual(log2(8), 3)

    def test_case_2(self):
        self.assertEqual(log2(12), 4)
