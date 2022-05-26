def display_in_reverse_order(*strings):
    new_s = ''
    for string in strings[::-1]:
        for char in string[::-1]:
            new_s += char
    return new_s


print(display_in_reverse_order("Hello", "Good", "Morning"))