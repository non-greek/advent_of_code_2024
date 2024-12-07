import numpy as np 
from tqdm import tqdm

def take_next_action(data, x_pos, y_pos, curr_char):
    rotated = False
    if curr_char == '^':
        if data[x_pos-1][y_pos]!='#':
            x_pos = x_pos-1
        else:
            curr_char = '>'
            rotated = True

    if curr_char == '>' and (not rotated):
        if data[x_pos][y_pos+1]!='#':
            y_pos = y_pos+1
        else:
            curr_char = 'v'
            rotated = True

    if curr_char == 'v' and (not rotated):
        if data[x_pos+1][y_pos]!='#':
            x_pos = x_pos+1
        else:
            curr_char = '<'
            rotated = True

    if curr_char == '<' and (not rotated):
        if data[x_pos][y_pos-1]!='#':
            y_pos = y_pos-1
        else:
            curr_char = '^'
            rotated = True
    return x_pos, y_pos, curr_char, rotated

def compute_full_path(data, starting_pos): 
    x_pos, y_pos = starting_pos
    curr_char = data[x_pos, y_pos]
    positions = np.zeros(data.shape)
    positions[x_pos, y_pos] =1
    positions_with_dir = {'^': np.zeros(data.shape), '>': np.zeros(data.shape), 'v': np.zeros(data.shape), '<':np.zeros(data.shape)}
    out = False
    while True:
        x_pos, y_pos, curr_char, rotated = take_next_action(data,x_pos,y_pos,curr_char)
        if curr_char =='#':
            print(curr_char)
        if data[x_pos][y_pos] == '-':
            out = True
            break
        positions[x_pos][y_pos]+=1
        if positions_with_dir[curr_char][x_pos,y_pos]==1:
            break
        else:
            positions_with_dir[curr_char][x_pos,y_pos]=1
    count_traversed = (positions>0).sum()
    positions = np.argwhere(positions)
    return count_traversed, out, positions


data = []

# open the file and add left and right padding with '-', as well as record the starting position (note: i+1 is because we will add top and bottom padding as well)
filename = 'data_day_6.txt'
#filename ='small_data.txt'
with open(filename) as f:
    for i,row in enumerate(f):
        row = '-'+row[:-1]+'-'
        data.append(list(row))
        j = row.find('^')
        if j>=0:
            starting_pos = (i+1,j)
# remove the last row ('\n')
#data = data[:-1]

#insert top and bottom padding
data.insert(0, ['-']*len(data[0]))
data.append(['-']*len(data[0]))

# convert to numpy array for convenience
data = np.array(data)
count_traversed, out, positions = compute_full_path(data, starting_pos)
print(f'Number of distinct points:' ,count_traversed)
print('Computing obstacle positions...')
count_obstacles = 0
for x,y in tqdm(positions):
    if (x,y) == starting_pos:
        continue
    data[x,y] = '#'
    _, out, _ = compute_full_path(data, starting_pos)
    if not out:
        count_obstacles +=1
    data[x,y] = '.'
print('Number of obstacle positions: ', count_obstacles)
