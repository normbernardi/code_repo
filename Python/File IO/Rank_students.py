def read_data(textfile: str) -> str:
    data_dict = dict()
    with open(textfile,  'r') as file:
        for line in file.readlines():
            name, grade = line.strip('\n').split(', ')
            data_dict[grade] = data_dict.get(grade, []) + [name]
    return data_dict

def student_grades(textfile: str) -> str:
    output = ''
    ranks = 1
    data = read_data(textfile)
    for mark, names in sorted(data.items(), reverse=True):
        for name in names:
            output += f"{ranks:4} {name} {mark}\n"
        ranks += len(names)
    return output


print(student_grades("StudentData.txt"))

