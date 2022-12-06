from copy import deepcopy

with open('day5_input.txt', 'r') as f:
    data = [x.strip('\n') for x in f.readlines()]

crates_data = []
for i in range(len(data)):
    if data[i] == '':
        break
    else:
        crates_data.append(data[i])
move_data = data[i+1:]

# Set initial stacks structure; First element is the top of its stack
stack_keys = crates_data[-1].split()
stacks0 =  dict(zip(stack_keys, len(stack_keys)*['']))
for c in crates_data[:-1]:
    ptr = 0
    for s in range(len(stacks0)):
        item = c[ptr:ptr+3]
        if item != '   ':
            stacks0[str(s+1)] += item.strip('[]')
        ptr += 4

def print_stacks(ss):
    for st in ss:
        print(st, ss[st])
    print()

def read_move(m):
    num, mv = m.split('from')
    num = int(num.split()[-1])
    src, dest =[x.strip() for x in  mv.split('to')]
    return num, src, dest

# Part 1
stacks = stacks0.copy()
for m in move_data:
    num, src, dest = read_move(m)
    crates = stacks[src][:num][::-1]  #grab and reverse order
    stacks[src] = stacks[src][num:]   #remove from source stack
    stacks[dest] = crates + stacks[dest] #add to destination stack

on_top = ''
for s in stack_keys:  #to guarantee order from an older dict
    on_top += stacks[s][0]

print(f"After the CrateMover 9000 has done its job, crates {on_top} are on top")


# Part 2
stacks = stacks0.copy()
for m in move_data:
    num, src, dest = read_move(m)
    crates = stacks[src][:num]    #grab and don't reverse order
    stacks[src] = stacks[src][num:]   #remove from source stack
    stacks[dest] = crates + stacks[dest] #add to destination stack

on_top = ''
for s in stack_keys:  #to guarantee order from an older dict
    on_top += stacks[s][0]

print(f"After the CrateMover 9001 has done its job, crates {on_top} are on top")