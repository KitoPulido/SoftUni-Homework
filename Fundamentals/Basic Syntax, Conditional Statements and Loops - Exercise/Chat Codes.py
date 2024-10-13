num = int(input())

for n in range(1, num +1):
    current_number = int(input())
    if current_number == 88:
        print('Hello')
    if current_number == 86:
        print('How are you?')
    if current_number != 88 and current_number != 86 and current_number < 88:
        print('GREAT!')
    if current_number > 88:
        print('Bye.')

