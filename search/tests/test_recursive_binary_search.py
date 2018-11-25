from unittest import TestCase
from search.recursive_binary_search import recursive_binary_search


class TestCaseRecursiveBinarySearch(TestCase):

    def test_case_base(self):
        self.assertEqual(None, recursive_binary_search([], 1))

    def test_case_len_1(self):
        self.assertEqual(0, recursive_binary_search([1], 1))
        self.assertEqual(None, recursive_binary_search([2], 1))

    def test_case_len_2(self):
        self.assertEqual(None, recursive_binary_search([1, 2], 3))
        self.assertEqual(0, recursive_binary_search([1, 2], 1))
        self.assertEqual(1, recursive_binary_search([1, 2], 2))

    def test_case_len_3(self):
        self.assertEqual(None, recursive_binary_search([1, 2, 3], 4))
        self.assertEqual(None, recursive_binary_search([1, 2, 3], 0))
        self.assertEqual(0, recursive_binary_search([1, 2, 3], 1))
        self.assertEqual(1, recursive_binary_search([1, 2, 3], 2))
        self.assertEqual(2, recursive_binary_search([1, 2, 3], 3))
