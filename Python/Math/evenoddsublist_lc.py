is_even = lambda x: x % 2 == 0

def even_odd_sublists(lst: []) -> ([], []):
    return [x for x in lst if is_even(x)] , [x for x in lst if not is_even(x)]

print(even_odd_sublists([2, 4, 6, 8, 1, 3, 5, 7, 9, 11, 12, 14, 15, 21]))