import math

type = str(input())
if type == "square":
    a = float(input())
    square_face = a * a
    print(round(square_face, 3))
elif type == "rectangle":
    a = float(input())
    b = float(input())
    rectangle_face = a * b
    print(round(rectangle_face, 3))
elif type == "circle":
    a = float(input())
    circle_face = math.pi * (a * a)
    print(round(circle_face, 3))
elif type == "triangle":
    a = float(input())
    b = float(input())
    triangle_face = (a * b) / 2
    print(round(triangle_face, 3))