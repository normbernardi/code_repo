def longest_substr_pally(s: str) -> str:
    if not s:
        return ""
    if is_palindrome(s):
        return s
    pally = []
    for i in range(0, len(s)):
        test = []
        for j in range(i+1, len(s)):
            if is_palindrome(s[i:j]):
                test = [x for x in s[i:j]]
            j += 1
        if len(pally) < len(test):
            pally = test
    return "".join(pally)


def is_palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


print(longest_substr_pally(''))