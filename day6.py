with open('day6_input.txt','r') as f:
    datastream = f.readline().strip()

# Part 1
for ix in range(4, len(datastream)+1):
    chunk = datastream[ix-4:ix]
    if len(chunk) == len(set(chunk)):
        break

print(f"First start-of-packet marker after character {ix}")

# Part 2
for ix in range(14, len(datastream)+1):
    chunk = datastream[ix-14:ix]
    if len(chunk) == len(set(chunk)):
        break

print(f"First start-of-message marker after character {ix}")
