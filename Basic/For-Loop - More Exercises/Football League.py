# user data input
stadium_capacity = int(input())
fans = int(input())
sec_a = 0
sec_b = 0
sec_v = 0
sec_g = 0
# logic
for game in range(fans):
    fan_spot = input()
    if fan_spot == 'A':
        sec_a += 1
    elif fan_spot == 'B':
        sec_b += 1
    elif fan_spot == 'V':
        sec_v += 1
    elif fan_spot == 'G':
        sec_g += 1

# result
print(f'{((sec_a / fans) * 100):.2f}%')
print(f'{((sec_b / fans) * 100):.2f}%')
print(f'{((sec_v / fans) * 100):.2f}%')
print(f'{((sec_g / fans) * 100):.2f}%')
print(f'{((fans / stadium_capacity) * 100):.2f}%')
