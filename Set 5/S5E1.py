import unittest


def is_palindrome(word):
    if not isinstance(word, str):
        raise TypeError("Input must be a string.")
    return word.lower() == word[::-1].lower()


class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("Radar"))
        self.assertFalse(is_palindrome("Hello"))
        self.assertFalse(is_palindrome("radars"))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            is_palindrome(123)
        with self.assertRaises(TypeError):
            is_palindrome([1, 2, 3])


if __name__ == '__main__':
    unittest.main()
