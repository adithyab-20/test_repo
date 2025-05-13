"""Palindrome utility functions."""

def is_palindrome(text):
    """Check if a text is a palindrome."""
    # Remove spaces and convert to lowercase
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def reverse_string(text):
    """Reverse a string."""
    return text[::-1]

def get_longest_palindrome(text):
    """Get the longest palindromic substring."""
    if not text:
        return ""
    
    longest = ""
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            substring = text[i:j]
            if is_palindrome(substring) and len(substring) > len(longest):
                longest = substring
    return longest

def is_valid_palindrome(text):
    """Check if text is a valid palindrome (alphanumeric only)."""
    import re
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return cleaned == cleaned[::-1]

def find_all_palindromes(text, min_length=3):
    """Find all palindromic substrings of minimum length."""
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + min_length, len(text) + 1):
            substring = text[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return sorted(list(palindromes))

def has_palindrome_pattern(text):
    """Check if text contains any palindrome of length 3 or more."""
    return len(find_all_palindromes(text, min_length=3)) > 0
