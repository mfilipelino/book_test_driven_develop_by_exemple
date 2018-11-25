from unittest import TestCase

from problems.consumption import consumption, output


class TestConsumption(TestCase):

    def test_out(self):
        self.assertEqual(output(consumption(500, 35.0)), '14.286 km/l')
        self.assertEqual(output(consumption(2254, 124.4)), '18.119 km/l')
        self.assertEqual(output(consumption(4554, 464.6)), '9.802 km/l')