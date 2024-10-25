all_snowballs = int(input())

high_snowball = 0
high_snowball_weight = 0
high_snowball_time = 0
high_snowball_quality = 0


for snowball in range(all_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    current_snowball = int(snowball_weight / snowball_time) ** snowball_quality
    if current_snowball > high_snowball:
        high_snowball = current_snowball
        high_snowball_weight = snowball_weight
        high_snowball_time = snowball_time
        high_snowball_quality = snowball_quality

print(f'{high_snowball_weight} : {high_snowball_time} = {high_snowball} ({high_snowball_quality})')
