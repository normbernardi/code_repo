# def aliquot_old(input: int):
# aliquot = 0
# x = 1
# while x <= (input//2):
# if input % x == 0:
# aliquot += x
# x += 1
# return aliquot
def aliquot(x: int) -> int:
    aliq = 1
    divisor = 2
    while divisor ** 2 < x:
        if x % divisor == 0:
            aliq += divisor + (x // divisor)
        if divisor ** 2 == x:
            aliq += divisor
        divisor += 1
    return aliq


def heron(x: float):
    epsilon = 0.0000000001
    root = 0.5 * x
    while (root * root - x) > epsilon:
        root = (root + x / root) / 2
    return root


def classify(x: int) -> int:
    if aliquot(x) > x:
        return 1
    elif aliquot(x) < x:
        return -1
    else:
        return 0


def num_digits(x: int) -> int:
    counter = 0
    if x < 0:
        x /= -1
    while x > 0:
        x % 10
        x //= 10
        counter += 1
    return counter


def raise_digits_to_power(x: int, exponent: int) -> int:
    elevated_x = 0
    if x < 0:
        x /= -1
    while x > 0:
        elevated_x += (x % 10) ** exponent
        x //= 10
    return elevated_x


def is_armstrong(x: int) -> bool:
    elevated_x = raise_digits_to_power(x, 3)
    if elevated_x == x:
        return True
    else:
        return False
