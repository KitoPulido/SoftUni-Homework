num = input().split(', ')
beggars = int(input())
money_in_num = []
money_get = []

for money in num:
    money_in_num.append(int(money))
index = 0
for beggar in range(beggars):
    current_beggar_sum = 0
    for current_index in range(index, len(money_in_num), beggars):
        current_beggar_sum += money_in_num[current_index]
    money_get.append(current_beggar_sum)
    index +=1
print(money_get)