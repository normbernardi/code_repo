POWER = 3
raise_to_power = lambda x: x ** POWER


def find_digits(x: int) -> [int]:
    output = []
    while x > 0:
        output.append(x % 10)
        x //= 10
    return output


def is_armstrong(x: int) -> bool:
    return sum(list(map(raise_to_power, [x for x in find_digits(x)]))) == x


def make_armstrong(start: int, end: int) -> [int]:
    return list(filter(is_armstrong, [x for x in range(start, end)]))


print(make_armstrong(100, 1000))




