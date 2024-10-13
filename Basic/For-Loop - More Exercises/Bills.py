# user data input
months = int(input())
electricity = 0
water = 0
internet = 0
other = 0

# logic
for bills in range(months):
    elect_bill = float(input())
    electricity += elect_bill
    water += 20
    internet += 15
    other += ((elect_bill + 20 + 15) * 1.2)

all_cost = electricity + water + internet + other
average = all_cost / months
# result
print(f'Electricity: {electricity:.2f} lv')
print(f'Water: {water:.2f} lv')
print(f'Internet: {internet:.2f} lv')
print(f'Other: {other:.2f} lv')
print(f'Average: {average:.2f} lv')
