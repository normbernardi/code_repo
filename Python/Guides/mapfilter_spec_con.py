TEST = 'I wish, really wish, map & filter are taught earlier!'
def is_vowel(char: str) -> bool:
    VOWELS = 'aeiouAEIOU'
    return char in VOWELS


def is_special(char: str) -> bool:
    return not char.isalnum() and not char.isspace()

def is_con(char: str) -> bool:
    VOWELS = 'aeiouAEIOU'
    return char.isalpha() and not char in VOWELS


vowel_iterate = list(filter(is_vowel, TEST))
con_iterate = list(filter(is_con, TEST))
spec_iterate = list(filter(is_special, TEST))

print('Result: \n')
print(len(vowel_iterate), len(con_iterate), len(spec_iterate))
