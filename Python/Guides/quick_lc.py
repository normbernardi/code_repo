def camel_snake_lc(camel: str) -> str:
    UNDERSCORE = '_'
    return ''.join([(UNDERSCORE + char.lower()) if char.isupper() else char for char in camel])

def sum_unique_numbers(num_list: [int]):
    return sum([number for number in set(num_list)])

def sum_of_two(nums: [int], target: int) -> [int]:
    return [(i, j) for i in range(len(nums) - 1) for j in range(i + 1, len(nums)) if nums[i] + nums[j] == target]


print(sum_of_two([3,3], 6))