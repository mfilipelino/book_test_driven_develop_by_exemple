from unittest import TestCase

from algorithms.linear_search import linear_search


class LinearSearchTestCase(TestCase):

    def test_instance_1(self):
        self.assertEqual(linear_search(1, []), None)