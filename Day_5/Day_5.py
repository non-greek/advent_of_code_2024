from functools import cmp_to_key


def sort_function(numA, numB, rules):
    if (numA, numB) in rules:
        return -1
    elif (numB, numA) in rules:
        return 1
    else:
        return 0


rules, instructions = [], []
with open("data_day_5.txt") as f:
    for row in f:
        if "|" in row:
            idx = row.find("|") + 1
            rules.append((int(row[: idx - 1]), int(row[idx:])))
        elif "," in row:
            instructions.append([int(num) for num in row.split(",")])

incorrect_instructions = []
sum_middle_nums = 0
sum_incorrect_middle_nums = 0
for instruction in instructions:
    incorrect = False
    final_idx = len(instruction) - 1
    for curr_num in instruction[::-1]:
        for other_num in instruction[:final_idx]:
            if (curr_num, other_num) in rules:
                incorrect = True
                break
        final_idx -= 1
        if incorrect:
            break
    if incorrect:
        fixed_instruction = sorted(instruction, key=cmp_to_key(lambda x, y: sort_function(x, y, rules)))
        incorrect_instructions.append(instruction)
        sum_incorrect_middle_nums += fixed_instruction[(len(fixed_instruction) - 1) // 2]
        # print(len(instruction))
    else:
        sum_middle_nums += instruction[(len(instruction) - 1) // 2]
print("Sum of correct instructions:", sum_middle_nums)
print("Sum of fixed instructions:", sum_incorrect_middle_nums)
