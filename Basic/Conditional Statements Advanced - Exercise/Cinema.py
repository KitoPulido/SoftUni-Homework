# user data input
film = input()
rows = int(input())
seats = int(input())
income = 0
Premiere_Ticket = 12.00
Normal_Ticket = 7.50
Discount_Ticket = 5.00
# logic
all_seats = rows * seats
if film == 'Premiere':
    income = all_seats * Premiere_Ticket
elif film == 'Normal':
    income = all_seats * Normal_Ticket
elif film == 'Discount':
    income = all_seats * Discount_Ticket
# result
print(f'{income:.2f} leva')