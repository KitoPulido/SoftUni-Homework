width = int(input())
length = int(input())
pieces = width * length
pieces_taken = 0

while pieces > 0:
    guest = input()
    if guest == 'STOP':
        print(f'{pieces} pieces are left.')
        break
    else:
        guest = int(guest)
        pieces -= guest

if pieces < 0:
    print(f'No more cake left! You need {abs(pieces)} pieces more.')

