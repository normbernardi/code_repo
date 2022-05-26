def snake_to_camel(s: str) -> str:
    words = s.split('_')
    for x in range(1, len(words)):
        words[x] = words[x].capitalize()
    return ''.join(words)


def camel_to_snake(s: str) -> str:
    snake = ''
    for char in s:
        if char.isalnum():
            if char.isupper():
                snake += '_' + char.lower()
            else:
                snake += char
    return snake

print("Camel:")
print('basic_salary_in_dollars -> '+ snake_to_camel("basic_salary_in_dollars") + "\n")
print("Snake:")
print('basicSalaryInDollar -> ' + camel_to_snake("basicSalaryInDollar") + '\n')
print('basi cSalary!@ InDoll !ar -> ' + camel_to_snake("basi cSalary!@ InDoll !ar") + '\n')