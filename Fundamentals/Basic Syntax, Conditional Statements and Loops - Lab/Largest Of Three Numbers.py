num1 = int(input())
num2 = int(input())
num3 = int(input())

greater_num = 0

if num1 > num2:
    greater_num = num1
else:
    greater_num = num2
if greater_num > num3:
    print(greater_num)
else: print(num3)