# user data input
sea_num = int(input())
mountain_num = int(input())
sum_of_all = 0
sea_count = 0
mountain_count = 0
type_of_excursion = input()
# logic
while type_of_excursion != 'Stop':

    if type_of_excursion == 'sea':
        if sea_count >= sea_num:
            sum_of_all += 0
        else:
            sum_of_all += 680
            sea_count += 1
    elif type_of_excursion == 'mountain':
        if mountain_count >= mountain_num:
            sum_of_all += 0
        else:
            sum_of_all += 499
            mountain_count += 1
    if sea_count >= sea_num and mountain_count >= mountain_num:
        break

    type_of_excursion = input()
# result
if sea_count >= sea_num and mountain_count >= mountain_num:
    print(f'Good job! Everything is sold.')
print(f'Profit: {sum_of_all} leva.')
