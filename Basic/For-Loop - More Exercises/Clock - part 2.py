a = 0
b = 0
c = 0

while True:
    if a >= 24:
        break
    print(f'{a} : {b} : {c}')
    if b == 59 and c == 59:
        a +=1
        b = 0
        c = 0
        continue
    if c >= 59:
        b += 1
        c = 0
        continue
    c += 1


