import numpy as np
arr1 = []
arr2 = []
with open("day_1_data.txt", "r") as f:
    for row in f:
        splitted_rows = row.split()
        if len(splitted_rows)>0:
            arr1.append(int(splitted_rows[0]))
            arr2.append(int(splitted_rows[1]))

arr1.sort()
arr2.sort()
arr1 = np.array(arr1)
arr2 = np.array(arr2)

print("-------- First method --------")
differences = 0
for val1, val2 in zip(arr1, arr2):
    differences += abs(val1-val2)

print(f"The total distance is {differences}!\n")


distance = 0
print("-------- Second method --------")
for val in arr1:
    distance += val*(arr2==val).sum()
    
print(f"The total distance is {distance}!\n")
