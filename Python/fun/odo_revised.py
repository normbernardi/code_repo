def digit_count(n: int) -> int:
    return len(str(n))

def last_digit(n: int) -> int:
    return n % 10

def is_ascending(n: int) -> bool:
    while n > 9:
        if last_digit(n) <= last_digit(n // 10):
            return False
        n //= 10
    return True

def get_limits(n: int) -> (int, int):
    size = digit_count(n)
    DIGITS = "123456789"
    return int(DIGITS[:size]), int(DIGITS[-size:])

def next_reading(reading: int) -> int:
    if not is_ascending(reading):
        return -1
    START, LIMIT = get_limits(reading)
    if reading == LIMIT:
        return START
    reading += 1
    while not is_ascending(reading):
        reading += 1
    return reading

print(next_reading(789))