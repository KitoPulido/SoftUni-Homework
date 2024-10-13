# user input data
mackerel_price = float(input())
sprinkle_price = float(input())
palamud_kilo = float(input()) * (mackerel_price * 1.6)
safrid_kilo = float(input()) * (sprinkle_price * 1.8)
mussels_kilo = int(input()) * 7.5
# logic
bill = palamud_kilo + safrid_kilo + mussels_kilo

# result
print(f'{bill:.2f}')