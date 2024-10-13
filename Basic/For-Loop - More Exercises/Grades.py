# user data input
num_of_students = int(input())
all_grades = 0
top_students = 0
middle_students = 0
low_students = 0
fail = 0
# logic
for exam in range(num_of_students):
    student_grade = float(input())
    all_grades += student_grade
    if 2 <= student_grade < 3:
        fail += 1
    elif 3 <= student_grade < 4:
        low_students += 1
    elif 4 <= student_grade < 5:
        middle_students += 1
    else:
        top_students += 1

average_grade = all_grades / num_of_students
# result
print(f'Top students: {((top_students / num_of_students) * 100):.2f}%')
print(f'Between 4.00 and 4.99: {((middle_students / num_of_students) * 100):.2f}%')
print(f'Between 3.00 and 3.99: {((low_students / num_of_students) * 100):.2f}%')
print(f'Fail: {((fail / num_of_students) * 100):.2f}%')
print(f'Average: {average_grade:.2f}')
