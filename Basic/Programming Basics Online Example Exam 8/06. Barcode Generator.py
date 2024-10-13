num1 = int(input())
num2 = int(input())

for code in range(num1, num2 + 1):
    for i in range(code[0], num2[0]):
        if i % 2 == 0:
            i += 1

        else:
            continue
        print(code)