#This odometer can only show digits 1 to 9
#Only the reading that are in ascending order are valid
#The odometer rolls over to the first valid reading after the last

def digit_count(n: int) -> int:
    return len(str(n))


def last_digit(n: int) -> int:
    return n % 10


def get_limits(n: int) -> (int, int):
    size = digit_count(n)
    DIGITS = '123456789'
    return int(DIGITS[:size]), int(DIGITS[-size:])


def is_ascending(r: int) -> bool:
    while r > 9:
        if last_digit(r) <= last_digit(r // 10):
            return False
        r //= 10
    return True


def next_reading(reading: int) -> int:
    if not is_ascending(reading):
        return -1
    START, LIMIT = get_limits(reading)
    if reading == LIMIT:
        return START
    while not is_ascending(reading):
        reading += 1
    return reading


def prev_reading(reading: int) -> int:
    if not is_ascending(reading):
        return -1
    START, LIMIT = get_limits(reading)
    if reading == START:
        return LIMIT
    reading -= 1
    while not is_ascending(reading):
        reading -= 1
    return reading


def nth_reading_after(reading: int, n: int) -> int:
    for i in range(n):
        reading = next_reading(reading)
    return reading


def nth_reading_before(reading: int, n: int) -> int:
    for i in range(n):
        reading = prev_reading(reading)
    return reading


def distance(read1: int, read2: int) -> int:
    if digit_count(read1) != digit_count(read2):
        return -1
    count = 0
    LOWER = get_limits(read1)
    if next_reading(read1) == LOWER:
        return -1
    while not read1 == read2:
        read1 = next_reading(read1)
        count += 1
    return count

def get_readings_for_limit(limit: int) -> [()]:
    return [next_reading(x) for x in range(1, limit+1) if next_reading(x) != -1]


def get_readings_for_size(size: int) -> [()]:
    return [next_reading(x) for x in range(1, int('1' * size))]

print(prev_reading(123))
print(prev_reading(156))
print(distance(789, 123))
print(get_readings_for_limit(14000))

#Write a function that returns all limits for a given size, all valid readings for a given size
