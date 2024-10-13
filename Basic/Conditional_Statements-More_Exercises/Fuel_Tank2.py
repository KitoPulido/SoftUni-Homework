Gasoline = 2.22
Diesel = 2.33
Gas = 0.93

# user data input

fuel_type = input()
quantities = float(input())
club_card = input()

# logic
result = 0

#result

if fuel_type == 'Gas' and club_card == 'Yes':
    result = quantities * (0.93 - 0.08)
elif fuel_type == 'Gas' and club_card == 'No':
    result = quantities * 0.93

elif fuel_type == 'Gasoline' and club_card == 'Yes':
    result = quantities * (2.22 - 0.18)
elif fuel_type == 'Gasoline' and club_card == 'No':
    result = quantities * 2.22

elif fuel_type == 'Diesel' and club_card == 'Yes':
    result = quantities * (2.33 - 0.12)
elif fuel_type == 'Diesel' and club_card == 'No':
    result = quantities * 2.33

if quantities > 25:
    result = result - (result * 0.1)
elif quantities >= 20 and quantities <= 25:
    result = result - (result * 0.08)

print(f'{result:.2f} lv.')