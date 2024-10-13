# user data input
air_bus_name = input()
ticket_old = int(input())
ticket_child = int(input())
ticket_old_price = float(input())
ticket_child_price = ticket_old_price * 0.3
service = float(input())
# logic
profit_old = ticket_old * (ticket_old_price + service)
profit_child = ticket_child * (ticket_child_price + service)
air_bus_profit = (profit_old + profit_child) * 0.2
# result
print(f'The profit of your agency from {air_bus_name} tickets is {air_bus_profit:.2f} lv.')
