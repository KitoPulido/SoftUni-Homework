# user data input
num1 = int(input())
num2 = int(input())
operator = input()
result = 0
even_odd = ''
left = 0
# logic
if operator == '+':
    result = num1 + num2
    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
    print(f'{num1} {operator} {num2} = {result} - {even_odd}')
elif operator == '-':
    result = num1 - num2
    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
    print(f'{num1} {operator} {num2} = {result} - {even_odd}')
elif operator == '*':
    result = num1 * num2
    if result % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
    print(f'{num1} {operator} {num2} = {result} - {even_odd}')
elif operator == '/':
    if num2 == 0:
        print(f'Cannot divide {num1} by zero')
    else:
        result = num1 / num2
        print(f'{num1} / {num2} = {result:.2f}')
elif operator == '%':
    if num2 == 0:
        print(f'Cannot divide {num1} by zero')
    else:
        left = num1 % num2
        print(f'{num1} % {num2} = {left}')


# result