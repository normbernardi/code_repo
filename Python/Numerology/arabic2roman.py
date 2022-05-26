arabic2roman_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: "X", 40: 'XL', 50: 'L', 90: 'XC',
                     100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}


def arabic2roman(arabic: int) -> str:
    output = ""
    for n in sorted(arabic2roman_dict, reverse=True):
        while arabic >= n:
            output += arabic2roman_dict[n]
            arabic -= n
    return output


print(arabic2roman(17))