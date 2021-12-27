#%%
from collections import deque, Counter

testData = deque([3,4,3,1,2])
def run(fishes):
    def helper(fish):
        fish -= 1
        if fish == -1:
            fish = 6
            return {'fish': fish, 'spawn': True}
        else: return {'fish': fish, 'spawn': False}
    spawnCounter = 0
    newFishes = deque([])
    for f in fishes:
        fObj = helper(f)
        if fObj['spawn']:
            spawnCounter += 1
        newFishes.append(fObj['fish'])
    if spawnCounter > 0:
        for s in range(spawnCounter):
            newFishes.append(8)
    return newFishes

def runOverDays(fishes, days):
    dayResult = fishes.copy()
    for i in range(days):
        dayResult = run(dayResult)
    return dayResult
state = {i: 0 for i in range(9)}       
with open('input.txt', 'r') as f:
    data = f.read().split(',')
    for i in data:
        state[int(i)] += 1
    cleanData = deque(list(map(int, data)))
    
for _ in  range(256):
    zero_state = state[0]
    for i in range(8):
        state[i] = state[i+1]
    state[8] = zero_state
    state[6] += zero_state

part1 = runOverDays(cleanData, 80)
print(f'Part1: {len(part1)}')
print(f'Part2: {sum(state.values())}')
# %%
