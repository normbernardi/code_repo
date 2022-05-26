def best_of_3(a, b, c: int) -> int:
    if a > b:
        if a > c:
            return a
        else:
            return c
    elif b > c:
        return b
    else:
        return c

print(best_of_3(15, 16, 12))