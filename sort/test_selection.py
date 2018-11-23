from unittest import TestCase
from sort.selection import selection


class TestSelection(TestCase):

    def test_base_case(self):
        self.assertEqual([], selection([]))
        self.assertEqual([1], selection([1]))
        self.assertEqual([2], selection([2]))

    def test_case_1(self):
        self.assertEqual([1, 2], selection([1, 2]))
        self.assertEqual([1, 2], selection([2, 1]))
        self.assertEqual([1, 3], selection([3, 1]))

    def test_case_2(self):
        self.assertEqual([1, 2, 3], selection([1, 2, 3]))
        self.assertEqual([1, 2, 3], selection([1, 3, 2]))
        self.assertEqual([1, 2, 3], selection([2, 3, 1]))
        self.assertEqual([1, 2, 3], selection([2, 1, 3]))
        self.assertEqual([1, 2, 3], selection([3, 1, 2]))
        self.assertEqual([1, 2, 3], selection([3, 2, 1]))

    def test_case_3(self):
        self.assertEqual(list(range(0, 10)), selection(list(range(9, -1, -1))))



