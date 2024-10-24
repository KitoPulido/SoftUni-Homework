num_1 = int(input())
num_2 = int(input())
list = []
for char in range(num_1, num_2+1):
    #char = chr(char)
    list.append(chr(char))

for element in list:
    print(element, end=' ')