# user data input
people_in_group = int(input())
night = int(input())
transport_cards = int(input())
museum_tickets = int(input())

# logic
all_nights = people_in_group * (night * 20)
all_transport_cards = transport_cards * (people_in_group * 1.60)
all_museum_cards = museum_tickets * (people_in_group * 6)
all_cost = all_nights + all_transport_cards + all_museum_cards
sum = all_cost * 1.25

# result
print(f'{sum:.2f}')
