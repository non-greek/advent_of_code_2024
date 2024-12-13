import re
import numpy as np

filename = "../Data/data_day_13.txt"
total_problems = []
with open(filename) as f:
    prob = []
    for i, row in enumerate(f):
        if i % 4 == 3:
            total_problems.append(prob)
            prob = []
        else:
            nums = [int(num) for num in re.findall(r"(\d+)", row)]
            prob.extend(nums)

for correction in [0, 10000000000000]:
    total_solution = 0
    for problem in total_problems:
        c = np.array([3, 1])
        A = np.array(problem[:-2][::-1]).reshape((2, 2))
        A[1, 0] *= -1
        A[0, 1] *= -1
        b_eq = np.array(problem[-2:]) + correction
        solution = A @ b_eq
        # mulitply by the denominator at the end to minimize computational errors
        solution = solution / (A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0])
        if np.all(solution == solution.astype(int)):
            total_solution += c @ solution
    print(f"The minimum number of tokens required is: {total_solution:.0f}.")
