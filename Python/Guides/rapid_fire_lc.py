def fizzbuzz_lc(limit: int) -> [str]:
    return ['fizzbuzz' if x % 3 == 0 and x % 5 == 0 else 'fizz' if x % 3 == 0 else 'buzz' if x % 5 == 0 else x for x in
            range(1, limit + 1)]


def if_eight(limit: int) -> [int]:
    return [x for x in range(1, limit + 1) if '8' in str(x)]


def find_space(string: str) -> int:
    return len([char for char in string if char.isspace()])


def remove_vowel(string: str) -> str:
    return ''.join([char for char in string if not char in 'aeiouAEIOU'])


def check_words_under_six(string: str) -> [str]:
    return [word for word in string if len(word) < 6]


def multiply_lists(lst1: [int], lst2: [int]) -> [int]:
    return [x * y for x in lst1 for y in lst2]


def transpose_matrix(lst: [[int]]) -> [[]]:
    return [[row[i] for row in lst] for i in range(4)]


def return_seq(seq: str) -> str:
    return '->'.join([(char * (seq.index(char) + 1)).capitalize() for char in seq])


def roman2arabic(rom: str) -> int:
    roman_arabic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return sum([roman_arabic[x] for x in rom.replace('IV', 'IIII').replace('IX', 'VIIII').replace('XL', 'XXXX')
               .replace('XC', 'LXXXX')])
