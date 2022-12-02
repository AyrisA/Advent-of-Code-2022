import numpy as np

with open('day2_input.txt', 'r') as f:
    data = [x.strip().split() for x in f.readlines()]

## Part 1 ##
# A,X = Rock
# B,Y = Paper
# C,Z = Scissors
strategy = np.array(data)
strategy[np.where((strategy == 'A') | (strategy == 'X'))] = 'R'
strategy[np.where((strategy == 'B') | (strategy == 'Y'))] = 'P'
strategy[np.where((strategy == 'C') | (strategy == 'Z'))] = 'S'
shape_score = {'R':1, 'P':2, 'S':3}

total_score = 0
for round in strategy:
    score = shape_score[round[1]]
    if round[0] == round[1]:
        score += 3
    else:
        if ((round[1] == 'R' and round[0] == 'S') 
            or (round[1] == 'P' and round[0] == 'R')
            or (round[1] == 'S' and round[0] == 'P')):
            score += 6
    total_score += score
print(f'Strategy guide score is: {total_score}')

## Part 2 ##
# A = Rock; B = Paper; C = Scissors
# X = Lose; Y = Draw; Z = Win
strategy = np.array(data)

them = strategy[:,0]
them[np.where(them == 'A')] = 'R'
them[np.where(them == 'B')] = 'P'
them[np.where(them == 'C')] = 'S'

result = strategy[:,1]
result[np.where(result == 'X')] = '0'
result[np.where(result == 'Y')] = '3'
result[np.where(result == 'Z')] = '6'
result = result.astype(int)

total_score = 0
for r in range(len(result)):
    score = result[r]
    if result[r] == 3:
        score += shape_score[them[r]]
    elif result[r] == 6:
        if them[r] == 'R':
            score += shape_score['P']
        elif them[r] == 'P':
            score += shape_score['S']
        else:
            score += shape_score['R']
    else:
        if them[r] == 'R':
            score += shape_score['S']
        elif them[r] == 'P':
            score += shape_score['R']
        else:
            score += shape_score['P']        
    total_score += score
print(f'Corrected strategy guide score is: {total_score}')
