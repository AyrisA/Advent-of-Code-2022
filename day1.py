import numpy as np

with open('day1_input.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

tot_calories = []
tot = 0
for el in data:
    if el == '':
        tot_calories.append(tot)
        tot = 0
    else:
        tot += int(el)

tot_calories = np.array(tot_calories)

# Part 1
print(tot_calories.max())

# Part 2
tot_calories.sort()
print(tot_calories[-3:].sum())