from unittest import TestCase
from sort.mergesort import mergesort


class TestCaseMergeSort(TestCase):

    def test_case_base(self):
        self.assertEqual([], mergesort([]))
        self.assertEqual([1], mergesort([1]))

    def test_case_1(self):
        self.assertEqual([1, 2], mergesort([1, 2]))
        self.assertEqual([1, 2], mergesort([2, 1]))