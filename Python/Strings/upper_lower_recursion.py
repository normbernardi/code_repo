def upper_lower(*strings):
    string = ''
    for word in strings:
        if len(word) < 3:
            string = word.upper()
        else:
            string = word.lower()
    return string + upper_lower(strings[1])

print(upper_lower("ro", 'SHAM', 'do', 'pass', 'string', 'LOWER'))
print(upper_lower('MAKE', 'ALL', 'THESE', 'LOWER', 'PLEASE'))
print(upper_lower('trying10', 'w!th', 'SP3c!@l', 'c4@rs!#@*'))


