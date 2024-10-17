budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
milk_price = (flour_price * 1.25) / 4

loaf_price = eggs_price + flour_price + milk_price

colored_eggs = 0
remaining_budget = budget
current_bread_count = 0
while loaf_price <= remaining_budget:
    current_bread_count += 1
    remaining_budget -= loaf_price
    colored_eggs += 3
    if current_bread_count % 3 == 0:
        colored_eggs -= (current_bread_count - 2)

print(f'You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {remaining_budget:.2f}BGN left.')
