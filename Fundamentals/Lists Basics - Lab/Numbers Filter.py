num = int(input())

even = []
odd = []
negative = []
positive = []

for i in range(num):
    number = int(input())
    if number % 2 == 0:
        even.append(number)
    if number % 2 != 0:
        odd.append(number)
    if number >= 0:
        positive.append(number)
    if number < 0:
        negative.append(number)
comand = input()
if comand == 'even':
    print(even)
if comand == 'odd':
    print(odd)
if comand == 'positive':
    print(positive)
if comand == 'negative':
    print(negative)