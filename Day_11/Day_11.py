import copy

def insert_freq_dict(dictionary, key, freq):
    if key in freq_dict.keys():
        freq_dict[key] += freq
    else:
        freq_dict[key] = freq


curr_str = open("../Data/data_day_11.txt").read().strip()
curr_list = [int(num) for num in curr_str.split()]
freq_dict = {k: curr_list.count(k) for k in curr_list}
sons_dict = {}
for it in range(75):
    if it == 25:
        print("Solution part 1 (25 blinks):", sum(freq_dict.values()))
    old_dict = copy.deepcopy(freq_dict)
    for num, freq in old_dict.items():
        if freq <= 0:
            continue
        freq_dict[num] -= freq
        if num in sons_dict.keys():
            list_nums_to_add = sons_dict[num]
            for add_num in list_nums_to_add:
                insert_freq_dict(freq_dict, add_num, freq)
            continue
        if num == 0:
            insert_freq_dict(freq_dict, 1, freq)
            sons_dict[0] = [1]
            continue
        num_length = len(str(num))
        if num_length % 2 == 0:
            next_num_1 = int(str(num)[: num_length // 2])
            next_num_2 = int(str(num)[num_length // 2 :])
            sons_dict[num] = [next_num_1, next_num_2]
            insert_freq_dict(freq_dict, next_num_1, freq)
            insert_freq_dict(freq_dict, next_num_2, freq)
        else:
            next_num = num * 2024
            sons_dict[num] = [next_num]
            insert_freq_dict(freq_dict, next_num, freq)
print("Solution part 2 (75 blinks):", sum(freq_dict.values()))
