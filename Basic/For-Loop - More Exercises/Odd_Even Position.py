import sys

# user data input
num = int(input())
odd_sum = 0
even_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_min = sys.maxsize
even_max = -sys.maxsize

for position in range(1, num + 1):
    number = float(input())
    if position % 2 == 0:
        even_sum += number
        if number > even_max:
            even_max = number

        if number < even_min:
            even_min = number
    elif position % 2 != 0:
        odd_sum += number
        if number > odd_max:
            odd_max = number

        if number < odd_min:
            odd_min = number
    elif number == 0:
        continue
print(f'OddSum={odd_sum:.2f},')
if odd_min == sys.maxsize:
    print(f'OddMin=No,')
else:
    print(f'OddMin={odd_min:.2f},')
if odd_max == -sys.maxsize:
    print(f'OddMax=No,')
else:
    print(f'OddMax={odd_max:.2f},')

print(f'EvenSum={even_sum:.2f},')

if even_min == sys.maxsize:
    print(f'EvenMin=No,')
else:
    print(f'EvenMin={even_min:.2f},')
if even_max == -sys.maxsize:
    print(f'EvenMax=No')
else:
    print(f'EvenMax={even_max:.2f}')
