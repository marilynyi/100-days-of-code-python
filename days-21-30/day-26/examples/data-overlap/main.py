

with open("file1.txt") as file1:
    data1 = file1.readlines()
    data1 = [int(data.strip()) for data in data1]

with open("file2.txt") as file2:
    data2 = file2.readlines()
    data2 = [int(data.strip()) for data in data2]

result = [data for data in data1 if data in data2]

print(result)