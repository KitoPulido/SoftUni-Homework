people = int(input())
capacity = int(input())

cours = int(people / capacity)

if people % capacity == 0:
    print(cours)
else:
    cours += 1
    print(cours)