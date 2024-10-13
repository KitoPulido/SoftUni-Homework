change = float(input())
# money = False
change = int(change * 100)
coins = 0
rest = change
while rest != 0:
    if rest >= 200:
        rest -= 200
        coins += 1
#        continue
    if 200 > rest >= 100:
        rest -= 100
        coins += 1
    if 50 <= rest < 100:
        rest -= 50
        coins += 1

    if 20 <= rest < 50:
        rest -= 20
        coins += 1
    if 10 <= rest < 20:
        rest -= 10
        coins += 1
    if 5 <= rest < 10:
        rest -= 5
        coins += 1
    if 2 <= rest < 5:
        rest -= 2
        coins += 1
#        continue
    if 0 < rest < 2:
        rest -= 1
        coins += 1
#    if rest == 0:
#        print(f'{coins}')
#        break
if rest == 0:
    print(f'{coins}')