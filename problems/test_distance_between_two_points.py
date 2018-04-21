from unittest import TestCase

from problems.distance_between_two_points import f1, square_root, distance, output


class TestConsumption(TestCase):

    def test_f1(self):
        self.assertEqual(f1(0, 0), 0)
        self.assertEqual(f1(1, 0), 1)
        self.assertEqual(f1(1, 1), 0)
        self.assertEqual(f1(5, 3), 4)
        self.assertEqual(f1(3, 5), 4)
        self.assertEqual(f1(-1, -4), 9)
        self.assertEqual(f1(-4, -1), 9)

    def test_square_root(self):
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(9), 3)

    def test_distance_two_points(self):
        self.assertEqual(output(distance(1.0, 7.0, 5.0, 9.0)), '4.4721')
        self.assertEqual(output(distance(-2.5, 0.4, 12.1, 7.3)), '16.1484')
        self.assertEqual(output(distance(2.5, -0.4, -12.2, 7.0)), '16.4575')

