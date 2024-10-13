# user data input
season = input()
group = input()
student = int(input())
nights = int(input())
sport = ''
price = 0

# logic
if season == 'Winter':
    if group == 'boys':
        price = nights * student * 9.60
        sport = 'Judo'
    elif group == 'girls':
        price = nights * 9.60 * student
        sport = 'Gymnastics'
    elif group == 'mixed':
        price = nights * 10 * student
        sport = 'Ski'
elif season == 'Spring':
    if group == 'boys':
        price = nights * 7.20 * student
        sport = 'Tennis'
    elif group == 'girls':
        price = nights * 7.20 * student
        sport = 'Athletics'
    elif group == 'mixed':
        price = nights * 9.50 *student
        sport = 'Cycling'
elif season == 'Summer':
    if group == 'boys':
        price = nights * 15 * student
        sport = 'Football'
    elif group == 'girls':
        price = nights * 15 * student
        sport = 'Volleyball'
    elif group == 'mixed':
        price = nights * 20 * student
        sport = 'Swimming'

if student >= 50:
    price *= 0.5
elif 20 <= student < 50:
    price *= 0.85
elif 10 <= student <20:
    price *= 0.95

# result
print(f'{sport} {price:.2f} lv.')
