def is_curzon(n: int) -> bool:
    return (2 ** n + 1) % (2 * n + 1) == 0

print(is_curzon(14))
print(is_curzon(5))
print(is_curzon(10))