# user data input
n = int(input())
salary = int(input())

# logic
for tabs in range(n):
    tabs = input()
    if tabs == 'Facebook':
        salary -= 150
        if salary <= 0:
            print(f'You have lost your salary.')
            break
    elif tabs == 'Instagram':
        salary -= 100
        if salary <= 0:
            print(f'You have lost your salary.')
            break
    elif tabs == 'Reddit':
        salary -= 50
        if salary <= 0:
            print(f'You have lost your salary.')
            break

if salary > 0:
    print(int(salary))

# result
