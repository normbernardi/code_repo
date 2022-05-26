def valid_parens(string):
    for char in string:
        if char.isalnum() or char.isspace():
            string = string.replace(char, '')
    for char1 in string:
        if ord(char1) == ord("("):
            for char2 in string[::-1]:
                while
                    if ord(char2) == ord(")"):
                        string = string.replace(char1, "").replace(char2, "")
    return not string

print(valid_parens('hi())('))