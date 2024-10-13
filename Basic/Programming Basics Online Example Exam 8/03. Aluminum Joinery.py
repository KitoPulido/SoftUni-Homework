# user data input
orders = int(input())
types = input()
delivery = input()
price = 0
# logic
if types == '90X130':
    price = orders * 110
    if 30 < orders <= 60:
        price = price * 0.95
    elif orders > 60:
        price = price * 0.92
elif types == '100X150':
    price = orders * 140
    if 40 < orders <= 80:
        price = price * 0.94
    elif orders > 80:
        price = price * 0.90
elif types == '130X180':
    price = orders * 190
    if 20 < orders <= 50:
        price = price * 0.93
    elif orders > 50:
        price = price * 0.88
elif types == '200X300':
    price = orders * 250
    if 25 < orders <= 50:
        price = price * 0.91
    elif orders > 50:
        price = price * 0.86

if delivery == 'With delivery':
    price += 60

if orders > 99:
    price = price * 0.96
# result
if orders <= 10:
    print(f'Invalid order')
else:
    print(f'{price:.2f} BGN')