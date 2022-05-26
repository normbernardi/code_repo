def is_palindrome(s):
    """Checks if a given string is a palindrome"""

    # Empty strings and 1 character strings are palindromes
    if len(s) <= 1:
        return True
    # if first character is different from last it is not
    if s[0] != s[-1]:
        return False
    # Now first == last, so we can throw those out!
    return is_palindrome(s[1:-1])


print(is_palindrome("zerorez"))
