quantity = int(input())
days = int(input())

total_cost = 0
chr_spirit = 0

for shoping_days in range(1, days + 1):
    if shoping_days % 11 == 0:
        quantity += 2
    if shoping_days % 2 == 0:
        total_cost += 2 * quantity
        chr_spirit += 5
    if shoping_days % 3 == 0:
        total_cost += 8 * quantity
        chr_spirit += 13
    if shoping_days % 5 == 0:
        total_cost += 15 * quantity
        chr_spirit += 17
    if shoping_days % 3 == 0 and shoping_days % 5 == 0:
        chr_spirit += 30
    if shoping_days % 10 == 0:
        chr_spirit -= 20
        total_cost += 23

if days % 10 == 0:
    chr_spirit -= 30


print(f'Total cost: {total_cost}')
print(f'Total spirit: {chr_spirit}')

