# user data input
import math

days = int(input())
food_left = int(input())
dog_food_kl_needed_per_day = float(input())
cat_food_kl_needed_per_day = float(input())
turtle_food_gr_needed_per_day = float(input()) / 1000

# logic
food_needed = (dog_food_kl_needed_per_day + cat_food_kl_needed_per_day + turtle_food_gr_needed_per_day ) * days

# result
result = abs(food_left - food_needed)

if food_left >= food_needed:
    print(f'{math.floor(result)} kilos of food left.')
else:
    print(f'{math.ceil(result)} more kilos of food are needed.')
