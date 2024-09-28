# read first line of file
file = open("input.txt", "r")
print("Reading first line...")
print(file.readline())
file.close()



# read first three lines of file
file = open("input.txt", "r")
print("Reading first three lines...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()



file = open("input.txt", "r")
print("Looping through the lines...")
for line in file:
    print(line)
file.close()