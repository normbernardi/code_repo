STAR = "*"

def multiply_pyramid(n:int) -> [str]:
    mult_pyramid = []
    for value in range(1, n+1):
        mult_pyramid.append(value * STAR)
    return "\n".join(mult_pyramid)

def right_triangle(n: int) -> str:
    pyramid = multiply_pyramid(n)
    formatted_triangle = " "
    for item in pyramid:
        formatted_triangle += f'{item:}'
    return formatted_triangle

print(right_triangle(7))