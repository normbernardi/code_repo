def upper_lower(*strings) -> str:
    new_s = []
    for string in strings:
        if len(string) < 3:
            new_s.append(string.upper())
        else:
            new_s.append(string.lower())
    return ''.join(new_s)


print(upper_lower("ro", 'SHAM', 'do', 'pass', 'string', 'LOWER'))
print(upper_lower('MAKE', 'ALL', 'THESE', 'LOWER', 'PLEASE'))
print(upper_lower('trying10', 'w!th', 'SP3c!@l', 'c4@rs!#@*'))
