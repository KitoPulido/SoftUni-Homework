import math

square_m_field = int(input())
grapes_for_q_m = float(input())
wine_needed = int(input())
workers = int(input())

# logic
all_grapes = square_m_field * grapes_for_q_m
grapes_for_wine = all_grapes * 0.4
wine_produced = (grapes_for_wine) / 2.5

# result
result = abs(wine_needed - wine_produced)

if wine_produced < wine_needed:
#    result = math.floor(wine_needed - wine_produced)
    print(f'It will be a tough winter! More {math.floor(result)} liters wine needed.')

elif wine_produced >= wine_needed:
#    result1 = math.ceil(wine_produced - wine_needed)
    wine_for_workers = math.ceil(result / workers)
#    wine_produced = math.floor(wine_produced)
    print(f'Good harvest this year! Total wine: {math.floor(wine_produced)} liters.')
    print(f'{math.ceil(result)} liters left -> {wine_for_workers} liters per person.')
