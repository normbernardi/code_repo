# 3/16/22
def next_leap_year(year: int) -> int:
    if year % 400 == 0 or year % 4 == 0:
        year += 4
    else:
        while (True):
            year += 1
            if year % 400 == 0 or year % 4 == 0:
                break
    return year



