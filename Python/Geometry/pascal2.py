def next_pascal(row: [int]) -> [int]:
    pre = [0] + row
    post = row + [0]
    prepost = []
    for i in range(len(pre)):
        prepost.append(pre[i] + post[i])
    return prepost


def pascal(size: int) -> [str]:
    rows, row = [], [1]
    for r in range(size):
        rows.append(row)
        row = next_pascal(row)
    return rows


def pascal_output(size: int) -> str:
    answer = ''
    CRLF = "\n"
    for row in pascal(size):
        answer += format_row(row) + CRLF
    return answer


def format_row(row: [int]) -> str:
    srow = ''
    for num in row:
        srow += f'{num:4}'
    return srow.center(160)

print(pascal_output(10))