from unittest import TestCase

from katas.consumption import consumption

class TestConsumption(TestCase):

    def test_one(self):
        self.assertEqual(consumption(500, 35.0), 14.286)