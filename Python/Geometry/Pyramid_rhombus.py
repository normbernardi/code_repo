STAR = "*"
CRLF = "\n"
CENTER = 280


def pyramid_a2(size: int, sentinel: bool) -> [str]:
    pyramid = []
    if sentinel:
        for line_num in range(size):
            pyramid.append(line_num * STAR)
    else:
        for line_num in range(size, 0, -1):
            pyramid.append(line_num * STAR)
    return pyramid


def pyramid_format(pyramid: [str]) -> str:
    formatted_pyramid = ""
    for item in pyramid:
        formatted_pyramid += f'{item:2}'
    return formatted_pyramid.center(CENTER)


def pyramid_output(pyramid: int, reverse: bool) -> str:
    answer = ""
    for row in pyramid_a2(pyramid, True):
        answer += pyramid_format(row) + CRLF
    for row in pyramid_a2(pyramid, False):
        answer += pyramid_format(row) + CRLF
    return answer

print("*******************************************")
size = int(input("How large for the pyramid? "))
flip = bool(input("Print whole rhombus? True/False "))
print(pyramid_output(size, flip))

