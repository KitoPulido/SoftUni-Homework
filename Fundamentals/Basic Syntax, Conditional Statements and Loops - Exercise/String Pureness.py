num_of_str = int(input())
#signs = 0

for str in range(num_of_str):
    current_string = input()
    if ',' in current_string or '_' in current_string or '.' in current_string:
        print(f'{current_string} is not pure!')
    else:
        print(f'{current_string} is pure.')
#    for j in range(len(current_string)):
#        character = current_string[j]
#        if character == ',' or character == '_' or character == '.' :
#            signs += 1
            #continue
#    if signs > 0:
#        print(f'{current_string} is not pure!')
#    else:
#        print(f'{current_string} is pure.')


