import re
import numpy as np
import math
filename ='../Data/data_day_8.txt'
data = open(filename).read()
freqs = list(set(filter(lambda x: x!='.' and x!='\n', data)))
data = data.split()
dict_coords ={}
for freq in freqs:
    dict_coords[freq] = []
    for i,row in enumerate(data):
        for j in range(len(row)):
            if row[j] == freq:
                dict_coords[freq].append((i,j))


n_rows, n_cols = len(data),len(data[0])
max_range = max(n_rows, n_cols)
mask_double = np.zeros((n_rows, n_cols))
mask_final = np.zeros((n_rows, n_cols))
for freq, coords in dict_coords.items():
    for i, (x_1, y_1) in enumerate(coords):
        for x_2, y_2 in coords[i+1:]:
            if x_1 == x_2:
                x_to_sum, y_to_sum = 0,1
            elif y_1 == y_2:
                x_to_sum,y_to_sum =1,0
            else:
                GCD = math.gcd(abs(x_1-x_2), abs(y_1-y_2))
                x_to_sum = int((x_1-x_2)/GCD)
                y_to_sum = int((y_1-y_2)/GCD)
            for t in range(-max_range, max_range):
                new_x = x_to_sum*t+x_1
                new_y = y_to_sum*t+y_1
                if new_x>=0 and new_y>=0 and new_x < n_rows and new_y < n_cols:
                    mask_final[new_x, new_y] = 1
                    d1 = abs(new_x- x_1)+abs(new_y-y_1)
                    d2 = abs(new_x-x_2) + abs(new_y-y_2)
                    if d1 == 2*d2 or d2 == 2*d1:
                        mask_double[new_x, new_y]=1
print(f'Answer 1: {int(mask_double.sum())}')
print(f'Answer 2: {int(mask_final.sum())}')                        
