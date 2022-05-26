def all_digits_even(n: int) -> bool:
    for x in str(n):
        if int(x) % 2 != 0:
            return False
    return True

def all_digits_even_2(x: int) -> bool:
    if x < 0:
        x /= -1
    while x >= 0:
        digit = 0
        digit = x % 10
        x //= 10
        if digit % 2 != 0:
            return False
        if x < 10 and x % 2 == 0:
            return True

