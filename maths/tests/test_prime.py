from unittest import TestCase
from maths.prime import is_prime


class TestIsPrime(TestCase):

    def test_case_base(self):
        self.assertEqual(False, is_prime(1))
        self.assertEqual(True, is_prime(2))

    def test_case_1(self):
        self.assertEqual(True, is_prime(3))
        self.assertEqual(False, is_prime(4))
        self.assertEqual(True, is_prime(5))
        self.assertEqual(False, is_prime(6))
        self.assertEqual(True, is_prime(7))
        self.assertEqual(False, is_prime(8))
        self.assertEqual(False, is_prime(9))
        self.assertEqual(False, is_prime(10))

    def test_168(self):
        self.assertEqual(
            len(
                list(
                    filter(
                        lambda x: x is True,
                        map(
                            is_prime,
                            range(1000)
                        )
                    )
                )
            ),
            168
        )


