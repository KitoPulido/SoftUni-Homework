needed_number = int(input())
combinations = 0

for x1 in range(0, needed_number + 1):
    for x2 in range(0, needed_number + 1):
        for x3 in range(0, needed_number + 1):
            if (x1 + x2 + x3) == needed_number:
                combinations += 1

print(combinations)
