lines = int(input())

open = 0
closed = 0
unbalanced = 0
for i in range(lines):
    str = input()
    if str == '(':
        if open > closed:
            if str == '(':
                unbalanced += 1
        elif closed > open:
            if str == '(':
                unbalanced += 1
        open += 1

    if str == ')':
        if closed > open:
            if str == ')':
                unbalanced += 1
        closed += 1

    if open == closed:
        open = 0
        closed = 0

if unbalanced > 0:
    print('UNBALANCED')
else:
    print('BALANCED')