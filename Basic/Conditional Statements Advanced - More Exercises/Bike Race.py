# user data input
juniors = int(input())
seniors = int(input())
trace = input()
price = 0

# logic
all_people = juniors + seniors
if trace == 'trail':
    price = (juniors * 5.50) + (seniors * 7)
elif trace == 'cross-country':
    price = (juniors * 8) + (seniors * 9.50)
    if all_people >= 50:
        price = price * 0.75
elif trace == 'downhill':
    price = (juniors * 12.25) + (seniors * 13.75)
else:
    price = (juniors * 20) + (seniors * 21.50)

tax = price * 0.95

# result
print(f'{tax:.2f}')