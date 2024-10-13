# user data input
Puzzel_price = 2.6
Doll_price = 3
Teddy_bear_price = 4.10
Minions_price = 8.2
Truck_price = 2

vacation_price = float(input())
puzzels = int(input())
dolls = int(input())
teddy_bear = int(input())
minions = int(input())
trucks = int(input())

# logic
order_price = (puzzels * 2.6) + \
              (dolls * 3) + \
              (teddy_bear * 4.1) + \
              (minions * 8.2) + \
              (trucks * 2)
number_of_toys = puzzels + dolls + teddy_bear + minions + trucks
if number_of_toys >= 50:
    order_price = order_price - (order_price * 0.25)

profit_after_rent = order_price - (order_price * 0.1)
result1 = profit_after_rent - vacation_price
result2 = vacation_price - profit_after_rent

# result

if vacation_price <= profit_after_rent:
    print(f'Yes! {result1:.2f} lv left.')
elif vacation_price > profit_after_rent:
    print(f'Not enough money! {result2:.2f} lv needed.')
