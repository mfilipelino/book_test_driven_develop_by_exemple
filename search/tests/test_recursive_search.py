from unittest import TestCase
from search.recursive_linear_search import recursive_linear_search


class TestCaseRecursiveLinearSearch(TestCase):

    def test_case_base(self):
        self.assertEqual(None, recursive_linear_search([], 1), 'case base size = 0')

    def test_case_1(self):
        self.assertEqual(None, recursive_linear_search([2], 1))
        self.assertEqual(0, recursive_linear_search([1], 1))

    def test_case_2(self):
        self.assertEqual(None, recursive_linear_search([1, 2, 3, 4, 5, 6, 7], 0))
        self.assertEqual(None, recursive_linear_search('abcdef', 'g'))
        self.assertEqual(5, recursive_linear_search('abcdef', 'f'))
        self.assertEqual(4, recursive_linear_search('abcdef', 'e'))
        self.assertEqual(3, recursive_linear_search('abcdef', 'd'))
        self.assertEqual(2, recursive_linear_search('abcdef', 'c'))
        self.assertEqual(1, recursive_linear_search('abcdef', 'b'))
        self.assertEqual(0, recursive_linear_search('abcdef', 'a'))