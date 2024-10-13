# user data input
bags_20_up = float(input())
bags_kilos = float(input())
day_to_go = int(input())
bags = int(input())
price = 0
# logic
if bags_kilos < 10:
    price += (bags_20_up * 0.2) * bags
elif 10 <= bags_kilos <= 20:
    price += (bags_20_up * 0.5) * bags
else:
    price += bags_20_up * bags

if day_to_go > 30:
    price = (price * 1.1)
elif 7 <= day_to_go <= 30:
    price = (price * 1.15)
else:
    price = (price * 1.4)
# result
print(f' The total price of bags is: {price:.2f} lv.')
