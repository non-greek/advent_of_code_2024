import more_itertools
from tqdm import tqdm
def get_operations_string(n_plus, total_length, n_concat=0):
    assert n_plus+n_concat <= total_length
    basic_operation = ['+']*n_plus+['*']*(total_length-n_concat-n_plus)+['||']*n_concat
    all_ops = list(set(more_itertools.distinct_permutations(basic_operation)))
    return sorted(all_ops)

def get_all_ops(total_length, include_concat=False):
    ops = []
    for i in range(total_length+1):
        if include_concat:
            for j in range(total_length+1-i):
                ops.extend(get_operations_string(i,total_length,j))
        else:    
            ops.extend(get_operations_string(i,total_length))
    return ops

def compute_op(ops, nums):
    assert len(ops) == len(nums)-1
    tot = nums[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            tot += nums[i+1]
        elif ops[i] == '*':
            tot *= nums[i+1]
        elif ops[i] == '||':
            tot = int(str(tot)+str(nums[i+1]))
    return tot


data_dict = {}
lens = []
filename = 'data_day_7.txt'
#filename = 'small_dataset.txt'
with open(filename) as f:
    for row in f:
        splitted_row = row.split(':')
        value = int(splitted_row[0])
        other_values = [int(val) for val in splitted_row[1].split()]
        #data_dict[value] = other_values
        if value in data_dict.keys(): data_dict[value].append(other_values)
        else: data_dict[value] = [other_values]
        lens.append(len(other_values))

total_valid = 0
all_ops_dict = {}
for target, value_lists in tqdm(data_dict.items()):
    for list_nums in value_lists:
        ops = all_ops_dict.get(len(list_nums), -1)
        if ops == -1:
            ops = get_all_ops(len(list_nums)-1, include_concat=True)  
            all_ops_dict[len(list_nums)] = get_all_ops(len(list_nums)-1, include_concat=True)
        for op in ops:
            tot = compute_op(op, list_nums)
            if tot == target:
                total_valid += target
                break
print(total_valid)
