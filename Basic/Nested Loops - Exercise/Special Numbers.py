num = int(input())

magic_number = False

while True:
    if magic_number:
        break
    count = 0
    for number in range(1111, 9999 + 1):
        number = str(number)
        for index, digit in enumerate(number):
            digit = int(digit)
            if digit == 0:
                continue
            if num % digit == 0:
                count += 1
                if count == 4:
                    print(f'{number}', end=' ')
        count = 0
    number = int(number)
    if number >= 9999:
        magic_number = True
