# user data input
budget = int(input())
season = input()
fishermens = int(input())
price = 0
# logic
if season == 'Spring':
    price = 3000
    if fishermens <= 6:
        price = price - (price * 0.1)
    elif 7 <= fishermens <= 11:
        price = price - (price * 0.15)
    elif fishermens >= 12:
        price = price - (price * 0.25)
elif season == 'Summer' or season == 'Autumn':
    price = 4200
    if fishermens <= 6:
        price = price - (price * 0.1)
    elif 7 <= fishermens <= 11:
        price = price - (price * 0.15)
    elif fishermens >= 12:
        price = price - (price * 0.25)
elif season == 'Winter':
    price = 2600
    if fishermens <= 6:
        price = price - (price * 0.1)
    elif 7 <= fishermens <= 11:
        price = price - (price * 0.15)
    elif fishermens >= 12:
        price = price - (price * 0.25)

if season == 'Spring' or season == 'Summer' or season == 'Winter':
    if fishermens % 2 == 0:
        price = price - (price * 0.05)

result = abs(budget - price)
# result
if budget >= price:
    print(f'Yes! You have {result:.2f} leva left.')
else:
    print(f'Not enough money! You need {result:.2f} leva.')


