def pythagorean_triplets(arr: [int]) -> bool:
    a, b, c = sorted(arr)
    if a ** 2 + b ** 2 == c ** 2:
        return is_prime(a) and is_prime(b) or is_prime(c)
    else:
        return False

def is_prime(k: int) -> bool:
    if k == 2 or k == 3:
        return True
    if k % 2 == 0 or k < 2:
        return False
    r = 3
    while r * r <= k:
        if k % r == 0:
            return False
    return True
