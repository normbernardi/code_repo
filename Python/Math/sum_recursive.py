def summation(seq) -> int:
    if not seq:
        return 0
    else:
        return seq[0] + summation(seq[1:])


print(summation([1, 5]))
print(summation([1, 2, 3, 4, 5, 6, 7]))
print(summation([5]))
print(summation([0]))
