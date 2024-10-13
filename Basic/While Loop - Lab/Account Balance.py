balance = 0

while True:
    sum = input()
    if sum == 'NoMoreMoney':
        break
    sum = float(sum)
    if sum < 0:
        print(f'Invalid operation!')
        break
    else:
        balance += sum
        print(f'Increase: {sum:.2f}')
        continue
print(f'Total: {balance:.2f}')
