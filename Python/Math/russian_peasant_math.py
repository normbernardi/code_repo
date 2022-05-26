def half_number(input: int) -> [int]:
    num_div2 = [input]
    while input > 1:
        input //= 2
        num_div2.append(input)
    return num_div2

def double_number(input: int, first_length: int) -> [int]:
    num_mult2 = [input]
    while len(num_mult2) < first_length:
        input *= 2
        num_mult2.append(input)
    return num_mult2

def format_column(values: [int]) -> [str]:
    str_values = [str(x) for x in values]
    return str_values

def peasant_output(first: int, second: int) -> [str]:
    total = 0
    ADD = " +"
    SKIP = " x"
    first_column = half_number(first)
    second_column = (double_number(second, len(first_column)))
    for a, b in zip(format_column(first_column), format_column(second_column)):
        if not int(a) % 2 == 0:
            print(a + "\t" + b + ADD)
            total += int(b)
        else:
            print(a + "\t" + b + SKIP)
    return total
print("Output is: " + str(peasant_output(2571, 972)))
print(2571 * 972)
