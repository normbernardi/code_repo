def is_prime(n: int) -> bool:
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    factor = 3
    while factor * factor <= n:
        if n % factor == 0:
            return False
        factor += 2
    return True


def cycle_number(n: int) -> int:
    old_num = str(n)
    new_num = old_num[1:] + old_num[0]
    return int(new_num)


def is_circular_prime(n: int) -> bool:
    cycled_n = cycle_number(n)
    while cycled_n != n:
        if not is_prime(cycled_n):
            return False
        cycled_n = cycle_number(cycled_n)
    return True


print(is_circular_prime(115))
print(is_circular_prime(131))
