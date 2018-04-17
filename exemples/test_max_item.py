from unittest import TestCase

from exemples.max_items import max_item


class TestMaxItem(TestCase):

    def test_list_empty(self):
        self.assertEqual(max_item([]), [])

    def test_list_one_item(self):
        self.assertEqual(max_item([1]), 1)
        self.assertEqual(max_item([5]), 5)

    def test_list_two_items(self):
        self.assertEqual(max_item([1, 2]), 2)
        self.assertEqual(max_item([2, 1]), 2)

    def test_list_three_items(self):
        self.assertEqual(max_item([1, 2, 3]), 3)
        self.assertEqual(max_item([3, 2, 1]), 3)
        self.assertEqual(max_item([2, 3, 1]), 3)

    def test_list_all_items(self):
        self.assertEqual(max_item([1, 2, 3, 4]), 4)
        self.assertEqual(max_item([4, 3, 2, 1]), 4)
        self.assertEqual(max_item([4, 2, 1, 3]), 4)
        self.assertEqual(max_item([2, 4, 1, 3]), 4)