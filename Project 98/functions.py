#We didn't manage to find out how to open files in the lesson
def swapFileData ():
    file1 = input("Enter the first file you want to swap. ")
    file2 = input("Enter the second file you want to swap. ")
    with open(file1, 'r') as a:
        data_a = a.read()
    with open(file2, 'r') as a:
        data_b = a.read()
    with open(file1, 'w') as a:
        a.write(data_b)
    with open(file2, 'w') as a:
        a.write(data_a)

swapFileData()
