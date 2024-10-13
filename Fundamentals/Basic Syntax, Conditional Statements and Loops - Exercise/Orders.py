num_of_orders = int(input())
total_price = 0

for order in range(0, num_of_orders):
    caps_price = float(input())
    days = int(input())
    caps_per_day = int(input())
    if 0.01 <= caps_price <= 100 and 1 <= days <= 31 and 1 <= caps_per_day <= 2000:
        coffee_price = (days * caps_per_day) * caps_price
        print(f'The price for the coffee is: ${coffee_price:.2f}')
    else:
        continue
    total_price += coffee_price

print(f'Total: ${total_price:.2f}')
