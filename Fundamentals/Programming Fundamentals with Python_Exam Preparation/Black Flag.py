days_in_action = int(input())
plunder_day = int(input())
expected_plunder = int(input())

real_plunder = 0

for day in range(1, days_in_action + 1):
    real_plunder += plunder_day
    if day % 3 == 0:
        real_plunder += plunder_day * 0.5

    if day % 5 == 0:
        real_plunder = real_plunder - (real_plunder * 0.3)

if real_plunder >= expected_plunder:
    print(f'Ahoy! {real_plunder:.2f} plunder gained.')
else:
    remaining_plunder = (real_plunder / expected_plunder) * 100
    print(f'Collected only {remaining_plunder:.2f}% of the plunder.')
