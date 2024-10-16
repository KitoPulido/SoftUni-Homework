string_1 = input()
string_2 = input()
last_printed_str = string_1
for j in range(len(string_1)):
    first_part = string_2[:j + 1]
    second_part = string_1[j + 1:]
    new_word = first_part + second_part
    if new_word != last_printed_str:
        print(new_word)
        last_printed_str = new_word
