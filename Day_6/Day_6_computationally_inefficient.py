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
    count_traversed = 0
    curr_char = data[x_pos, y_pos]
    positions = [(x_pos,y_pos)]
    positions_with_dir = [(x_pos, y_pos, curr_char)]
    out = False
    while True:
        count_traversed +=1
        x_pos, y_pos, curr_char, rotated = take_next_action(data,x_pos,y_pos,curr_char)
        if data[x_pos][y_pos] == '-':
            out = True
            break
        if (x_pos,y_pos) not in positions:
            positions.append((x_pos,y_pos))
        if (x_pos, y_pos, curr_char) in positions_with_dir:
            break
        else:
            positions_with_dir.append((x_pos, y_pos, curr_char))
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
print('Computing obstacles positions...')
count_obstacles = 0
for x,y in tqdm(positions[1:]):
    data[x,y] = '#'
    _, out, _ = compute_full_path(data, starting_pos)
    if not out:
        count_obstacles +=1
#        print(x,y)
    data[x,y] = '.'
print('Number of obstacle positions: ', count_obstacles)
