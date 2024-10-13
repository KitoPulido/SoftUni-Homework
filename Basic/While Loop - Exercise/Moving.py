width = int(input())
length = int(input())
height = int(input())
room_volum = width * length * height

no_more_space = room_volum

while no_more_space > 0:
    box = input()
    if box == 'Done':
        print(f'{no_more_space} Cubic meters left.')
        break
    else:
        box = int(box)
        no_more_space -= box
    if no_more_space <= 0:
        print(f'No more free space! You need {abs(no_more_space)} Cubic meters more.')
        break
