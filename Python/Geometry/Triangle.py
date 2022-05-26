STAR, SPACE, CRLF = "*", " ", "\n"

START, REPEAT, END = STAR, SPACE + STAR, ""

WIDTH = 60

def start_line(line_numLint) -> str:
    return START

def repeat_middle(line_num: int) -> str:
    return line_num * REPEAT

def end_line(line_num: int) -> str:
    return END

def line(line_num: int) -> str:
    return start_line(line_num) + repeat_middle(line_num) + end_line(line_num)

def make_pyramid(size: int) -> [str]:
    pyramid = []
    for line_num in range(size):
        pyramid.append(line(line_num))
    return pyramid

def format_mirror_tri(ps: [str]) -> str:
    pyramid = []
    for p in ps:
        pyramid.append(p.rjust(WIDTH))
    return CRLF.join(pyramid)

print(format_mirror_tri(make_pyramid(7)))
