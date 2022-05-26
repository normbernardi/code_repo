def fizzbuzz_logic(n: int) -> str:
    divisor1, divisor2 = 3, 5
    if n % divisor1 == 0 and n % divisor2 == 0:
        return 'fizzbuzz'
    elif n % divisor1 == 0:
        return 'fizz'
    elif n % divisor2 == 0:
        return 'buzz'
    else:
        return str(n)


def fizzbuzz(n: int) -> [str]:
    fb = []
    for i in range(1, n+1):
        fb.append(fizzbuzz_logic(i))
    return fb


print(fizzbuzz(15))
print(fizzbuzz(30))
