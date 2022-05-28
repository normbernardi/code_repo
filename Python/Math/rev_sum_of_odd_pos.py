def rev_sum_of_odd_pos(n: int) -> bool:
    return sum([int(odds) for odds in str(n)[1::2]]) % 2 == 0
