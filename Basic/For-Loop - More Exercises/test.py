a = 0
b = 0
while True:
    if a >= 24:
        break
    print(f'{a} : {b}')
    if b >= 59:
        a += 1
        b = 0
        continue
    b += 1
