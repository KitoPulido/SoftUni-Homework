# user data input
shirt_price = float(input())
sum_for_ball = float(input())

# logic
shorts_price = shirt_price * 0.75
socs_price = shorts_price * 0.2
shoose_price = (shirt_price + shorts_price) * 2
sum = shirt_price + shorts_price + socs_price + shoose_price
final_price = sum - (sum * 0.15)

# result
if final_price >= sum_for_ball:
    print(f'Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {final_price:.2f} lv.')
else:
    print(f'No, he will not earn the world-cup replica ball.')
    print(f'He needs {sum_for_ball - final_price:.2f} lv. more.')
