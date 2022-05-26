def read_file(fname: str):
    file = open(fname, "r")
    for line in file:
        line = file.readline()
        if line=="":
            break
        print(line)
    file.close()

def write_file(fname: str):
    file = open(fname, "a")
    exit = False
    while not exit:
        file.write(input("Enter text to be written: ") + "\n")
        if input("Write another line? Y/N ").upper()=='N':
            exit=True
    file.close()
    print("Done")

def file_io():#driver
    print("---Simple File IO---")
    close = False
    while not close:
        filename=input("Enter name of file: ")
        operation = input("(R)ead or (W)rite? ").upper()
        if operation=="W":
            print("Writing " + filename + ":")
            write_file(filename)
        elif operation=="R":
            print("Reading " + filename + ":")
            read_file(filename)
        else:
            print("Invalid Choice!")
        if input("Continue? Y/N ").upper()=="N":
            close=True

file_io()

