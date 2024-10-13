divisor = int(input())
boundary = int(input())

for g in range(boundary, divisor, -1):
    if g % divisor == 0:
        if g > 0:
            print(g)
            break