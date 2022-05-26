def anagrams(word, words: [str]):
    sort_word = sorted(word)
    anagram = []
    for item in words:
        tmp = ''.join(sorted(item))
        if is_anagram(sort_word, tmp):
            anagram.append(tmp)
    return anagram


def is_anagram(original, check):
    if len(original) != len(check):
        return False
    for a, b in zip(original, check):
        if a != b:
            return False
    return True

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
