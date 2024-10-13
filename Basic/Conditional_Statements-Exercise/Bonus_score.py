# user input data
num = float(input())
bonus_point = 0

#logic

if num <= 100:
    bonus_point = 5
elif num > 100 and num <= 1000:
    bonus_point = num * 0.2
elif num > 1000:
    bonus_point = num * 0.1
if num % 2 == 0:
    bonus_point = bonus_point + 1
elif num % 10 == 5:
    bonus_point = bonus_point + 2

# result

print(bonus_point)
print(num + bonus_point)