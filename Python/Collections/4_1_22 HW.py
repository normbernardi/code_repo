def next_line(row: [int]) -> [str]:
    pre = [0] + row
    post = row + [0]
    added = []
    for a, b in zip(pre, post):
        added.append(a + b)
    return added

def pascal(level: int) -> [int]:
    rows, current_row = [], [1]
    for r in range(level):
        rows.append(current_row)
        current_row = next_line(current_row)
    return rows

def pascal_output(size: int) -> str:
    answer = ""
    CRLF = '\n'
    for row in pascal(size):
        answer += format_row(row) + CRLF
    return answer

def format_row(row: [int]) -> str:
    srow = ""
    for num in row:
        srow += f'{num:4}'
    return srow.center(80)

print(pascal_output(15))
