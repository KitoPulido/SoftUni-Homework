goal = 10000
steps = 0

while steps < goal:
    day_steps = input()
    if day_steps == 'Going home':
        last_steps = int(input())
        steps += last_steps
        if steps >= goal:
            print(f'Goal reached! Good job!')
            print(f'{(steps - goal)} steps over the goal!')
            break
        else:
            print(f'{(goal - steps)} more steps to reach goal.')
            break
    day_steps = int(day_steps)
    steps += day_steps
    if steps >= goal:
        print(f'Goal reached! Good job!')
        print(f'{(steps - goal)} steps over the goal!')
        break
