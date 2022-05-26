def make_test_file(filename: str):
    file = open(filename, "w")
    file.write("2, 4, 6, 8, \n")
    file.write("3, 5, 7, 9")
    file.close()


def get_numbers(filename: str) -> [int]:
    numbers = []
    file = open(filename, "r")
    line = file.readline()
    while line != "":
        for i in line.split(', '):
            if i.isdigit():
                numbers.append(int(i))
        line = file.readline()
    file.close()
    return numbers


def average_from_file(filename: str) -> float:
    make_test_file(filename)
    numbers = get_numbers(filename)
    return sum(numbers) / len(numbers)


global_file = open("test2.txt")
global_line = global_file.readline()
file_contents = ''
while global_line != "":
    file_contents += global_line
    global_line = global_file.readline()
global_file.close()

print("File contains: \n" + file_contents)

print("Average: " + str(average_from_file("test2.txt")))