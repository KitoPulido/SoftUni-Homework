# user data input
season = input()
klm_a_month = float(input())
salary = 0

# logic
if season == 'Spring' or season == 'Autumn':
    if klm_a_month <= 5000:
        salary = klm_a_month * 0.75
    elif 5000 < klm_a_month <= 10000:
        salary = klm_a_month * 0.95
    else:
        salary = klm_a_month * 1.45
elif season == 'Summer':
    if klm_a_month <= 5000:
        salary = klm_a_month * 0.90
    elif 5000 < klm_a_month <= 10000:
        salary = klm_a_month * 1.10
    else:
        salary = klm_a_month * 1.45
elif season == 'Winter':
    if klm_a_month <= 5000:
        salary = klm_a_month * 1.05
    elif 5000 < klm_a_month <= 10000:
        salary = klm_a_month * 1.25
    else:
        salary = klm_a_month * 1.45

afther_tax = (salary * 4) * 0.90
# result sf
print(f'{afther_tax:.2f}')
