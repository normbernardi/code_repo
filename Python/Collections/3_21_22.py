# 3/21/22
def find_sum_even_fibonacci() -> int:
    fib1 = 1
    fib2 = 2
    sum_fib = 2
    upperLimit = 4000000
    while fib1 <= upperLimit or fib2 <= upperLimit:
        fib1 = fib1 + fib2
        fib2 = fib1 + fib2
        if fib1 % 2 == 0:
            sum_fib += fib1
        if fib2 % 2 == 0:
            sum_fib += fib2
    return sum_fib


def find_sum_even_fibonacci_revised() -> int:
    fib1, fib2, sum_fib = 1, 2, 0  # in python you can one-line declare, use it more
    upperLimit = 4 * 10 ** 6  # make a hard coded 7-digit number easier to read and modify
    while fib1 <= upperLimit:
        fib1, fib2 = fib2, (fib1 + fib2)  # python making life easy and lines verbose yet again
        if fib1 % 2 == 0:  # using this alg theres no need to check if b=0 because b value is derivative of a, therefore all applicable values come into a before going into b
            sum_fib += fib1  # see above, don't run redundant code!!!
    return sum_fib


def euler003(x: int) -> int:
    largest_factor = 1  # pre-test value for largest_factor
    factor = 2  # intial value for factor, to check divisibility by 2
    while x % factor == 0:  # while x is still divisible by 2:
        if largest_factor < factor:  # if the largest factor is less than the divisor
            largest_factor = factor  # largest_factor becomes 2
        x //= factor  #
        # if n % 2 = 0, n could be % 2 numerous times
    factor = 3
    while x > 1:
        while x % factor == 0:
            if largest_factor < factor:
                largest_factor = factor
            x //= factor
        factor += 2
    return largest_factor


def is_prime(input: int) -> bool:
    x = 2
    if input == 0:
        return False
    while input >= x * x:
        if input % x == 0:
            return False
        x += 1
    return True


def largest_pally_3_digit(start: int, limit: int, ):
    largest_palindrome = 0
    m = start
    while m < limit:
        n = 1
        while n < limit:
            product = m * n
            if is_palindrome(product):
                if largest_palindrome < product:
                    largest_palindrome = product
            n += 1
        m += 1
    return largest_palindrome


def is_curzon(input: int) -> bool:
    divisor1 = 2 * (input) + 1
    divisor2 = 2 ** (input) + 1
    if divisor2 % divisor1 == 0:
        return True
    else:
        return False


def permute_number(x: int) -> int:
    s = str(x)
    digit = s[0]
    print("Starting at " + s)
    newS = s.replace(s[0], "0", 1) + digit
    print("Cycled number is: " + newS)
    return int(newS)


def is_circularprime(x: int) -> bool:
    if not is_prime(x):
        return False
    cycled_x = permute_number(x)
    while cycled_x != x:
        if not is_prime(x):
            return False
        cycled_x = permute_number(cycled_x)
    return True


def is_valid_triangle(side1: int, side2: int, side3: int) -> bool:
    if 0 in (side1, side2, side3):
        return False
    print(str(side1) + " " + str(side2) + " " + str(side3))
    if side1 + side2 > side3:
        if side2 + side3 > side1:
            if side1 + side3 > side2:
                return True
    return False
