#%%
with open('input1.txt', 'r') as f:
    lines = f.readlines()
    raw_data = [int(line.strip()) for line in lines]
    
def countDepthIncrease(data):
    '''
    Counts the numer of increase in depth of an entry in data from the previous entry
    '''
    count = 0
    prevEntry = 0
    curEntry = 0
    for e in data:
        if e == data[0]:
            prevEntry = e
        else:
            curEntry = e
            if curEntry > prevEntry:
                count += 1
            prevEntry = curEntry
    return count

print(countDepthIncrease(raw_data))
#Part 2

def slidingWindowDepth(data):
    '''
    count the number of times the sum of measurements in the current entry and the next 2 entrys increases from the previous sum.
    '''
    count = 0
    prevEntrySum = 0
    curEntrySum = 0
    for ind in range(len(data)):
        if ind+3 <= len(data):
            if ind == 0:
                prevEntrySum = data[ind] + data[ind+1]+ data[ind+2]
            else:
                curEntrySum = data[ind] + data[ind+1]+ data[ind+2]
                if curEntrySum > prevEntrySum:
                    count += 1
                prevEntrySum = curEntrySum
    return count

testData = [199,200,208,210,200,207,240,269,260,263]
print(slidingWindowDepth(raw_data))

# %%
