special = '\/~!@#$%^&*()-_=+{}[]\"'
vowels = 'aeiou'


def vowel_count(phrase: str) -> int:
    count = 0
    for letter in phrase.lower():
        if letter in vowels:
            count += 1
    return count


def consonant_count(phrase: str) -> int:
    count = 0
    for letter in phrase.lower():
        if letter not in vowels:
            if letter.isalpha():
                count += 1
    return count


def digit_count(phrase: str) -> int:
    count = 0
    for char in phrase.lower():
        if char.isdigit():
            count += 1
    return count


def special_count(phrase: str) -> int:
    count = 0
    for char in phrase.lower():
        if not char.isspace():
            if char in special:
                count += 1
    return count


def multi_count(phrase: str) -> str:
    print("Vowels in phrase: " + str(vowel_count(phrase)))
    print("Consonants in phrase: " + str(consonant_count(phrase)))
    print("Digits in phrase: " + str(digit_count(phrase)))
    print("Special characters in phrase: " + str(special_count(phrase)))
    return ""

def vowel_to_upper_cons_to_lower(string: str) -> str:
    output_string = ""
    for character in string:
        if character in vowels or character in vowels.upper():
            output_string += character.upper()
        else:
            output_string += character.lower()
    return output_string