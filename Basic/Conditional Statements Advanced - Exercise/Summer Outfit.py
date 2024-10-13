# user data input
degrees_cel = int(input())
time_of_the_day = input()
outfit = ''
shoes = ''
# logic
if time_of_the_day == 'Morning':
    if 10 <= degrees_cel <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < degrees_cel <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degrees_cel >= 25:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
elif time_of_the_day == 'Afternoon':
    if 10 <= degrees_cel <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degrees_cel <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif degrees_cel >= 25:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
elif time_of_the_day == 'Evening':
    if 10 <= degrees_cel <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degrees_cel <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degrees_cel >= 25:
        outfit = 'Shirt'
        shoes = 'Moccasins'

# result
print(f'It\'s {degrees_cel} degrees, get your {outfit} and {shoes}.')