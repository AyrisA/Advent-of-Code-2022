import numpy as np

with open('day8_input.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

cols = len(data[0])
rows = len(data)
grid = np.zeros((rows, cols)).astype(int)

for i, row in enumerate(data):
    grid[i] = [x for x in row]

# Part 1
num_visible = (2 * cols) + (2 * (rows-2)) # Edge trees
for r in range(1, rows-1):
    for c in range(1, cols-1):
        height = grid[r, c]
        
        # Up
        if (grid[:r, c] < height).all():
            num_visible += 1
            continue

        # Down
        if (grid[r+1:, c] < height).all():
            num_visible += 1
            continue

        # Right
        if (grid[r, c+1:] < height).all():
            num_visible += 1
            continue

        # Left
        if (grid[r, :c] < height).all():
            num_visible += 1
            continue
        
print(f"There are {num_visible} trees visible")

# Part 2
score = np.zeros_like(grid)
for r in range(rows):
    for c in range(cols):
        height = grid[r,c]

        s1 = 0
        if r != 0:
            search_up = grid[:r, c].tolist()
            search_up.reverse()
            for tree in search_up:
                s1 += 1
                if tree >= height:
                    break

        s2 = 0
        if r != rows - 1:
            for tree in grid[r+1:, c]:
                s2 += 1
                if tree >= height:
                    break

        s3 = 0
        if c != cols - 1:
            for tree in grid[r, c+1:]:
                s3 += 1
                if tree >= height:
                    break

        s4 = 0
        if c != 0:
            search_left = grid[r, :c].tolist()
            search_left.reverse()
            for tree in search_left:
                s4 += 1
                if tree >= height:
                    break

        score[r,c] = s1 * s2 * s3 * s4

print(f"The highest scoring tree has score {score.max()}")