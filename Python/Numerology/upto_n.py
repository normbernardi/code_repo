
def end_of_line(k: int) -> bool:
    r = 1
    triangle_num = 1
    while triangle_num < k:
        r += 1
        triangle_num = (r * (r + 1)) // 2
    return k == triangle_num

def make_line(k: int) -> [int]:
    line = [[]]
    for i in range(k):
        if end_of_line(i):
            line.append([])
        line[-1].append(i + 1)
    return line

def upto_n(n: int) -> str:
    output = ''
    for row in make_line(n):
        for i in row:
            output += f'{i:4}'
        output += '\n'
    return output + "**"

print(upto_n(21))
