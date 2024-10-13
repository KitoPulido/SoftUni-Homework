# user data input
num_of_cargos = int(input())
microbus_cargos = 0
truck_cargos = 0
train_cargos = 0
total_price = 0

# logic
for cargo in range(num_of_cargos):
    weighs = int(input())
    if weighs <= 3:
        total_price += (weighs * 200)
        microbus_cargos += weighs
    elif 4 <= weighs <= 11:
        total_price += (weighs * 175)
        truck_cargos += weighs
    elif weighs >= 12:
        total_price += (weighs * 120)
        train_cargos += weighs

all_cargo = microbus_cargos + truck_cargos + train_cargos
average_cargo_price = total_price / all_cargo
# result
print(f'{average_cargo_price:.2f}')
print(f'{((microbus_cargos / all_cargo) * 100):.2f}%')
print(f'{((truck_cargos / all_cargo) * 100):.2f}%')
print(f'{((train_cargos / all_cargo) * 100):.2f}%')
