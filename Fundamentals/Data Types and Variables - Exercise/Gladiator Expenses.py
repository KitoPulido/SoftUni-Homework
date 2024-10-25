lost_fights = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

shield_broken = 0
gladiator_expenses = 0
for fights in range(1, lost_fights + 1):
    if fights % 2 == 0:
        gladiator_expenses += helmet_price
    if fights % 3 == 0:
        gladiator_expenses += sword_price
    if fights % 2 == 0 and fights % 3 == 0:
        gladiator_expenses += shield_price
        shield_broken += 1
        if shield_broken % 2 == 0:
            gladiator_expenses += armor_price

print(f'Gladiator expenses: {gladiator_expenses:.2f} aureus')