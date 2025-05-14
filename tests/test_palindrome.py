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

def test_is_valid_palindrome():
    from myproject.palindrome import is_valid_palindrome
    assert is_valid_palindrome("A1B2C2B1A") is True
    assert is_valid_palindrome("race a car!") is False
    # Note: Not testing edge cases

def test_find_all_palindromes_basic():
    from myproject.palindrome import find_all_palindromes
    result = find_all_palindromes("ababa")
    assert "aba" in result
    assert "bab" in result
    # Note: Not testing min_length parameter

# Note: Not testing has_palindrome_pattern function at all

def test_find_all_palindromes_and_pattern():
    from myproject.palindrome import find_all_palindromes, has_palindrome_pattern
    pals = find_all_palindromes("racecar")
    # racecar itself, plus smaller ones, should appear
    assert "racecar" in pals
    assert has_palindrome_pattern("racecar") is True
    assert has_palindrome_pattern("xyz") is False
