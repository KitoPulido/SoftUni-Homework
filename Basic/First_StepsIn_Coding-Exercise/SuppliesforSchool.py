pen = float(input()) * 5.8
marker = float(input()) * 7.2
chemicals = float(input()) * 1.2
discount = float(input()) / 100

sum = pen + marker + chemicals
final_discount = sum * discount
price = sum - final_discount

print(price)