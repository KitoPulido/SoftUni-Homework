n = int(input())
left_sum = 0
right_sum = 0

for i in range(n):
    r_num = int(input())
    left_sum += r_num

for i in range(n):
    l_num = int(input())
    right_sum += l_num


if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    result = abs(left_sum - right_sum)
    print(f'No, diff = {result}')
