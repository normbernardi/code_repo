def count_characters(filename: str):
    number, letter = 0, 0
    symbol, space = 0, 0
    make_test_file(filename)
    local_file = open(filename, "r")
    local_line = local_file.readline()
    while local_line != "":
        for char in local_line:
            if char.isspace():
                space += 1
            elif not char.isalnum():
                symbol += 1
            elif not char.isalpha():
                number += 1
            else:
                letter += 1
        local_line = local_file.readline()
    return number, letter, symbol, space


def make_test_file(filename: str):
    local_file = open(filename, "w")
    local_file.write("This is a test file. 12345 !@#$%\n")
    local_file.write(" It can also do multiple lines!\n")
    local_file.write(" How c001 i5 t4@t?!")
    local_file.close()


a, b, c, d= count_characters("test.txt")
file = open('test.txt', 'r')

file_lines = ''
line = file.readline()
while line != "":
    file_lines += str(line)
    line = file.readline()
file.close()


print("Test File: \n" + '"' + file_lines + '"\n')

print("Numbers: " + str(a))
print("Letters: " + str(b))
print("Symbols: " + str(c))
print("Spaces: " + str(d))