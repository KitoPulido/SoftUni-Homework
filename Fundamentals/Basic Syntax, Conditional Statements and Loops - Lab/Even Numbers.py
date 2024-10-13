all_num = int(input())

for num in range(all_num):
    num = int(input())
    if not num % 2 == 0:
        print(F"{num} is odd!")
        break
else:
    print('All numbers are even.')
