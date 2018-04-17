from unittest import TestCase

from katas.multiples import multiples


class TestMultiplos(TestCase):

    def test_base(self):
        self.assertTrue(multiples(6, 24))
        self.assertFalse(multiples(6, 25))
        self.assertFalse(multiples(7, 3))
        self.assertTrue(multiples(4, 36))
        self.assertTrue(multiples(36, 4))





