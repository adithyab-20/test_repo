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
