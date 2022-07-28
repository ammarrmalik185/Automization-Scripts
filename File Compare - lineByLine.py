file_name_1 = input ("Enter File 1 :")
file_name_2 = input ("Enter File 2 :")

path = "autoTyperData\\"

file1 = open(path + file_name_1 + ".txt")
file2 = open(path + file_name_2 + ".txt")

lines1 = file1.readlines()
lines2 = file2.readlines()

print(lines1)
print(lines2)


for line in lines1:
    if line not in lines2:
        print("not in file 2 :" + line)

for line in lines2:
    if line not in lines1:
        print("not in file 1 :" + line)

input ("done")
