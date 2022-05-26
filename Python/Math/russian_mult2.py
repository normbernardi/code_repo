def half_steps(n: int) -> [int]:
    res = [n]
    while n != 1:
        res.append(n // 2)
    return res

def russian_mult(a: int, b: int) -> []:
    PLUS, CROSS, SPACE, EQUAL = '+', 'X', " ", '='
    ab = 0
    while a > 0:
        if a % 2 > 0:
            sign = CROSS
        else:
            sign = PLUS
            ab += b
        print(f'{a:4d} {b:6d}' + SPACE + sign)
        a //= 2
        b *= 2
    print(EQUAL + f'{ab:10}')


russian_mult(1472, 73)
