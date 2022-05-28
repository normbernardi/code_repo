def is_strong_number(num: int) -> bool:
    fact_sum = 0
    split = digits(num)
    for x in split:
        fact_sum += factorial(x)
    return fact_sum == num


def digits(num: int) -> [int]:
    if len(str(num)) < 1:
        return []
    if len(str(num)) == 1:
        return [num]
    return [num % 10] + digits(num // 10)


def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n-1)