def is_anagram(input_string: str, check_string: str) -> bool:
    if len(input_string) != len(check_string):
        return False
    for a, b in zip(sorted(input_string.lower()), sorted(check_string.lower())):
        if a != b:
            return False
    return True