# user data input
Time_After_15_min = 15

hour = int(input())
minutes = int(input())

# logic
all_to_min = (hour * 60) + minutes + 15
hour_after_15 = all_to_min // 60
minutes_after_15 = all_to_min % 60
if hour_after_15 >= 24:
    hour_after_15 = hour_after_15 - 24


# result
if minutes_after_15 < 10:
    print(f'{hour_after_15}:0{minutes_after_15}')
else:
    print(f'{hour_after_15}:{minutes_after_15}')
