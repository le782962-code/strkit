"""strkit - A minimal, zero-dependency string toolkit for Python."""

import re
from typing import List


def slugify(text: str) -> str:
    """Convert text to a URL-safe slug.

    >>> slugify("Hello, World!")
    'hello-world'
    """
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[-\s]+", "-", text).strip("-")


def truncate(text: str, length: int) -> str:
    """Truncate text to a given length, appending ellipsis if needed.

    >>> truncate("A very long string", 10)
    'A very lo...'
    """
    if len(text) <= length:
        return text
    return text[: length - 3] + "..."


def title_case(text: str) -> str:
    """Convert text to Title Case.

    >>> title_case("the quick brown fox")
    'The Quick Brown Fox'
    """
    return text.title()


def extract_emails(text: str) -> List[str]:
    """Find all email addresses in text.

    >>> extract_emails("Contact: alice@example.com or bob@test.org")
    ['alice@example.com', 'bob@test.org']
    """
    return re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)


def remove_whitespace(text: str) -> str:
    """Collapse multiple spaces and newlines into single spaces.

    >>> remove_whitespace("Hello,\n\nWorld!")
    'Hello, World!'
    """
    return re.sub(r"\s+", " ", text).strip()


def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word.

    >>> capitalize_words("hello world")
    'Hello World'
    """
    return " ".join(word.capitalize() for word in text.split())


def reverse_words(text: str) -> str:
    """Reverse the order of words in text.

    >>> reverse_words("the quick brown fox")
    'fox brown quick the'
    """
    return " ".join(reversed(text.split()))


def count_words(text: str) -> int:
    """Count the number of words in text.

    >>> count_words("the quick brown fox")
    4
    """
    return len(text.split())


def is_palindrome(text: str) -> bool:
    """Check if text is a palindrome (ignoring case and non-alphanumeric).

    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    """
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", text.lower())
    return cleaned == cleaned[::-1]


def remove_punctuation(text: str) -> str:
    """Remove all punctuation from text.

    >>> remove_punctuation("Hello, World!")
    'Hello World'
    """
    return re.sub(r"[^\w\s]", "", text)


def to_leet(text: str) -> str:
    """Convert text to leetspeak.

    >>> to_leet("hello world")
    'h3ll0 w0rld'
    """
    mapping = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 't': '7'}
    return ''.join(mapping.get(c.lower(), c) for c in text)