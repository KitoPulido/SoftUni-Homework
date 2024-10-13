num = int(input())
odd_sum = 0
even_sum = 0

for i in range(num):
    element = int(input())
    if i % 2 == 0:
        even_sum += element
    else:
        odd_sum += element

if even_sum == odd_sum:
    print('Yes')
    print(f'Sum = {even_sum}')

else:
    result = abs(even_sum - odd_sum)
    print('No')
    print(f'Diff = {result}')