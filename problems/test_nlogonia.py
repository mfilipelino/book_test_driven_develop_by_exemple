from unittest import TestCase
from problems.nlogonia import validate_input, residence_is_located


class NlogoniaImpTestCase(TestCase):
    def test_number_testes_invalid(self):
        self.assertFalse(validate_input(0))
        self.assertFalse(validate_input(1001))

    def test_number_testes_valid(self):
        self.assertTrue(validate_input(1))
        self.assertTrue(validate_input(2))
        self.assertTrue(validate_input(10))

    def test_output_divisa(self):
        self.assertEqual(residence_is_located(east_weast=0, north_south=0, x=0, y=0), 'divisa')
        self.assertEqual(residence_is_located(east_weast=0, north_south=0, x=1, y=0), 'divisa')
        self.assertEqual(residence_is_located(east_weast=0, north_south=0, x=0, y=-1), 'divisa')

    def test_output_ne(self):
        self.assertEqual(residence_is_located(east_weast=0, north_south=0, x=-1, y=1), 'NO')

    def test_output_se(self):
        self.assertEqual(residence_is_located(east_weast=0, north_south=0, x=-1, y=-1), 'SO')

    def test_output_no(self):
        self.assertEqual(residence_is_located(east_weast=0, north_south=0, x=1, y=1), 'NE')

    def test_output_so(self):
        self.assertEqual(residence_is_located(east_weast=0, north_south=0, x=1, y=-1), 'SE')
