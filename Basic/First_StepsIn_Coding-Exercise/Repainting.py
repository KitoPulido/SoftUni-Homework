nylon = 1.5 * float(input())
paint = 14.5 * float(input())
thinner = 5 * float(input())
hours = float(input())

extra_paint = paint * 0.1
materials = nylon + paint + thinner + extra_paint + 3.4
worker = (materials * 0.3) * hours
cost = materials + worker

print(cost)