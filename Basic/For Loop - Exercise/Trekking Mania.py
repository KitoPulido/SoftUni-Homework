# user data input
num_of_groups = int(input())
all_people = 0
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

# logic
for people in range(num_of_groups):
    people = int(input())
    if people <= 5:
        musala += people
        all_people += people
    elif 6 <= people <= 12:
        monblan += people
        all_people += people
    elif 13 <= people <= 25:
        kilimandjaro += people
        all_people += people
    elif 26 <= people <= 40:
        k2 += people
        all_people += people
    else:
        everest += people
        all_people += people

# output
print(f'{((musala / all_people) * 100):.2f}%')
print(f'{((monblan / all_people) * 100):.2f}%')
print(f'{((kilimandjaro / all_people) * 100):.2f}%')
print(f'{((k2 / all_people) * 100):.2f}%')
print(f'{((everest / all_people) * 100):.2f}%')
