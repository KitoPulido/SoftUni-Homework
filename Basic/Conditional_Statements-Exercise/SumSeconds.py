# user input data
athlete_1 = int(input())
athlete_2 = int(input())
athlete_3 = int(input())

#logic
time_in_sec = athlete_1 + athlete_2 + athlete_3
minutes = time_in_sec // 60
seconds = time_in_sec % 60

#result
if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')