from unittest import TestCase

from search.linear_search import linear_search


class LinearSearchTestCase(TestCase):
    def test_instance_base(self):
        self.assertEqual(linear_search(1, []), None)
        self.assertEqual(linear_search(1, [1]), 0)
        self.assertEqual(linear_search(1, [2]), None)

    def test_intance_eq_1(self):
        self.assertEqual(linear_search(1, [2, 3]), None)
        self.assertEqual(linear_search(2, [2, 3]), 0)
        self.assertEqual(linear_search(3, [2, 3]), 1)

    def test_intance_3(self):
        self.assertEqual(linear_search(10, list(range(10))), None)
        self.assertEqual(linear_search(9, list(range(10))), 9)
        self.assertEqual(linear_search(4, [1, 2, 3, 4, 5]), 3)
