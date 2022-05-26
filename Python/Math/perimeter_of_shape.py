def perimeter_of_shape(*sides) -> int:
    side_count = len(sides)
    if side_count == 2:
        return 2 * (sides[0] + sides[1])
    elif side_count == 3:
        return sides[0] + sides[1] + sides[2]
    else:
        res = 1
        for x in sides:
            res *= x
        return res


print(perimeter_of_shape(2, 2))
print(perimeter_of_shape(3, 3, 3))
print(perimeter_of_shape(4, 4, 4, 4))
print(perimeter_of_shape(5, 5, 5, 5, 5))
print(perimeter_of_shape(6, 6, 6, 6, 6, 6))
