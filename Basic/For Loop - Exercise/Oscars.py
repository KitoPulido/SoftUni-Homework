# user data input
actor_name = input()
points_academy = float(input())
judges = int(input())
all_points = points_academy
# logic
for _ in range(judges):
    judge_name = input()
    judge_points = float(input())
    all_points += (len(judge_name) * judge_points) / 2
    if all_points > 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {all_points:.1f}!')
        break

if all_points <= 1250.5:
    print(f'Sorry, {actor_name} you need {(1250.5 - all_points):.1f} more!')

# result

