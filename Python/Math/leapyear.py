def next_leap_year(n: int) -> int:
    if is_leap_year(n):
        return n + 4
    else:
        while not is_leap_year(n):
            n += 1
    return n


def is_leap_year(n: int) -> bool:
    if n % 4 == 0:
        return True
    elif n % 100 == 0 and n % 400 == 0:
        return True
    return False

print(next_leap_year(15))
