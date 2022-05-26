def fb_test(x: int) -> [str]:
    fizzbuzz_dict = {(True, True): 'fizzbuzz',
                     (True, False): 'fizz',
                     (False, True): 'buzz',
                     (False, False): str(x)}
    return fizzbuzz_dict[x % 3 == 0, x % 5 == 0]


def fizzbuzz(n: int) -> [str]:
    output = []
    for x in range(1, n):
        output.append(fb_test(x))
    return output

print(fizzbuzz(21))