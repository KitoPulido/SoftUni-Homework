num = int(input())

if num == 0 or num == 1:
    print('False')
elif num == 2 or num == 3 or num == 5 or num == 7 or num == 11:
    print('True')
elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0 or num % 11 == 0:
    print('False')
else:
    print('True')