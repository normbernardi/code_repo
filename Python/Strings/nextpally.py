def is_palindrome(x: int) -> bool:
    number = find_digits(x)
    rev_number = [e for e in reversed(number)]
    for x in range(len(number)):
        if number[x] != rev_number[x]:
            return False
    return True


def find_digits(x: int) -> [int]:
    digits = []
    while x > 0:
        digits.append(x % 10)
        x //= 10
    return digits

