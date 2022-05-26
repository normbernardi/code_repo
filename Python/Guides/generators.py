# Demonstration of the generator object
def sequence(k: int):
    i = 1
    while i <= k:
        yield i
        i += 1


def fibonacci(limit):
    current, last, tmp = 1, 0, 0
    while current <= limit:
        if current % 2 == 0:
            yield current
        tmp = current
        current += last
        last = tmp


def fizz_buzz(limit):
    for i in range(1, limit+1):
        if i % 15 == 0:
            yield "FIZZBUZZ"
        elif i % 3 == 0:
            yield "FIZZ"
        elif i % 5 == 0:
            yield "BUZZ"
        else:
            yield i


fizzbuzz_gen = fizz_buzz(15)

print(list(fizzbuzz_gen))


