# user data input
month = input()
nigths = int(input())
apartment_price = 0
studio_price = 0

# logic
if month == 'May' or month == 'October':
    apartment_price = nigths * 65
    studio_price = nigths * 50
    if nigths > 14:
        studio_price = studio_price - (studio_price * 0.3)
        apartment_price = apartment_price - (apartment_price * 0.1)
    elif nigths > 7:
        studio_price = studio_price - (studio_price * 0.05)

elif month == 'June' or month == 'September':
    apartment_price = nigths * 68.70
    studio_price = nigths * 75.20
    if nigths > 14:
        studio_price = studio_price - (studio_price * 0.2)
        apartment_price = apartment_price - (apartment_price * 0.1)
elif month == 'July' or month == 'August':
    apartment_price = nigths * 77
    studio_price = nigths * 76
    if nigths > 14:
        apartment_price = apartment_price - (apartment_price * 0.1)

# result
print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')
