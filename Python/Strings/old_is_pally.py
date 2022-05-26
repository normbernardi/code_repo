def store_each_digit(k: int):
    digits = []
    while k > 0:
        digits.append(k % 10)
        k //= 10
    digits.reverse()
    return digits


def reverse(x: int):
    reverse = 0
    while x > 0:
        reverse = (reverse * 10) + (x % 10)
        x //= 10
    return reverse


def is_palindrome(x: int):
    return x == reverse(x)


def palindrome_recipe(input: int):
    while not is_palindrome(input):
        input += reverse(input)
    return input