def rot13(phrase: str) -> str:
    encoded_string = []
    cipher_value = 13
    uppercase_upper_limit = 90
    lowercase_lower_limit, lowercase_upper_limit = 97, 122
    for letter in phrase:
        if letter.isupper() and ord(letter) + cipher_value > uppercase_upper_limit:
            encoded_string.append(chr(ord(letter) - cipher_value))
        elif letter.islower() and ord(letter) + cipher_value > lowercase_upper_limit:
            encoded_string.append(chr(ord(letter) - cipher_value))
        elif letter.isalpha():
            encoded_string.append(chr(ord(letter) + cipher_value))
        else:
            encoded_string.append(letter)
    return "".join(encoded_string)


def fizz_buzz(x: int) -> [str]:
    fizz_buzz_list = [str]
    divisor1, divisor2 = 3, 5
    for number in range(0, x + 1):
        if number % divisor1 == 0 and number % divisor2 == 0:
            fizz_buzz_list.append("FizzBuzz")
        elif number % divisor1 == 0:
            fizz_buzz_list.append("Fizz")
        elif number % divisor2 == 0:
            fizz_buzz_list.append("Buzz")
        else:
            fizz_buzz_list.append(str(number))
    return fizz_buzz_list


def split_Even_Odd_Sublist(num_array):
    sorted_list = []
    evens_list = []
    odds_list = []
    for value in num_array:
        if value % 2 == 0:
            evens_list.append(value)
        else:
            odds_list.append(value)
    sorted_list.append(evens_list)
    sorted_list.append(odds_list)
    return sorted_list


def shifu_split(nums: [int]) -> ([int], [int]):
    sublists = [[], []]
    for num in nums:
        sublists[num % 2].append(num)
    return sublists[1], sublists[0]


def ndigits(n: int) -> int:
    if n < 10:
        return 1
    return 1 + ndigits(n // 10)


def verify_ascent(n: int) -> bool:
    if n < 10:
        return True
    if n % 10 <= (n // 10) % 10:
        return False
    return verify_ascent(n // 10)


def ispowerof2(n: int) -> bool:
    while n != 1:
        if n % 2 == 1:
            return False
        n //= 2

    return True









