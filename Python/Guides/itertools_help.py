from itertools import combinations as nCr

lst = [tuple(''.join(_) for _ in nCr("123456789", size)) for size in range(2, 9)]
trim = lst[3-2]
print(trim)
print(len(trim))