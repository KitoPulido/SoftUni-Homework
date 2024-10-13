# user data input
computers_num = int(input())
all_sels = 0
all_ratings = 0
# logic
for i in range(computers_num):
    model = int(input())
    rating = model % 10
    sels = model // 10
    if rating == 2:
        all_ratings += 2
        all_sels += 0
    elif rating == 3:
        all_ratings += 3
        all_sels += sels / 2
    elif rating == 4:
        all_ratings += 4
        all_sels += sels * 0.7
    elif rating == 5:
        all_ratings += 5
        all_sels += sels * 0.85
    elif rating == 6:
        all_ratings += 6
        all_sels += sels
average_ratings = all_ratings / computers_num
# result
print(f'{all_sels:.2f}')
print(f'{average_ratings:.2f}')
