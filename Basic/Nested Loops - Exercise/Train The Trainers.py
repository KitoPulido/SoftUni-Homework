juges = int(input())
grades = 0
presentation = input()
count = 0
all_gtrades = 0
while presentation != 'Finish':
    for exam in range(juges):
        grade = float(input())
        grades += grade
        all_gtrades += grade
        count += 1
    print(f'{presentation} - {(grades / juges):.2f}.')
    grades = 0
    presentation = input()

print(f"Student's final assessment is {(all_gtrades / count):.2f}.")
