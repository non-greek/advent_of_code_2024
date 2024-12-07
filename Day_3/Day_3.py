import re
data = open("data_day_3.txt").read()
def find_and_multiply(raw_string:str)->int:
    first_index, second_index = raw_string.find('(')+1, raw_string.find(',')+1
    return int(raw_string[first_index:second_index-1])*int(raw_string[second_index:-1])
num_matches = sum([find_and_multiply(instruction) for instruction in re.findall(r"mul\(\d+,\d+\)",data)])
print(f"The sum of the operations is {num_matches}.")
data = re.sub(r'(don\'t\(\))(.*?)(do\(\))', '',re.sub('\n', '', data))
data = re.sub(r'(don\'t\(\))(.*$)', '',data)
num_matches = sum([find_and_multiply(instruction) for instruction in re.findall(r"mul\(\d+,\d+\)",data)])
print(f"The sum of the operations is {num_matches}.")
