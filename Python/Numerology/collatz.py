def is_even(n: int) -> bool:
    return n % 2 == 0


def collatz_logic(n: int) -> [int]:
    collatz_seq = [n]
    while n != 1:
        n = next_collatz(n)
        collatz_seq.append(n)
        if n == 8:

    return format_collatz(collatz_seq)


def format_collatz(col: list) -> [int]:
    suffix = (4, 2, 1)
    if col[-1] != 4:
        col.extend(suffix)
    return col

def next_collatz(n: int) -> int:
    if is_even(n):
        n //= 2
    else:
        n = (n*3)+1
    return n


print(collatz_logic(7))
print(collatz_logic(42))
print(collatz_logic(19))
print(collatz_logic(1))
print(collatz_logic(5))
