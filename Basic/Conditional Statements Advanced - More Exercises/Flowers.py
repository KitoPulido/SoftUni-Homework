# user data input
chrysanthemum = int(input())
rose = int(input())
tulip = int(input())
season = input()
holiday = input()
bouquet = 0
chrysanthemum_price = 0
rose_price = 0
tulip_price = 0
# logic
if season == 'Spring' or season == 'Summer':
    chrysanthemum_price = chrysanthemum * 2.00
    rose_price = rose * 4.10
    tulip_price = tulip * 2.50
elif season == 'Autumn' or season == 'Winter':
    chrysanthemum_price = chrysanthemum * 3.75
    rose_price = rose * 4.50
    tulip_price = tulip * 4.15

bouquet = chrysanthemum_price + rose_price + tulip_price

if holiday == 'Y':
    bouquet *= 1.15

if tulip > 7 and season == 'Spring':
    bouquet *= 0.95

if rose >= 10 and season == 'Winter':
    bouquet *= 0.90

all_flowers = chrysanthemum + rose + tulip
if all_flowers > 20:
    bouquet *= 0.80

# result
print(f'{bouquet + 2:.2f}')
