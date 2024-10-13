# user data input
people = int(input())
season = input()
sum_of_excursion = 0
# logic
if season == 'spring':
    if people <= 5:
        sum_of_excursion += people * 50
    else:
        sum_of_excursion += people * 48
elif season == 'autumn':
    if people <= 5:
        sum_of_excursion += people * 60
    else:
        sum_of_excursion += people * 49.50
elif season == 'summer':
    if people <= 5:
        sum_of_excursion += people * 48.50
        sum_of_excursion = sum_of_excursion * 0.85
    else:
        sum_of_excursion += people * 45
        sum_of_excursion = sum_of_excursion * 0.85
elif season == 'winter':
    if people <= 5:
        sum_of_excursion += people * 86
        sum_of_excursion = sum_of_excursion * 1.08
    else:
        sum_of_excursion += people * 85
        sum_of_excursion = sum_of_excursion * 1.08

# result
print(f'{sum_of_excursion:.2f} leva.')
