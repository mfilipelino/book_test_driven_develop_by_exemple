from unittest import TestCase
from sort.bubble import bubble_sort


class TestCaseBubbleSort(TestCase):

    def test_case_base(self):
        self.assertEqual([], bubble_sort([]))
        self.assertEqual([1], bubble_sort([1]))
        self.assertEqual(['a'], bubble_sort(['a']))
        self.assertEqual([[]], bubble_sort([[]]))

    def test_case_1(self):
        self.assertEqual([1, 2], bubble_sort([1, 2]))
        self.assertEqual([1, 2], bubble_sort([2, 1]))
        self.assertEqual(['a', 'b'], bubble_sort(['a', 'b']))
        self.assertEqual(['a', 'b'], bubble_sort(['b', 'a']))

    def test_case_2(self):
        self.assertEqual([1, 2, 3], bubble_sort([1, 2, 3]))
        self.assertEqual([1, 2, 3], bubble_sort([1, 3, 2]))
        self.assertEqual([1, 2, 3], bubble_sort([2, 1, 3]))
        self.assertEqual([1, 2, 3], bubble_sort([2, 3, 1]))
        self.assertEqual([1, 2, 3], bubble_sort([3, 2, 1]))
        self.assertEqual([1, 2, 3], bubble_sort([3, 1, 2]))