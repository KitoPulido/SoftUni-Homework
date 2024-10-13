# user data input
Taxi_Day = 0.79
Taxi_Night = 0.90
Bus_min_20 = 0.09
Train_min_100 = 0.06

km = int(input())
time_of_the_day = input()

# logic
day_taxi = (km * 0.79) + 0.70
night_taxi = (km * 0.90) + 0.70
bus = km * 0.09
train = km * 0.06

# result

if km < 20 and time_of_the_day == "day":
    print(f'{day_taxi:.2f}')
elif km < 20 and time_of_the_day == "night":
    print(f'{night_taxi:.2f}')
elif km >= 20 and km < 100:
    print(f'{bus:.2f}')
else:
    print(f'{train:.2f}')
