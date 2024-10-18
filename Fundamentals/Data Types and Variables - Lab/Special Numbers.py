num = int(input())
first_num = 0
second_num = 0

for number in range(1, num +1):
    first_num = number % 10
    second_num = number // 10
    magic_number = first_num + second_num
    if magic_number == 5 or magic_number == 7 or magic_number == 11:
        print(f'{number} -> True')
    else:
        print(f'{number} -> False')




