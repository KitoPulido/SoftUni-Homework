# user data input
time = int(input())
day_of_week = input()
result = ''
# logic
if 10 <= time <= 18:
   if day_of_week != 'Sunday':
     result = 'open'
   else:
      result = 'closed'
else:
    result = 'closed'
# result
print(result)
