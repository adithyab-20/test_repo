"""Tests for palindrome module."""
from myproject.palindrome import is_palindrome, reverse_string, get_longest_palindrome

def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("hello") is False

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"

def test_get_longest_palindrome():
    assert get_longest_palindrome("babad") == "bab"
    assert get_longest_palindrome("cbbd") == "bb"
    assert get_longest_palindrome("") == ""
