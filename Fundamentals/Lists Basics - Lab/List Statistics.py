num = int(input())

positives = []
negatives = []
pos_count = 0
neg_sum = 0
for i in range(num):
    number = int(input())
    if number >= 0:
        positives.append(number)
        pos_count += 1
    else:
        negatives.append(number)
        neg_sum += number
print(positives)
print(negatives)
#print(f'Count of positives: {pos_count}')
#print(f'Sum of negatives: {neg_sum}')
print(f'Count of positives: {len(positives)}')
print(f'Sum of negatives: {sum(negatives)}')