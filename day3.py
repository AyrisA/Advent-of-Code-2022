from string import ascii_letters

priorities = dict(zip(ascii_letters, range(1,53)))

with open('day3_input.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

# Part 1
def find_mistake_items(contents):
    num_items = len(contents)
    half = num_items // 2
    assert num_items % 2 == 0, "There are not an even number of items in this bag!"  #Just in case

    comp1 = set(contents[:half])
    comp2 = set(contents[half:])

    return comp1.intersection(comp2)

priority_sum = 0
for rucksack in data:
    mistakes = find_mistake_items(rucksack)
    for m in mistakes:
        priority_sum += priorities[m]

print(f"The sum of the priorities is {priority_sum}")


# Part 2
def find_group_badge(group_sacks):
    badge = set(group_sacks[0])
    badge.intersection_update(set(group_sacks[1]))
    badge.intersection_update(set(group_sacks[2]))
    return badge

badge_priority_sum = 0
for g in range(0, len(data), 3):
    group_badge = find_group_badge(data[g:g+3])
    for b in group_badge:
        badge_priority_sum += priorities[b]

print(f"The sum of the badge priorities is {badge_priority_sum}")
