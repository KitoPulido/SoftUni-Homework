# user data input
fruit = input()
day_of_week = input()
qty = float(input())
price = None
# logic
if day_of_week == 'Saturday' or day_of_week == 'Sunday':
    if fruit == 'banana':
        price = qty * 2.70
    elif fruit == 'apple':
        price = qty * 1.25
    elif fruit == 'orange':
        price = qty * 0.9
    elif fruit == 'grapefruit':
        price = qty * 1.6
    elif fruit == 'kiwi':
        price = qty * 3.00
    elif fruit == 'pineapple':
        price = qty * 5.60
    elif fruit == 'grapes':
        price = qty * 4.20
    else:
        price = 'error'
        print(price)
elif day_of_week == 'Monday' or day_of_week == 'Tuesday' \
    or day_of_week == 'Wednesday' or day_of_week == 'Thursday' \
    or day_of_week == 'Friday':
    if fruit == 'banana':
        price = qty * 2.50
    elif fruit == 'apple':
        price = qty * 1.20
    elif fruit == 'orange':
        price = qty * 0.85
    elif fruit == 'grapefruit':
        price = qty * 1.45
    elif fruit == 'kiwi':
        price = qty * 2.70
    elif fruit == 'pineapple':
        price = qty * 5.50
    elif fruit == 'grapes':
        price = qty * 3.85
    else:
        price = 'error'
        print(price)
else:
    price = 'error'
    print(price)
# result
if price != 'error':
    print(f'{price:.2f}')