# user data input
days = int(input())
room_type = input()
rating = input()
price = 0
# logic
nigths = days - 1
if room_type == 'room for one person':
    price = nigths * 18
elif room_type == 'apartment':
    price = nigths * 25
    if days < 10:
        price = price - (price * 0.3)
    elif 10 <= days <= 15:
        price = price - (price * 0.35)
    elif days > 15:
        price = price - (price * 0.5)
elif room_type == 'president apartment':
    price = nigths * 35
    if days < 10:
        price = price - (price * 0.1)
    elif 10 <= days <= 15:
        price = price - (price * 0.15)
    elif days > 15:
        price = price - (price * 0.2)

if rating == 'positive':
    price = price * 1.25
elif rating == 'negative':
    price = price - (price * 0.1)

# result
print(f'{price:.2f}')
