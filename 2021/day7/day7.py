#%%
import numpy as np

testData = np.array([16,1,2,0,4,2,7,1,2,14])
def acc(start, end):
    if start > end:
        start, end = end, start
    const = 1
    total = 0
    #arr = np.array([]).astype(int)
    for i in range(start+1, end+1):
        #arr = np.append(arr, const)
        total += const
        const += 1
    return total
def findPos(data):
    endIndx = len(data)-1
    currIndx = 0
    def permutate(data, currIndx, endIndx, optimal, fuelCost=np.array([0])):
        if currIndx == endIndx:
            return [fuelCost, optimal]
        currCrab = data[currIndx]
        #part1
        #nextFuelCost = np.array([abs(currCrab - d) for d in data])
        #part2
        nextFuelCost = np.array([acc(currCrab, d) for d in data])
        #removed .sum()
        if nextFuelCost.sum() < fuelCost.sum() or fuelCost.sum() == 0:
            optimal = currIndx
            fuelCost = nextFuelCost
            #print(f'Found Current Optimal Index: {optimal}\nCurrent Fuel Cost: {fuelCost.sum()}\nPosition: {data[optimal]}')
        return permutate(data, currIndx+1, endIndx, optimal, fuelCost)
    return permutate(data, currIndx, endIndx, 0)

data = np.genfromtxt('input.txt', delimiter=',', dtype=int)
#print(list(data))
result = findPos(data)
#part1
#print(f'Optimal Index: {result[1]}\nFuel Cost: {result[0].sum()}')
# part2
print(f'Optimal Index: {result[1]}\nFuel Cost: {result[0].sum()}')
# %%
