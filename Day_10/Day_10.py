import numpy as np
import re

def count_paths(z_pos, n_pos, rows):
    curr_pos = [z_pos]
    found_path = False
    count_paths = 0
    while curr_pos != []:
        next_pos = curr_pos.pop()
        next_i, next_j = next_pos
        if next_i-1>=0 and rows[next_i-1][next_j]-rows[next_i][next_j]==1:
            curr_pos.append((next_i-1, next_j))
        if next_i+1<len(rows) and rows[next_i+1][next_j]-rows[next_i][next_j]==1:
            curr_pos.append((next_i+1, next_j))
        if next_j-1>=0 and rows[next_i][next_j-1]-rows[next_i][next_j]==1:
            curr_pos.append((next_i, next_j-1))
        if next_j+1<len(rows) and rows[next_i][next_j+1]-rows[next_i][next_j]==1:
            curr_pos.append((next_i, next_j+1))
        if (next_i,next_j)==n_pos:
            count_paths +=1
    return count_paths


rows = []
zeros_pos = []
nines_pos = []
filename = '../Data/data_day_10.txt'
with open(filename) as f:
    for i,row in enumerate(f):
        int_row = [int(num) for num in row.strip()]
        rows.append(int_row)
        for j,num in enumerate(int_row):
            if num == 0:
                zeros_pos.append((i,j))
            if num == 9:
                nines_pos.append((i,j))

ratings_sum = 0
total_scores = 0
for z_pos in zeros_pos:
    for n_pos in nines_pos:
        num_paths = count_paths(z_pos, n_pos, rows)
        if num_paths > 0:
            total_scores+=1
            ratings_sum+=num_paths

print(f'The sum of the trailheads is {total_scores}.')
print(f'The sum of the ratings is {ratings_sum}.')

