name = input()
grade = 1
fail = 0
all_grades = 0
while grade <= 12:
    score = float(input())
    if score < 4:
        fail += 1
        if fail == 2:
            print(f'{name} has been excluded at {grade} grade')
            break
        continue
    elif score >= 4:
        all_grades += score
        grade += 1


average_score = all_grades / 12
if fail < 2:
    print(f'{name} graduated. Average grade: {average_score:.2f}')
