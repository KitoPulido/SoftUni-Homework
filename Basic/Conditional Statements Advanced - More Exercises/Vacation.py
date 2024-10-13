# user data input
budget = float(input())
season = input()
location = ''
place_to_stay = ''
price = 0
# logic
if budget <= 1000:
    place_to_stay = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.65
    else:
        location = 'Morocco'
        price = budget * 0.45

elif 1000 < budget <= 3000:
    place_to_stay = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.80
    else:
        location = 'Morocco'
        price = budget * 0.60

if budget > 3000:
    place_to_stay = 'Hotel'
    price = budget * 0.90
    if season == 'Summer':
        location = 'Alaska'
    else:
        location = 'Morocco'

# result
print(f'{location} - {place_to_stay} - {price:.2f}')
