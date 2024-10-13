# user input data

budget = float(input())
num_graphic_card = int(input())
num_cpu = int(input())
num_ram = int(input())

# logic
graphic_card_cost = num_graphic_card * 250
cpu_cost = (graphic_card_cost * 0.35) * num_cpu
ram_cost = (graphic_card_cost * 0.1) * num_ram
all_materials = graphic_card_cost + cpu_cost + ram_cost
if num_graphic_card > num_cpu:
    all_materials = all_materials - (all_materials * 0.15)
result = budget - all_materials
result1 = all_materials - budget

# result
if all_materials <= budget:
    print(f'You have {result:.2f} leva left!')

elif all_materials > budget:
    print(f'Not enough money! You need {result1:.2f} leva more!')