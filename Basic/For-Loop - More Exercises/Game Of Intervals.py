# user data input
moves = int(input())
resulr = 0
from_0_9 = 0
from_10_19 = 0
from_20_29 = 0
from_30_39 = 0
from_40_50 = 0
invalid_num = 0
# logic
for game in range(moves):
    points = int(input())
    if 0 <= points <= 9:
        resulr += (points * 0.2)
        from_0_9 += 1
    elif 10 <= points <= 19:
        resulr += (points * 0.3)
        from_10_19 += 1
    elif 20 <= points <= 29:
        resulr += (points * 0.4)
        from_20_29 += 1
    elif 30 <= points <= 39:
        resulr += 50
        from_30_39 += 1
    elif 40 <= points <= 50:
        resulr += 100
        from_40_50 += 1
    else:
        invalid_num += 1
        resulr = resulr / 2

# result
print(f'{resulr:.2f}')
print(f'From 0 to 9: {((from_0_9 / moves) * 100):.2f}%')
print(f'From 10 to 19: {((from_10_19 / moves) * 100):.2f}%')
print(f'From 20 to 29: {((from_20_29 / moves) * 100):.2f}%')
print(f'From 30 to 39: {((from_30_39 / moves) * 100):.2f}%')
print(f'From 40 to 50: {((from_40_50 / moves) * 100):.2f}%')
print(f'Invalid numbers: {((invalid_num / moves) * 100):.2f}%')
