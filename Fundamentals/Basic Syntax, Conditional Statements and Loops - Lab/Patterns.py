pattern_num = int(input())

for num in range(1,pattern_num + 1):
    for t in range(0,num):
        print('*', end='')
    print()

for j in range(pattern_num -1, 0, -1):
    for d in range(0,j):
        print('*', end='')
    print()