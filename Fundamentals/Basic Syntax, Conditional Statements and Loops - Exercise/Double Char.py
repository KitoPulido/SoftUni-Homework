word = input()

while word != 'End':
    if word != 'SoftUni':
        new_word = ''
        for char in word:
            new_word += char * 2
        print(new_word)
    word = input()