pairs = int(input())
sum = 0
sum1 = 0

for _ in range(pairs):
    num1 = int(input())
    num2 = int(input())
    sum = num1 + num2

# for _ in range(pairs):
#    num1 = int(input())
#    num2 = int(input())
#    sum1 = num1 + num2

if sum == sum1:
    print(f'Yes, value={sum}')
else:
    result = sum - sum1
    print(f'No, maxdiff={result}')
