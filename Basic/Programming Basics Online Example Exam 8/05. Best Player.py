# user data input
import sys

most_goals = -sys.maxsize
best_player = ''
user_input = False

while True:
    if user_input == True:
        break
    player_name = input()
    if player_name == 'END':
        user_input = True
        continue
    goals = int(input())
    if goals > most_goals:
        most_goals = goals
        best_player = player_name
    if goals >= 10:
        break

# result
print(f"{best_player} is the best player!")
if goals >= 3:
    print(f'He has scored {goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {goals} goals.')
