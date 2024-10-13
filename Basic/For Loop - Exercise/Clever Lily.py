# user data input
lily_age = int(input())
washer_price = float(input())
toy_price = int(input())
sum = 0
money_for_presant = 10
increase = 10
# logic
for num in range(1, lily_age + 1):
    if num % 2 == 0:
        sum = (sum + money_for_presant) - 1
        money_for_presant += increase
    else:
        sum += toy_price

result = abs(sum - washer_price)
# result
if sum >= washer_price:
    print(f'Yes! {result:.2f}')
else:
    print(f'No! {result:.2f}')
