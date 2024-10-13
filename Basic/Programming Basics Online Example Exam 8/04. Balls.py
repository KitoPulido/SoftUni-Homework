# user data input
import math

balls = int(input())
points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
others_colors = 0
black_divides = 0
# logic
for ball in range(balls):
    color = input()
    if color == 'red':
        points += 5
        red_balls += 1
    elif color == 'orange':
        points += 10
        orange_balls += 1
    elif color == 'yellow':
        points += 15
        yellow_balls += 1
    elif color == 'white':
        points += 20
        white_balls += 1
    elif color == 'black':
        points = math.floor(points / 2)
        black_divides += 1
    else:
        others_colors += 1
        continue
# result
print(f'Total points: {points}')
print(f'Red balls: {red_balls}')
print(f'Orange balls: {orange_balls}')
print(f'Yellow balls: {yellow_balls}')
print(f'White balls: {white_balls}')
print(f'Other colors picked: {others_colors}')
print(f'Divides from black balls: {black_divides}')
