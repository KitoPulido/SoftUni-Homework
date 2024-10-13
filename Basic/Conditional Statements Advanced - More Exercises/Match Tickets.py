# user data input
budget = float(input())
ticket_type = input()
people = int(input())
transport = 0
ticket_price = 0
rest_of_budget = 0
result = 0
# logic
if 0 < people <= 4:
    transport = budget * 0.75
elif 5 <= people <= 9:
    transport = budget * 0.6
elif 10 <= people <= 24:
    transport = budget * 0.5
elif 25 <= people <= 49:
    transport = budget * 0.4
elif people >= 50:
    transport = budget * 0.25

if ticket_type == 'VIP':
    ticket_price = people * 499.99
elif ticket_type == 'Normal':
    ticket_price = people * 249.99

rest_of_budget = budget - transport

# result
if rest_of_budget >= ticket_price:
    result = rest_of_budget - ticket_price
    print(f'Yes! You have {result:.2f} leva left.')
elif rest_of_budget < ticket_price:
    result = ticket_price - rest_of_budget
    print(f'Not enough money! You need {result:.2f} leva.')
