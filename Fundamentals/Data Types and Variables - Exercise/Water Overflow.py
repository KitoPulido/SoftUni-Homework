lines = int(input())

water_tank_capacity = 255
liters_in_tank = 0

for flow in range(lines):
    new_liters_of_water = int(input())
    if (water_tank_capacity - new_liters_of_water) < 0:
        print('Insufficient capacity!')
    else:
        water_tank_capacity -= new_liters_of_water
        liters_in_tank += new_liters_of_water

print(liters_in_tank)
