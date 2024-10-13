budget = int(input())

remaining_budget = budget
spending = input()

while remaining_budget >= 0:

    if spending == 'End':
        break

    else:
        spending = int(spending)
        remaining_budget -= spending
        if remaining_budget < 0:
            break

    spending = input()

if remaining_budget >= 0:
    print('You bought everything needed.')
else:
    print('You went in overdraft!')