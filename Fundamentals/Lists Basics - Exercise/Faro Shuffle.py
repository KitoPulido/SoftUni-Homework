faro_list = input().split(' ')
shuffle_times = int(input())

for cur_shuffle in range(shuffle_times):
    middle_list = len(faro_list) // 2
    first_part = faro_list[:middle_list]
    second_part = faro_list[middle_list:]
    new_faro_list = []
    for shuffle in range(len(first_part)):
        new_faro_list.append(first_part[shuffle])
        new_faro_list.append(second_part[shuffle])
    faro_list = new_faro_list

print(new_faro_list)
