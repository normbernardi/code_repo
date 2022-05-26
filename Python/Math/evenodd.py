def even_odd_sublist(num_list) -> (list, list):
    even = []
    odd = []
    for i in num_list:
        if is_even(i):
            even.append(i)
        else:
            odd.append(i)
    return even, odd


def is_even(n: int) -> bool:
        return n % 2 == 0

print(even_odd_sublist([1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))