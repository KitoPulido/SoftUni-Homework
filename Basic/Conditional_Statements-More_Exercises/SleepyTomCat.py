# user data input

free_days = int(input())

# logic
working_days = 365 - free_days
play_time_for_year = (free_days * 127) + (working_days * 63)
result = abs(30000 - play_time_for_year)
hours = result // 60
minutes = result % 60

# result

if play_time_for_year > 30000:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')

elif play_time_for_year < 30000:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')