def two_of_three(a: bool, b: bool, c: bool) -> bool:
    true_bools = 0
    minimum_requirement = 2
    if a:
        true_bools += 1
    if b:
        true_bools += 1
    if c:
        true_bools += 1
    return true_bools == minimum_requirement

print(two_of_three(True, True, True))
print(two_of_three(False, True, True))
print(two_of_three(False, False, True))
print(two_of_three(False, False, False))
print(two_of_three(False, True, True))