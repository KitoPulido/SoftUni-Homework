# user data input
examen_hour = int(input())
examen_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())
result = ''
# logic
exam = (examen_hour * 60) + examen_minutes
arrival = (arrival_hour * 60) + arrival_minutes
dif = abs(exam - arrival)
dif_hour = dif // 60
dif_minutes = dif % 60
if arrival > exam:
    result = 'Late'
    if dif_hour > 0:
        print(result)
        print(f'{dif_hour}:{dif_minutes:02d} hours after the start')
    else:
        print(result)
        print(f'{dif_minutes} minutes after the start')
elif 0 <= dif <= 30 and exam > arrival:
    result = 'On time'
    if 1 <= dif_minutes <= 30:
        print(result)
        print(f'{dif_minutes} minutes before the start')
elif exam == arrival:
    result = 'On time'
    print(result)
elif exam > arrival:
    result = 'Early'
    if dif_hour > 0:
        print(result)
        print(f'{dif_hour}:{dif_minutes:02d} hours before the start')
    else:
        print(result)
        print(f'{dif_minutes} minutes before the start')

# result
