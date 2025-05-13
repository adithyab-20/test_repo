"""Tests for palindrome module."""
from myproject.palindrome import is_palindrome, reverse_string, get_longest_palindrome

def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("hello") is False
    # Added edge cases
    assert is_palindrome("") is True
    assert is_palindrome("a") is True

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    # Added unicode test
    assert reverse_string("hello world") == "dlrow olleh"

def test_get_longest_palindrome():
    assert get_longest_palindrome("babad") == "bab"
    assert get_longest_palindrome("cbbd") == "bb"
    assert get_longest_palindrome("") == ""
    # Added edge cases
    assert get_longest_palindrome("a") == "a"
    assert get_longest_palindrome("abcdef") == "a"  # Single char is palindrome
