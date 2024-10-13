# user data input
n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0

# logic
for _ in range(n):
    num = int(input())
    if num < 200:
        num1 += 1
    elif 200 <= num <= 399:
        num2 += 1
    elif 400 <= num <= 599:
        num3 += 1
    elif 600 <= num <= 799:
        num4 += 1
    else:
        num5 += 1

p1 = (num1 / n) * 100
p2 = (num2 / n) * 100
p3 = (num3 / n) * 100
p4 = (num4 / n) * 100
p5 = (num5 / n) * 100

# result
print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')