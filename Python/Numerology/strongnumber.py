def is_strong(n: int) -> bool:
    number = find_digits(n)
    total = 0
    for value in number:
        total += factorial(value)
    return total == n


def factorial(n: int) -> int:
    if n == 1:
        return 1
    return n * factorial(n-1)


def find_digits(x: int) -> [int]:
        digits = []
        while x > 0:
            digits.append(x % 10)
            x //= 10
        return digits

print(is_strong(131))
print(is_strong(145))