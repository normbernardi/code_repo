# 3/14/22
from typing import List, Any


def sum_of_digits(k: int) -> int:
    sod = 0
    while k > 0:
        print("K before %: " + str(k))
        sod += k % 10
        print("K after % but before //: " + str(k))
        print("Remainder of k % 10: " + str(sod))
        k //= 10
        print("K after //: " + str(k))
    return sod


def factorial(x: int) -> int:
    fact = 1
    if x < 0:
        return -1
    for i in range(x):
        fact *= (x - i)
    return fact
