# user input data
import math

name_of_series = input()
episode_length = int(input())
break_length = int(input())

# logic
lunch_time = break_length * 0.125
relax_time = break_length * 0.25
all_activities = episode_length + lunch_time + relax_time


# result
result = math.ceil(break_length - all_activities)
result1 = math.ceil(all_activities - break_length)

if break_length >= all_activities:
    print(f'You have enough time to watch {name_of_series} and left with {result} minutes free time.')

elif break_length < all_activities:
    print(f"You don't have enough time to watch {name_of_series}, you need {result1} more minutes.")
