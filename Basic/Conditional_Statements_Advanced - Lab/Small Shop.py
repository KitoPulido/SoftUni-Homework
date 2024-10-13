# user data input
product = input()
city = input()
qty = float(input())

result = 0
# logic
if city == 'Sofia':
    if product == 'coffee':
        result = qty * 0.50
    elif product == 'water':
        result = qty * 0.80
    elif product == 'beer':
        result = qty * 1.2
    elif product == 'sweets':
        result = qty * 1.45
    elif product == 'peanuts':
        result = qty * 1.60
elif city == 'Plovdiv':
    if product == 'coffee':
        result = qty * 0.40
    elif product == 'water':
        result = qty * 0.70
    elif product == 'beer':
        result = qty * 1.15
    elif product == 'sweets':
        result = qty * 1.30
    elif product == 'peanuts':
        result = qty * 1.50
elif city == 'Varna':
    if product == 'coffee':
        result = qty * 0.45
    elif product == 'water':
        result = qty * 0.70
    elif product == 'beer':
        result = qty * 1.10
    elif product == 'sweets':
        result = qty * 1.35
    elif product == 'peanuts':
        result = qty * 1.55
# result
print(result)