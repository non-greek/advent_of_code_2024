data = []
with open("data_day_2.txt", "r") as f:
    for row in f:
        data.append(row)

safe_count = 0

for row in data:
    row = row.split()
    if len(row) == 0:
        continue
    previous_el = int(row[0])
    is_growing = int(row[1]) > int(row[0])
    for i, el in enumerate(row[1:]):
        el = int(el)
        distance = abs(el - previous_el)
        if distance > 3 or distance < 1:
            break
        if is_growing and previous_el > el:
            break
        if (not is_growing) and previous_el < el:
            break
        previous_el = el
        if i == (len(row[1:]) - 1):
            safe_count += 1


print(f"The number of safe reports is {safe_count}.")


safe_count = 0
for row in data:
    row = row.split()
    if len(row) == 0:
        continue
    for i in range(len(row)):
        shortened_row= row[:i]+row[i+1:]
        previous_el = int(shortened_row[0])
        is_growing = int(shortened_row[1]) > int(shortened_row[0])
        is_safe = False
        for j,el in enumerate(shortened_row[1:]):
            el = int(el)
            distance = abs(el - previous_el)
            if distance > 3 or distance < 1:
                break
            if is_growing and previous_el > el:
                break
            if (not is_growing) and previous_el < el:
                break
            previous_el = el
            if j == (len(shortened_row[1:]) - 1):
                is_safe = True
        if is_safe:
            safe_count+=1
            break
        
print(f"The number of safe reports is {safe_count}.")


