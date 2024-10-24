num_of_letters = int(input())

for letter in range(num_of_letters):
    chr_1 = chr(97 + letter)
    for letter_2 in range(num_of_letters):
        chr_2 = chr(97 + letter_2)
        for letter_3 in range(num_of_letters):
            chr_3 = chr(97 + letter_3)
            print(f'{chr_1}{chr_2}{chr_3}')
