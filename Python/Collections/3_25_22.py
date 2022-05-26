#3/25/22
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


def sort_descending(x: int) -> int:
    return digits_to_number(sorted(number_to_digits(x), reverse=True))


def sort_ascending(x: int) -> int:
    return digits_to_number(sorted(number_to_digits(x)))


def next_kaprekar(x: int) -> int:
    return sort_descending(x) - sort_ascending(x)


def kaprekar_seq(x: int) -> [int]:
    solution = [x]
    while x != next_kaprekar(x):
        x = next_kaprekar(x)
        solution.append(x)
    return solution


def collatz_seq(k: int) -> [int]:
    seq = []
    while k != 4:
        seq.append(k)
        k = next_collatz(k)
    seq.extend([4, 2, 1])
    return seq

def next_collatz(n: int) -> int:
    return n // 2 if n % 2 == 0 else 3 * n + 1
