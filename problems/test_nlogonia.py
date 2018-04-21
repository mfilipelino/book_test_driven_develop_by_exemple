from unittest import TestCase
import io
from problems.nlogonia import validate_input, residence_is_located, main


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


def add_input(s):
    return s + '\n'


class NlogoniaBehaveTest(TestCase):

    def test_case_1(self):
        input_case_1 = add_input('3') + add_input('2 1') + add_input('10 10') + add_input('-10 -1') + add_input(
            '0 33') + add_input('0')
        print('######## CASE 1 ######')
        print('### INPUT ###')
        print(input_case_1)
        print('### OUTPUT ###')
        main(io.StringIO(input_case_1))

    def test_case_2(self):
        input_case_2 = add_input('4') + add_input('-1000 -1000') + add_input('-1000 -1000') + add_input(
            '0 0') + add_input('-2000 -10000') + add_input('-999 -1001') + add_input('0')
        print('######## CASE 2 ######')
        print('### INPUT ###')
        print(input_case_2)
        print('### OUTPUT ###')
        main(io.StringIO(input_case_2))
