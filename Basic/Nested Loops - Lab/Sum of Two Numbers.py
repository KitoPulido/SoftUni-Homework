start_number = int(input())
last_number = int(input())
magic_number = int(input())
combination = 0
faund = False
for i in range(start_number, last_number + 1):
    for j in range(start_number, last_number + 1):
        combination += 1
        if i + j == magic_number:
            print(f'Combination N:{combination} ({i} + {j} = {magic_number})')
            faund = True
            break
    if faund:
        break
if faund != True:
    print(f'{combination} combinations - neither equals {magic_number}')
