key = int(input())

letters = int(input())

message = []

for char in range(letters):
    current_chr = input()
    new_chr = ord(current_chr) + key
    message.append(chr(new_chr))

for elements in message:
    print(elements, end='')