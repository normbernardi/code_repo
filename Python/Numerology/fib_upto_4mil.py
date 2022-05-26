LIMIT = 4000000
is_even = lambda x: x % 2 == 0


def make_fib() -> [int]:
    output = [1]
    tmp, last, current, = 0, 1, 2
    while current <= LIMIT:
        tmp = current
        output.append(current)
        current = current + last
        last = tmp
    return sum(list(filter(is_even, output)))

print(make_fib())
