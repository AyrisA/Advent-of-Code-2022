import numpy as np

with open('day10_input.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

cvlog = {}  # Cycle Value Log
X = 1
cycle = 1
for instruction in data:
    iparts = instruction.split()
    cvlog[cycle] = X    # happens for both noop and addx
    cycle += 1    
    if len(iparts) == 2:  # addx instruction second tick
        cvlog[cycle] = X
        cycle += 1
        X += int(iparts[1])

# Part 1
signal_str = []
for ix in range(20, 221, 40):
    signal_str.append(ix * cvlog[ix])
print(f"The sum of my interesting signal strengths is {sum(signal_str)}")

# Part 2
display = np.zeros((6, 40)).astype(int)
flat_display = display.ravel()
for i in range(240):
    X = cvlog[i+1]
    sprite_pos = [X-1, X, X+1]
    if i%40 in sprite_pos:
        flat_display[i] = 1  

display = display.astype(str)
display[display == '0'] = '.'
display[display == '1'] = '#'
pic = ''
for ii in range(len(display)):
    pic += (''.join(display[ii]))
    pic += '\n'
print(pic)
