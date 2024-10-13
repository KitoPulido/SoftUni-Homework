# user data input
import math

world_record = float(input())
distancce = float(input())
time_for_metar = float(input())

# logic

delay = math.floor(distancce / 15) * 12.5
swimming_time = (distancce * time_for_metar) + delay
# result

if swimming_time < world_record:
    print(f'Yes, he succeeded! The new world record is {swimming_time:.2f} seconds.')

elif swimming_time >= world_record:
    result = swimming_time - world_record
    print(f'No, he failed! He was {result:.2f} seconds slower.')