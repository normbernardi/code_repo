def prime_sequence(limit: int) -> [int]:
    primes = []
    for i in range(limit):
        if is_prime(i):
            primes.append(i)
    return primes


def is_prime(k: int) -> bool:
    if k == 2 or k == 3:
        return True
    if k % 2 == 0 or k < 2:
        return False
    r = 3
    while r * r <= k:
        if k % r == 0:
            return False
        r += 2
    return True

print(prime_sequence(25))
