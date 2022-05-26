def count_characters(filename: str) -> (int, int):
    vowel, con = 0, 0
    VOWELS = 'aeiouAEIOU'
    local_file = open(filename, "r")
    local_line = local_file.readline()
    while local_line != "":
        for char in local_line:
            if char in VOWELS:
                vowel += 1
            elif char.isalpha():
                con += 1
            local_line = local_file.readline()
    return vowel, con

print(count_characters('Content.txt'))