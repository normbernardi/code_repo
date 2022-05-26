def find_digits(n: int) -> [int]:
    digits = []
    while n!=0:
        digits.append(n % 10)
        n //= 10
    return digits[::-1]


numbers = (145, 321, 658, 996, 9682, 11435)
print(list(map(find_digits, numbers)))