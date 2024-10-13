money_needed = float(input())
real_money = float(input())
saved_money = real_money
days = 0
cant_save = 0

while saved_money < money_needed:
    action = input()
    sum1 = float(input())
    if action == 'spend':
        saved_money -= sum1
        if saved_money < 0:
            saved_money = 0
    elif action == 'save':
        saved_money += sum1
    days += 1
    if action == 'spend':
        cant_save += 1
        if cant_save == 5:
            print(f"You can't save the money.")
            print(f'{days}')
            break
    else:
        cant_save = 0
    if saved_money >= money_needed:
        print(f'You saved the money for {days} days.')
        break