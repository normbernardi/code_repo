def roll(side: int) -> int:
    import random
    return random.randint(1, side)

def tally_rolls(throws: int) -> [int]:
    output = []
    for x in range(throws):
        output.append(roll(20))
    return output

print(tally_rolls(5))