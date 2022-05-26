def calculate_gross(base_salary: int, bonus=500) -> float:
    ss = base_salary * .1
    state = base_salary * .12
    return base_salary - ss - state + bonus

print(calculate_gross(134000, 1500))