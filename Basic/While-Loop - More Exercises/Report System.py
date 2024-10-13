money = int(input())
cash_money = 0
cash_pays = 0
card_money = 0
card_pays = 0
money_needed = 0
all_pays = 1
while money_needed <= money:
    pay = input()
    if pay == 'End':
        print(f'Failed to collect required money for charity.')
        break
    else:
        pay = int(pay)
    if all_pays % 2 == 0:
        if pay < 10:
            print(f'Error in transaction!')
        else:
            card_money += pay
            card_pays += 1
            money_needed += pay
            print(f'Product sold!')
    else:
        if pay > 100:
            print(f'Error in transaction!')
        else:
            cash_money += pay
            cash_pays += 1
            money_needed += pay
            print(f'Product sold!')
    all_pays += 1

    if money_needed >= money:
        print(f'Average CS: {(cash_money / cash_pays):.2f}')
        print(f'Average CC: {(card_money / card_pays):.2f}')
        break

