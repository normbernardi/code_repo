def aliquot(n: int) -> [int]:
    aliquot, divisor = 1, 2
    while divisor * divisor < n:
        if n % divisor == 0:
            aliquot += divisor + (n // divisor)
        divisor += 1
    if divisor * divisor == n:
        aliquot += divisor
    return aliquot


def classify(n: int) -> int:
    ali = aliquot(n)
    if ali == n:
        return 0
    elif ali <= n:
        return -1
    else:
        return 1

print(classify(1))

print(classify(15))

print(classify(100))

print(classify(1500))

print(classify(156))