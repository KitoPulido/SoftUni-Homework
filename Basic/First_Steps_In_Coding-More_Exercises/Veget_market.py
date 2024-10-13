# user data input
price_veg = float(input())
price_fruit = float(input())
veg_kilos = float(input())
fruit_kilos = float(input())

# logic
veg = price_veg * veg_kilos
fruit = price_fruit * fruit_kilos
all_cost = (veg + fruit) / 1.94
# result

print(f'{all_cost:.2f}')

