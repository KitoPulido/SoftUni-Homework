# user data input
budget = float(input())
season = input()
destination = ''
place = ''
price = 0
# logic
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        price = budget * 0.3
        place = 'Camp'
    elif season == 'winter':
        price = budget * 0.7
        place = 'Hotel'
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        price = budget * 0.4
        place = 'Camp'
    elif season == 'winter':
        price = budget * 0.8
        place = 'Hotel'
elif budget > 1000:
    destination = 'Europe'
    price = budget * 0.9
    place = 'Hotel'

# result
print(f'Somewhere in {destination}')
print(f'{place} - {price:.2f}')