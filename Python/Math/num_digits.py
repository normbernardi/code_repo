def num_digits(n: int) -> int:
    return len(str(n))

def num_digits_nostr(n: int) -> int:
    digits_count = 0
    while n > 0:
        digits_count += 1
        n //= 10
    return digits_count

print(num_digits(1554))
print(num_digits_nostr(1554))

