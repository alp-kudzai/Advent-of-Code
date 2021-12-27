#%%
from collections import defaultdict

conv = lambda s : list(map(int, s.replace(' -> ',',').split(',')))
lines = list(map(conv, open('input.txt').read().splitlines()))

def count_overlappings(lines, part2):
    vents = defaultdict(int)
    for x1,y1,x2,y2 in lines:
        x_range = range(x1, x2 + (-1 if x1 > x2 else 1), -1 if x1 > x2 else 1)
        y_range = range(y1, y2 + (-1 if y1 > y2 else 1), -1 if y1 > y2 else 1)
        if x1 == x2:
            for y in y_range: vents[(x1,y)] += 1
        elif y1 == y2:
            for x in x_range: vents[(x,y1)] += 1
        elif part2:
            for x,y in zip(x_range, y_range):
                vents[(x,y)] += 1
    return sum(value > 1 for value in vents.values())

print(f'Part 1: {count_overlappings(lines, False)}')
print(f'Part 2: {count_overlappings(lines, True)}')
# %%
