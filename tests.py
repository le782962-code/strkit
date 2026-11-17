import unittest
from strkit import (
    slugify, truncate, title_case, extract_emails,
    remove_whitespace, capitalize_words, reverse_words, count_words,
    is_palindrome, remove_punctuation, to_leet,
)


class TestStrkit(unittest.TestCase):

    def test_slugify_basic(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_slugify_multiple_spaces(self):
        self.assertEqual(slugify("  Extra   Spaces  "), "extra-spaces")

    def test_slugify_underscores(self):
        self.assertEqual(slugify("hello_world"), "hello-world")

    def test_truncate_short(self):
        self.assertEqual(truncate("Hi", 10), "Hi")

    def test_truncate_exact(self):
        self.assertEqual(truncate("Hello", 5), "Hello")

    def test_truncate_long(self):
        self.assertEqual(truncate("A very long string", 10), "A very lo...")

    def test_title_case(self):
        self.assertEqual(title_case("the quick brown fox"), "The Quick Brown Fox")

    def test_extract_emails(self):
        text = "Contact: alice@example.com or bob@test.org"
        self.assertEqual(extract_emails(text), ["alice@example.com", "bob@test.org"])

    def test_remove_whitespace(self):
        self.assertEqual(remove_whitespace("Hello,\n\nWorld!"), "Hello, World!")

    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")

    def test_reverse_words(self):
        self.assertEqual(reverse_words("the quick brown fox"), "fox brown quick the")

    def test_count_words(self):
        self.assertEqual(count_words("the quick brown fox"), 4)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))

    def test_remove_punctuation(self):
        self.assertEqual(remove_punctuation("Hello, World!"), "Hello World")

    def test_to_leet(self):
        self.assertEqual(to_leet("hello world"), "h3ll0 w0rld")


if __name__ == "__main__":
    unittest.main()
