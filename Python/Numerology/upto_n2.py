def end_of_line(n: int) -> bool:
    r = 1
    while (r * (r + 1)) // 2 < n:
        r += 1
    return n == (r * (r + 1)) // 2

def upto_n(n: int) -> str:
    CRLF = "\n"
    output = ""
    for i in range(1, n):
        item = f'{i:4}'
        if end_of_line(i):
            item += CRLF
        output += item
    output += f'{n:4}' + CRLF + "**" + CRLF
    return output

print(upto_n(15))