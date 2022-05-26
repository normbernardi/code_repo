#Version A
def fibs_a(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b

print(sum(x for x in fibs_a(4000000) if x % 2 == 0))

#Version B
def fibs(limit, pick):
    a, b = 0, 1
    while a < limit:
        if pick(a):
            yield a
        a, b = b, a+b

print(sum(x for x in fibs(4000000, lambda x: x % 2 == 0)))