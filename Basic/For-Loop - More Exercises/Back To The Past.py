# user data input
money = float(input())
year_to_live = int(input())
# years_left = (years_of_life - 18) + 1800
money_left = money
years_old = 18

# logic
for money_need in range(1800, year_to_live + 1):
    if money_need % 2 == 0:
        money_left -= 12000
        years_old += 1
    else:
        money_left -= (12000 + years_old * 50)
        years_old += 1
# output
if money_left >= 0:
   print(f'Yes! He will live a carefree life and will have {money_left:.2f} dollars left.')
else:
   print(f'He will need {abs(money_left):.2f} dollars to survive.')
