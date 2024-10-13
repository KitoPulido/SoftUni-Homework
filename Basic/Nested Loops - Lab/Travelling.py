destination = input()
sum = 0

while destination != 'End':
    budget = float(input())
    while sum < budget:
        save = float(input())
        sum += save
        if sum >= budget:
            print(f'Going to {destination}!')
            sum = 0
            break

    destination = input()