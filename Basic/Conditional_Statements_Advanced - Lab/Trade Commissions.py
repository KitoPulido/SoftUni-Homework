# user data input
city = input()
sales = float(input())
result = 'error'
# logic
if city == 'Sofia':
    if 0 <= sales <= 500:
        result = sales * 0.05
    elif 500 < sales <= 1000:
        result = sales * 0.07
    elif 1000 < sales <= 10000:
        result = sales * 0.08
    elif sales > 10000:
        result = sales * 0.12
elif city == 'Varna':
    if 0 <= sales <= 500:
        result = sales * 0.045
    elif 500 < sales <= 1000:
        result = sales * 0.075
    elif 1000 < sales <= 10000:
        result = sales * 0.1
    elif sales > 10000:
        result = sales * 0.13
elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        result = sales * 0.055
    elif 500 < sales <= 1000:
        result = sales * 0.08
    elif 1000 < sales <= 10000:
        result = sales * 0.12
    elif sales > 10000:
        result = sales * 0.145

# result

if result == 'error':
    print(result)
elif result < 0:
    print('error')
else:
    print(f'{result:.2f}')