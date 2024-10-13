# user input data

fuel_type = str(input())
quantities = float(input())

# result

if fuel_type != 'Diesel' and fuel_type != 'Gasoline' and fuel_type != 'Gas':
    print('Invalid fuel!')

elif quantities >= 25:
    print(f'You have enough {fuel_type.lower()}.')

elif quantities < 25:
    print(f'Fill your tank with {fuel_type.lower()}!')