# data user input
age = float(input())
gender = input()
result = ''
# logic
if age >= 16:
    if gender == 'm':
        result = 'Mr.'
    else:
        result = 'Ms.'
elif age < 16:
    if gender == 'm':
        result = 'Master'
    else:
        result = 'Miss'
# result
print(result)