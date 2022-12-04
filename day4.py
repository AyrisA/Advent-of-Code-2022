with open('day4_input.txt', 'r') as f:
    data = [x.strip().split(',') for x in f.readlines()]

def is_contained_in(p1, p2):
    return (p1[0] >= p2[0]) and (p1[1] <= p2[1])

def overlap(p1, p2):
    return (p1[1] >= p2[0] and p1[0] <= p2[1])

count_fully_contained = 0
count_overlaps = 0 
for pair in data:
    elf1 = [int(x) for x in pair[0].split('-')]
    elf2 = [int(x) for x in pair[1].split('-')]

    # Part 1
    if (elf1 == elf2) \
        or is_contained_in(elf1, elf2)\
        or is_contained_in(elf2, elf1):

        count_fully_contained += 1

    # Part 2
    if overlap(elf1, elf2):
        count_overlaps += 1

print(f'In {count_fully_contained} pairs one range fully contains the other')
print(f'There are {count_overlaps} overlapping pairs')