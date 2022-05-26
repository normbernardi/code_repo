STAR, SPACE, CRLF = '*', ' ', '\n'
START, REPEAT, END = STAR, SPACE + STAR, ''
WIDTH = 160

def line(line_num: int) -> str:
    return start_line(line_num) + repeat_middle(line_num) + end_line(line_num)

def start_line(line_num: int) -> str:
    return START

def repeat_middle(line_num) -> str:
    return line_num * REPEAT

def end_line(line_num: int) -> str:
    return END

def make_pyramid(size: int) -> [str]:
    pyramid = []
    for line_num in range(size):
        pyramid.append(line(line_num))
    return pyramid

def pyramid(ps: [str]) -> str:
    pyr = []
    for p in ps:
        pyr.append(p.center(WIDTH))
    return CRLF.join(pyr)


def upside_down_triangle(ps: [str]) -> str:
    tri = []
    for p in ps[::-1]:
        tri.append(p.center(WIDTH))
    return CRLF.join(tri)

def rjust_triangle(ps: [str]) -> str:
    tri = []
    for p in ps:
        tri.append(p)
    return CRLF.join(tri)

def ljust_triangle(ps: [str]) -> str:
    tri = []
    for p in ps:
        tri.append(p.rjust((WIDTH // 2)))
    return CRLF.join(tri)

print(pyramid(make_pyramid(7)) + CRLF)
print((upside_down_triangle((make_pyramid(7)))) + CRLF)
print((rjust_triangle((make_pyramid(7)))) + CRLF)
print((ljust_triangle((make_pyramid(7)))) + CRLF)