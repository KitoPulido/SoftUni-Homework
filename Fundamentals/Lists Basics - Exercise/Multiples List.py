factor = int(input())
count = int(input())

multiples_list = []

for num in range(1, count +1):
    current_num = num * factor
    multiples_list.append(current_num)

print(multiples_list)
