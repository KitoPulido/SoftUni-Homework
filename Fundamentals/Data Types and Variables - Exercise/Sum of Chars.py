num_of_char = int(input())

sum_of_char = 0

for char in range(num_of_char):
    char = input()
    sum_of_char += ord(char)

print(f'The sum equals: {sum_of_char}')