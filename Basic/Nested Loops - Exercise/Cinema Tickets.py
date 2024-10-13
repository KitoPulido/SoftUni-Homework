all_student = 0
all_standart = 0
all_kid = 0
film_seats = 0
all_seats = 0
if_flag = False
while True:
    if if_flag:
        break
    film = input()
    if film == 'Finish':
        break

    seats = int(input())
    for tickets in range(seats):
        ticket = input()
        if ticket == 'End':
            break
        if ticket == 'Finish':
            if_flag = True
            break
        if ticket == 'standard':
            all_standart += 1
            film_seats += 1
            all_seats += 1
        elif ticket == 'student':
            all_student += 1
            film_seats += 1
            all_seats += 1
        elif ticket == 'kid':
            all_kid += 1
            film_seats += 1
            all_seats += 1
        if film_seats > seats:
            break

    print(f'{film} - {(film_seats / seats) * 100:.2f}% full.')
    film_seats = 0

print(f'Total tickets: {all_seats}')
print(f'{(all_student / all_seats) * 100:.2f}% student tickets.')
print(f'{(all_standart / all_seats) * 100:.2f}% standard tickets.')
print(f'{(all_kid / all_seats) * 100:.2f}% kids tickets.')
