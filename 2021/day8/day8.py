#%%
from collections import Counter, defaultdict
def getUsefulBit(line):
    res = line.split(' | ')
    return res[1]

with open('input.txt') as f:
    data = f.read().split('\n')
    outputVdata = [getUsefulBit(line) for line in data]
# Part 1   
customDict = defaultdict(int) #CD
def splitNpack(CD, line):
    data = line.split(' ')
    for l in data:
        CD[len(l)] += 1
    #return CD

for line in outputVdata:
    splitNpack(customDict, line)
total = 0
for k, v in customDict.items():
    if k in [2, 4, 3, 7]:
        total += v

print(f'Part 1: {total} is the total number of unique segments')
# %%
