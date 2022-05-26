# 3/23/22

def largest_palindrome(start: int, upperLimit: int) -> int:
    productList = []
    for x in range(start, upperLimit):
        for y in range(x, upperLimit):
            product = x * y
            if is_palindrome(product):
                productList.append(product)
    return max(productList)


def find_multiples(upperLimit: int, divisorList=[]) -> list[int]:
    multipleList = []
    for value in range(upperLimit):
        for divisor in divisorList:
            if value % divisor == 0:
                multipleList.append(value)
    return trim_redundant_list(multipleList)


def trim_redundant_list(redundantList, trimmedList=[]) -> list[Any]:
    for x in redundantList:
        if x not in trimmedList:
            trimmedList.append(x)
    return trimmedList


DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
CUMULATIVE_DAYS = [[0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334],
                   [0, 0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]]


def nthdayofyear(s: str):
    month = int(s[:2])
    day = int(s[2:4])
    year = int(s[4:])
    if year % 4 == 0 or year % 400 == 0:
        return year * 1000 + day + CUMULATIVE_DAYS[1][month]
    else:
        return year * 1000 + day + CUMULATIVE_DAYS[0][month]
