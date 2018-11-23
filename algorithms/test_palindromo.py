from unittest import TestCase

from algorithms.palindromo import recursive_palindromo


class TestPalindromo(TestCase):

    def test_str_empty(self):
        self.assertTrue(recursive_palindromo(''))

    def test_str_one_char(self):
        self.assertTrue(recursive_palindromo('a'))
        self.assertTrue(recursive_palindromo('b'))
        self.assertTrue(recursive_palindromo('c'))

    def test_str_two_char(self):
        self.assertFalse(recursive_palindromo('ab'))
        self.assertFalse(recursive_palindromo('ba'))
        self.assertTrue(recursive_palindromo('aa'))
        self.assertTrue(recursive_palindromo('cc'))

    def test_str_tree_char(self):
        self.assertFalse(recursive_palindromo('abc'))
        self.assertFalse(recursive_palindromo('acb'))
        self.assertTrue(recursive_palindromo('aba'))
        self.assertTrue(recursive_palindromo('bab'))
        self.assertTrue(recursive_palindromo('bbb'))

    def test_all(self):
        self.assertTrue(recursive_palindromo('abccba'))
        self.assertTrue(recursive_palindromo('abcfcba'))
        self.assertFalse(recursive_palindromo('abdcba'))
        self.assertFalse(recursive_palindromo('abccea'))