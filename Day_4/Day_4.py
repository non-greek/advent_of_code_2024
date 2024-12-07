import re
import numpy as np
data = open('data_day_4.txt').read()
rows = data.split('\n')[:-1]
columns = [''.join([row[i] for row in rows]) for i in range(len(rows[0]))]
diagonals_matrix = np.array([list(row) for row in rows])
diagonals = [''.join(list(np.diagonal(diagonals_matrix, offset = i))) for i in range(-len(rows),len(rows))]
diagonals += [''.join(list(np.diagonal(diagonals_matrix[::-1,], offset = -i))) for i in range(-len(rows),len(rows))]
all_data = rows + columns + diagonals
all_data += [data[::-1] for data in all_data]
count_xmas = sum([len(re.findall(r"XMAS", string)) for string in all_data])
print(count_xmas)


def find_X_MAS(rows):
    count_x_mas=0
    for i,row in enumerate(rows[1:-1]):
        for j,char in enumerate(row[1:-1]):
            if char == 'A' and {rows[i][j], rows[i+2][j+2]} == {'M', 'S'} and {rows[i+2][j], rows[i][j+2]} == {'M', 'S'}:
                count_x_mas +=1
    return count_x_mas

print(find_X_MAS(rows))




coords = {x+1j*y: c for y, r in enumerate(open('data_day_4.txt')) for x, c in enumerate(r)}
g = lambda c: coords.get(c, "")

s1 = s2 = 0
for c in coords:
    for d in [1, 1j, 1+1j, 1-1j, -1, -1j, -1+1j, -1-1j]:
        s1 += g(c) + g(c+d) + g(c+d*2) + g(c+d*3) == "XMAS"
        if d.imag and d.real:
            s2 += g(c+d) + g(c) + g(c-d) == "MAS" and g(c+d*1j) + g(c-d*1j) == "MS"

print(s1, s2, sep="\n")
