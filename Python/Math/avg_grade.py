def average_marks(**grades) -> float:
    total = 0
    for grade in grades.values():
        total += grade
    return "{:.2f}".format(total / len(grades))

print(average_marks(math = 65, science = 77, english = 81))
