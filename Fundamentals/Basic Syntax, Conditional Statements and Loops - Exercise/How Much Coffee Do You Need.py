command = input()
coffees = 0

while command != 'END':
    if command == 'dog' or command == 'cat' or command == 'coding' or command == 'movie':
        coffees += 1
    elif command == 'DOG' or command == 'CAT' or command == 'CODING' or command =='MOVIE':
        coffees += 2


    command = input()

if coffees > 5:
    print('You need extra sleep')
else:
    print(f'{coffees}')