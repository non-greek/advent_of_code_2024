import numpy as np
filename='../Data/data_day_9.txt'
data = open(filename).read().strip()
data = [int(num) for num in data]
print('********** PART 1 **********')
last_id = (len(data)-1)/2
last_num = data.pop()
idx = 0
previous_id = 0
total_sum = 0
for i,num in enumerate(data):
    if i%2==0:
        previous_id = i/2
        total_sum += previous_id*np.arange(idx, idx+num).sum()
        idx += num        
    else:
        remaining = num
        while remaining > 0 and last_id>previous_id:
            if remaining >= last_num:
                remaining -= last_num
                total_sum += last_id*np.arange(idx, idx+last_num).sum()
                idx+=last_num
                last_id -=1
                data.pop()
                last_num = data.pop()
            else:
                last_num -= remaining
                total_sum += last_id*np.arange(idx, idx+remaining).sum()
                idx += remaining
                remaining = 0
if last_id>previous_id:
    total_sum += last_id*np.arange(idx, idx+last_num).sum()
print(int(total_sum))


print('********** PART 2 **********')

filename='../Data/data_day_9.txt'
data = open(filename).read().strip()
data = [int(num) for num in data]
last_id = (len(data)-1)/2
idx = 0
total_sum = 0
id_num_list = [k for k in data[::2]]
inserted_nums = np.zeros((len(id_num_list),))
available_spaces = [k for k in data[1::2]]
forward_idx = 0
spaces_idx = 0
for i in range(len(data)):
    if i%2==0:
        num = id_num_list[forward_idx]
        if inserted_nums[forward_idx]==0:
            total_sum += forward_idx*np.arange(idx, idx+num).sum()
            inserted_nums[forward_idx]+=1
        idx+=num
        forward_idx+=1
    else:
        backwards_idx = (len(data)-1)//2
        remaining = available_spaces[spaces_idx]
        spaces_idx+=1
        while backwards_idx>=0 and remaining>0:
            if id_num_list[backwards_idx]<=remaining and inserted_nums[backwards_idx]==0:
                remaining-=id_num_list[backwards_idx]
                inserted_nums[backwards_idx]+=1
                total_sum += backwards_idx*np.arange(idx, idx+id_num_list[backwards_idx]).sum()
                idx+=id_num_list[backwards_idx]
            backwards_idx -=1
        idx+=remaining
print(total_sum)




        








