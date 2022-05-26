def valid_parentheses(string):
    parentheses = "()"
    for char in string:
        if char.isalnum() or char.isspace():
            string = string.replace(char, '')
    if not is_paired_parens(string):
        return False
    while any(x in string for x in parentheses):
        for pares in parentheses:
            string = string.replace(pares, "")
    if len(string) == 0:
        print('String empty')
    return string

def is_paired_parens(string):
    open, close = 0, 0
    OPEN, CLOSE = ord("("), ord(")")
    for char in string:
        if ord(char) == OPEN:
            open += 1
        if ord(char) == CLOSE:
            close += 1
    return open == close

print(valid_parentheses('hi())('))