from unittest import TestCase

from examples.palindromo import palindromo


class TestPalindromo(TestCase):

    def test_str_empty(self):
        self.assertTrue(palindromo(''))

    def test_str_one_char(self):
        self.assertTrue(palindromo('a'))
        self.assertTrue(palindromo('b'))
        self.assertTrue(palindromo('c'))

    def test_str_two_char(self):
        self.assertFalse(palindromo('ab'))
        self.assertFalse(palindromo('ba'))
        self.assertTrue(palindromo('aa'))
        self.assertTrue(palindromo('cc'))

    def test_str_tree_char(self):
        self.assertFalse(palindromo('abc'))
        self.assertFalse(palindromo('acb'))
        self.assertTrue(palindromo('aba'))
        self.assertTrue(palindromo('bab'))
        self.assertTrue(palindromo('bbb'))

    def test_all(self):
        self.assertTrue(palindromo('abccba'))
        self.assertTrue(palindromo('abcfcba'))
        self.assertFalse(palindromo('abdcba'))
        self.assertFalse(palindromo('abccea'))