prime_sum = 0
non_prime_sum = 0
number = input()
while number != 'stop':
    number = int(number)
    if number < 0:
        print(f'Number is negative.')
        number = input()
        continue
    if number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
        if number == 2 or number == 5 or number == 15 or number == 3:
            prime_sum += number
        else:
            non_prime_sum += number
    else:
        prime_sum += number
    number = input()

print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')
