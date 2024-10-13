pages = int(input())
page_per_hour = int(input())
days = int(input())

needed_hours = int(pages / page_per_hour)
result = int(needed_hours / days)

print(result)