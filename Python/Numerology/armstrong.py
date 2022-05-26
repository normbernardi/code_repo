def is_armstrong(n:int) -> bool:
    digits = find_digits(n)
    total = 0
    for x in digits:
        total += cube(x)
    return total == n


def cube(x: int) -> int:
    return x ** 3


def find_digits(x: int) -> [int]:
    digits = []
    while x > 0:
        digits.append(x % 10)
        x //= 10
    return digits


def armstrong_upto_n(n: int) -> [int]:
    armstrong = []
    for x in range(n):
        if is_armstrong(x):
            armstrong.append(x)
    return armstrong
