# user input data
w = float(input())
h = float(input())

# logic
if h >= 3 and h <= w and w <= 100:
    w_num = (w * 100) // 120
    h_num = ((h - 1) * 100) // 70
    all_desks = (w_num * h_num ) - 3

# result
    print(all_desks)