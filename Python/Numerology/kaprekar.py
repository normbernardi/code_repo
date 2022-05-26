def next_kap(n: int) -> [int, int]:
    digits = find_digits(n)
    return sorted(digits) - sorted(digits, reverse=True)


def find_digits(n: int) -> [int]:
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return digits


def append_digits(n: [int]) -> int:
    number = 0
    for digit in n:
        number += number + digit * 10

def kaprekar_seq(n: int) -> [int]:
    seq = []
    while n != next_kap(n):
    ascending, descending = next_kap(n)


print(kaprekar_seq(1524))

print(next_kap(1524))