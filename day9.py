with open('day9_input.txt', 'r') as f:
    data = [x.split() for x in f.readlines()]

def touching(H, T):
    is_touching = False
    hdist = abs(H[0]-T[0])
    vdist = abs(H[1]-T[1])
    if hdist <= 1 and vdist <= 1:
        is_touching = True
    return is_touching


def adjust_follower(H, T):
    """Works in place"""
    if not touching(H, T):  
        if H[0] == T[0]:
            if H[1] > T[1]:
                T[1] += 1
            else:
                T[1] -= 1
        elif H[1] == T[1]:
            if H[0] > T[0]:
                T[0] += 1
            else:
                T[0] -= 1
        else:
            if H[0] > T[0]:
                T[0] += 1
                if H[1] > T[1]:
                    T[1] += 1
                else:
                    T[1] -= 1
            else:
                T[0] -= 1
                if H[1] > T[1]:
                    T[1] += 1
                else:
                    T[1] -= 1
        return


def move_pair(initial_state, direction):
    """This function works in place on the state"""
    (H, T) = initial_state
    assert direction in ['R', 'L', 'U', 'D'], "This is a bad direction!"
    if direction == 'R':
        H[0] += 1
    elif direction == 'L':
        H[0] -= 1
    elif direction == 'U':
        H[1] += 1
    else:
        H[1] -= 1
    adjust_follower(H, T) 
    return

# Part 1
H = [0, 0]
T = [0, 0]
state = (H, T)
T_positions = set()
T_positions.add(tuple(T))
for direction, count in data:
    for i in range(int(count)):
        move_pair(state, direction)
        T_positions.add(tuple(T))

print(f"Final state: {state}")
print(f"T visisted {len(T_positions)} positions.\n")

# Part 2
H = [0, 0]
K1 = [0, 0]
K2 = [0, 0]
K3 = [0, 0]
K4 = [0, 0]
K5 = [0, 0]
K6 = [0, 0]
K7 = [0, 0]
K8 = [0, 0]
T = [0, 0]
state = (H, K1, K2, K3, K4, K5, K6, K7, K8, T)
T_positions = set()
T_positions.add(tuple(T))
for direction, count in data:
    for i in range(int(count)):
        move_pair((state[0], state[1]), direction) 
        for k in range(1, len(state)-1):
            adjust_follower(state[k], state[k+1])
        T_positions.add(tuple(T))

print(f"Final state: {state}")
print(f"T visisted {len(T_positions)} positions.")