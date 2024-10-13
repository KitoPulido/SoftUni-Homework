# user input data
x = float(input())
y = float(input())
h = float(input())
# logic
front_walls_area = (x * x * 2) - (2*1.2)
side_walls_area = (x * y * 2) - (1.5*1.5*2)
walls_area = front_walls_area + side_walls_area
roof_area = (((x * h) / 2) * 2) + (x * y) *2
green_paint = walls_area / 3.4
red_paint = roof_area / 4.3


# result
print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')