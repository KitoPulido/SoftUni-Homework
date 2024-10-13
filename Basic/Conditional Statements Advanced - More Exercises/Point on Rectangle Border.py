# user data input
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())
possition = ''
# logic
if (x == x1 or x == x2) and (y1 <= y and y <= y2):
    possition = 'Border'
elif (y == y1 or y == y2) and (x1 <= x and x <= x2):
        possition = 'Border'
else:
    possition = 'Inside / Outside'

# result
print(possition)
