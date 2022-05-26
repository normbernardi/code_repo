def length_longest_substring(s: str) -> int:
    if not s:
        return 0
    length = 1
    for i in range(0, len(s)):
        for j in range(i + 1, len(s)):
            if all_unique(s[i:j]):
                length = max(length, j - i)
    return length


def all_unique(s: str) -> bool:
    unique_set = set()
    for ch in s:
        if ch in unique_set:
            return False
        unique_set.add(ch)
    return True


print(length_longest_substring('thisisastring'))