def sort_descending(x: int) -> int:
    return digits_to_number(sorted(number_to_digits(x), reverse=True))


def sort_ascending(x: int) -> int:
    return digits_to_number(sorted(number_to_digits(x)))


def next_kaprekar(x: int) -> int:
    return sort_descending(x) - sort_ascending(x)

def number_to_digits(k: int) -> [int]:
    digits = []
    while k > 0:
        digits.append(k % 10)
        k //= 10
    digits.reverse()
    return digits


def digits_to_number(digits: [int]) -> int:
    x = 0
    for digit in digits:
        x = x * 10 + digit
    return x
