f = open("C:\\Users\\Nouman\\Desktop\\test.txt", "rt")

str = f.readline()
str = str.split(",")
list = []
for i in str:
    list.append(int(i))

list.sort()
print(list)
age = int(input("Team Size: "))

low = 0
high = len(list) - 1;
result = []
while low < high:
    result.append([list[low], list[high]])
    high = high + 1
    low = low - 1

print(result)
