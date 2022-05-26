def fizzbuzz(n: int) -> str:
    if n % 15 == 0:
        return 'FIZZBUZZ'
    elif n % 3 == 0:
        return 'FIZZ'
    elif n % 5 == 0:
        return 'BUZZ'
    else:
        return str(n)

def fizzbuzz_map(k: int) -> [str]:
    return list(map(fizzbuzz, range(1, k+1)))

print(fizzbuzz_map(15))
