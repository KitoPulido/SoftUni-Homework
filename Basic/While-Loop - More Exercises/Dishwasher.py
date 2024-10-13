num_of_detergent = int(input())
detergent = num_of_detergent * 750
Dish = 5
Pot = 15
num = 1
dishes = 0
pots = 0
while detergent >= 0:
    count = input()
    if count == 'End':
        break
    else:
        count = int(count)
        if num % 3 == 0:
            detergent -= (Pot * count)
            pots += count
        else:
            detergent -= (Dish * count)
            dishes += count

    num += 1
if detergent >= 0:
    print(f'Detergent was enough!')
    print(f'{dishes} dishes and {pots} pots were washed.')
    print(f'Leftover detergent {detergent} ml.')
if detergent < 0:
    print(f'Not enough detergent, {abs(detergent)} ml. more necessary!')