from unittest import TestCase
from sort.insertion import insertion_sort


class TestInsertionSort(TestCase):

    def test_list_empty(self):
        self.assertEqual(insertion_sort([]), [])

    def test_list_one_item(self):
        self.assertEqual(insertion_sort([1]), [1])
        self.assertEqual(insertion_sort(['a']), ['a'])

    def test_list_two_items(self):
        self.assertEqual(insertion_sort([1, 2]), [1, 2])
        self.assertEqual(insertion_sort([2, 1]), [1, 2])

    def test_list_multi_items(self):
        self.assertEqual(insertion_sort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(insertion_sort([1, 3, 2]), [1, 2, 3])
        self.assertEqual(insertion_sort([3, 2, 1]), [1, 2, 3])

    def test_list_multi_items(self):
        self.assertEqual(insertion_sort([5, 3, 1, 2, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(insertion_sort(['e', 'c', 'a', 'b', 'd']), list('abcde'))