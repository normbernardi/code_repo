def length(sequence) -> int:
    if not sequence:
        return 0
    else:
        return 1 + length(sequence[1:])


print(length((1, 2, 3)))
print(length([1, 2, 3]))
print(length('123'))
print(length([]))
print(length(()))
