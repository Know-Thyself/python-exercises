with open('file1.txt', 'r') as file:
    list1 = file.readlines()

with open('file2.txt', 'r') as file:
    list2 = file.readlines()


result = [int(n) for n in list1 if n in list2]
#
print(result)
