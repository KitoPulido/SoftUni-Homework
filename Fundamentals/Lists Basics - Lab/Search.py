num = int(input())

word = input()
list = []
list_2 = []
for i in range(num):
    string = input()
    list.append(string)
print(list)
for i in range(len(list)):
    element = list[i]
    if word in element:
        list_2.append(element)

print(list_2)