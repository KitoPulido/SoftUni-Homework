word = input()
result = 0

for char in range(0,len(word)):
    if word[char] == 'a':
        result += 1
    elif word[char] == 'e':
        result +=2
    elif word[char] == 'i':
        result += 3
    elif word[char] == 'o':
        result += 4
    elif word[char] == 'u':
        result += 5

print(result)