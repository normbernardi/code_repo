def pyramid(n:int) -> [str]:
    pyramid = []
    for i in range(1, n + 1):
        pyramid.append(f'{i:3d}' * i)
    return pyramid

def rev_pyramid(n:int) -> [str]:
    rev_pyramid = []
    for i in range((1-n), 0):
        rev_pyramid.append((f'{-i:3d}' * -i))
    return rev_pyramid

def print_pyramid(size: int) -> None:
    print(("\n".join(pyramid(size))))
    print("\n".join(rev_pyramid(size)))

def multiply_pyramid(n:int) -> [str]:
    mult_pyramid = []
    for value in range(1, n+1):
        mult_pyramid.append(make_line(value))
    return "\n".join(mult_pyramid)


def make_line(n:int) -> str:
    line = ""
    for x in range(1, n+1):
        line += str(n*x) + ","
    return line[:-1]

def rev_mult_pyramid(n:int) -> [str]:
    rev_pyramid = []
    for i in range(n-1, 0, -1):
        rev_pyramid.append(make_line(i))
    return "\n".join(rev_pyramid)

def format_pyramid(n: int) -> str:
    print(multiply_pyramid(n))
    print(rev_mult_pyramid(n))
    return "Done"


print(format_pyramid(27))