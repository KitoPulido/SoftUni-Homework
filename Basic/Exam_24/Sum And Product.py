# user data input
n = int(input())
number_found = False
magic_number = 0
# logic

for a in range(1, 10):
    if number_found:
        break
    for b in range(9, a - 1, -1):
        if number_found:
            break
        for c in range(0, 10):
            if number_found:
                break
            for d in range(9, c -1, -1):
                sum = a + b + c + d
                multiply = a * b * c * d
                if sum == multiply and n % 10 == 5:
                    print(f'{a}{b}{c}{d}')
                    number_found = True
                    magic_number = 1
                    break
                if multiply // sum == 3 and n % 3 == 0:
                    print(f'{d}{c}{b}{a}')
                    number_found = True
                    magic_number = 1
                    break

# result
if magic_number == 0: #(sum == multiply and n % 10 == 5) and (multiply // sum == 3 and n % 3 == 0):
    print(f'Nothing found')

