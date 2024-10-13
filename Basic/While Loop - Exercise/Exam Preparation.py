low_grades = int(input())
all_names = 0
all_grades = 0
fail = 0
last_exam = ''
while True:
    name = input()


    if name == 'Enough':
        average = all_grades / all_names
        print(f'Average score: {average:.2f}')
        print(f'Number of problems: {all_names}')
        print(f'Last problem: {last_exam}')
        break
    grade = int(input())
    last_exam = name
    all_names += 1
    all_grades += grade
    if grade <= 4:
        fail += 1
        if fail >= low_grades:
            print(f'You need a break, {fail} poor grades.')
            break
