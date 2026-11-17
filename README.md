# strkit

A minimal, zero-dependency string toolkit for Python. No bloat, just the functions you actually need.

## Install

pip install strkit

## Usage

from strkit import slugify, truncate, title_case, extract_emails

slugify("Hello, World!")  # "hello-world"
truncate("A very long string that goes on and on", 20)  # "A very long strin..."
title_case("the quick brown fox")  # "The Quick Brown Fox"
extract_emails("Contact: alice@example.com or bob@test.org")  # ["alice@example.com", "bob@test.org"]

## Functions

- slugify(text) - converts text to a URL-safe slug
- truncate(text, length) - truncates text with ellipsis
- title_case(text) - converts to Title Case
- extract_emails(text) - finds all email addresses
- remove_whitespace(text) - collapses multiple spaces/newlines
- capitalize_words(text) - capitalizes first letter of each word
- reverse_words(text) - reverses word order
- count_words(text) - returns word count
- is_palindrome(text) - checks if text is a palindrome
- remove_punctuation(text) - removes all punctuation
- to_leet(text) - converts to leetspeak

## Why strkit?

Most string libraries are either too small or too bloated. strkit is the sweet spot: focused functions, zero dependencies, fully typed, with a test suite.

## Contributing

Fork the repo, make your change, open a PR. All contributions welcome.

## License

MIT
