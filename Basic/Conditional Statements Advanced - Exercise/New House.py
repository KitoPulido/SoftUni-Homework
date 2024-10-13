# user data input
flowers = input()
qty = int(input())
budget = int(input())
total_price = 0
# logic
if flowers == 'Roses':
    total_price = qty * 5
    if qty > 80:
        total_price = total_price - (total_price * 0.1)
elif flowers == 'Dahlias':
    total_price = qty * 3.80
    if qty > 90:
        total_price = total_price - (total_price * 0.15)
elif flowers == 'Tulips':
    total_price = qty * 2.80
    if qty > 80:
        total_price = total_price - (total_price * 0.15)
elif flowers == 'Narcissus':
    total_price = qty * 3
    if qty < 120:
        total_price = total_price * 1.15
elif flowers == 'Gladiolus':
    total_price = qty * 2.50
    if qty < 80:
        total_price = total_price * 1.2

result = abs(budget - total_price)
# result
if budget >= total_price:
    print(f'Hey, you have a great garden with {qty} {flowers} and {result:.2f} leva left.')
else:
    print(f'Not enough money, you need {result:.2f} leva more.')

