# user input data
import math

Magnolia = 3.25
Hyacinth = 4
Rose = 3.50
Cactus = 8

num_magnolia = int(input())
num_hyacinth = int(input())
num_rose = int(input())
num_cactus = int(input())
present_price = float(input())

# logic
flowers_order = (num_magnolia * 3.25) + (num_hyacinth * 4) + (num_rose * 3.50) + (num_cactus * 8)
flowers_tax = flowers_order * 0.05
flowers_cost = flowers_order - flowers_tax

# result
result = abs(present_price - flowers_cost)

if present_price <= flowers_cost:
    print(f'She is left with {math.floor(result)} leva.')

else:
    print(f'She will have to borrow {math.ceil(result)} leva.')