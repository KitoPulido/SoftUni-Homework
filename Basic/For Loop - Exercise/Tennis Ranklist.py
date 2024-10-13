# user data input
import math

num_of_tournament = int(input())
begining_points = int(input())
all_points = begining_points
wins = 0

# logic
for games in range(num_of_tournament):
    result = input()
    if result == 'W':
        wins += 1
        all_points += 2000
    elif result == 'F':
        all_points += 1200
    elif result == 'SF':
        all_points += 720

average_points = (all_points - begining_points) / num_of_tournament
average_wins = (wins / num_of_tournament) * 100
# output
print(f'Final points: {all_points}')
print(f'Average points: {math.floor(average_points)}')
print(f'{average_wins:.2f}%')