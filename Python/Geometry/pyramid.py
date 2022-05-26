STAR = "*"
CRLF = "\n"
CENTER = 280

def rev_pyramid(size: int) -> [str]:
    pyramid = []
    for line_num in range(size, 0, -1):
        pyramid.append(line_num * STAR)
    return pyramid

def pyramid_format(pyramid: [str]) -> str:
    formatted_pyramid = ""
    for item in pyramid:
        formatted_pyramid += f'{item:2}'
    return formatted_pyramid.center(CENTER)

def pyramid_output(pyramid: int ) -> str:
    answer = ""
    for row in rev_pyramid(pyramid):
        answer += pyramid_format(row) + CRLF
    return answer

print(pyramid_output(7))