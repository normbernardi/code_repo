def factorial(x: int) -> int:
    fact = 1
    if x < 0:
        return -1
    for i in range(x):
        fact *= (x - i)
    return fact

def is_strong(x: int) -> bool:
    originalValue = x
    sumFactorial = 0
    while x > 0:
        digit = x % 10
        sumFactorial += factorial(digit)
        x //= 10
    if originalValue == sumFactorial:
        return True
    else:
        return False


def is_strong_in_range(min: int, max: int):
    sumFactorial = 0
    strongNums = []
    for i in range(min, max):
        originalValue = i
        sumFactorial = 0
        while i > 0:
            digit = i % 10
            sumFactorial += factorial(digit)
            i //= 10
        if originalValue == sumFactorial:
            strongNums.append(sumFactorial)
    return strongNums

def function(n: int) -> float:
    for i in range(1, n):
        print((4 * factorial(i)) / (7*factorial(i)))

print(function(5))