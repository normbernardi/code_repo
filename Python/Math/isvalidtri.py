def is_valid_triangle(a: int, b: int, c: int) -> bool:
    return a + b > c and b + c > a and c + a > b

print(is_valid_triangle(7, 9, 13))
print(is_valid_triangle(4, 8, 15))