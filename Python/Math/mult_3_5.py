LIMIT = 1000
print(sum([num for num in range(LIMIT) if num % 3 == 0 or num % 5 == 0]))

print(sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(LIMIT))))


