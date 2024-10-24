import math

group = int(input())
days = int(input())

coins_gained = 0

for party_day in range(1, days + 1):
    if party_day % 10 == 0:
        group -= 2
    if party_day % 15 == 0:
        group += 5
    coins_gained += 50 - (group * 2)

    if party_day % 3 == 0:
        coins_gained -= group * 3
    if party_day % 5 == 0:
        coins_gained += 20 * group
        if party_day % 3 == 0:
            coins_gained -= group * 2

coins_per_companion = math.floor(coins_gained / group)
print(f'{group} companions received {coins_per_companion} coins each.')
