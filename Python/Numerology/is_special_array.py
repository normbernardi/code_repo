#list is special if every even index contains an even number and every odd index contains an odd number. Create a function that returns True if an array is special, and False otherwise.
#is_special_array([2, 7, 4, 9, 6, 1, 6, 3]) ➞ True
#Even indices: [2, 4, 6, 6]; Odd indices: [7, 9, 1, 3]
#is_special_array([2, 7, 9, 1, 6, 1, 6, 3]) ➞ False
#Index 2 has an odd number 9.
#is_special_array([2, 7, 8, 8, 6, 1, 6, 3]) ➞ False
#Index 3 has an even number 8.
#Try with and without a list comprehension.

def is_even(x: int) -> bool:
    return x % 2 == 0

def is_special(arr: []) -> bool:
    for item in arr:
        index = arr.index(item)
        if is_even(item) and is_even(index):
            return True
        if not is_even(item) and is_even(index):
            return True
        else:
            return False

print(is_special([2, 7, 4, 9, 6, 1, 6, 3]))