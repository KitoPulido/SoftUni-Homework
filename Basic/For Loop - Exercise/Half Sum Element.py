import sys

max_num = -sys.maxsize
sum_numbers = 0
n = int(input())

for i in range(0, n):
    num = int(input())
    if num > max_num:
        max_num = num

    sum_numbers +=num

number = sum_numbers - max_num

if max_num == number:
    print('Yes')
    print(f'Sum = {number}')
else:
    print('No')
    print(f'Diff = {abs(max_num - number)}')