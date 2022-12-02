#%%
with open('input.txt', 'r') as f:
    raw_data = f.readlines()
    data = [x.strip() for x in raw_data]

def calculatePosition(data, position):
    newPosition = position[:]
    if data[0] == 'forward':
        newPosition[0] += int(data[1])
    elif data[0] == 'down':
        newPosition[1] += int(data[1])
    elif data[0] == 'up':
        newPosition[1] -= int(data[1])
    return newPosition

def getPosition(data):
    position = [0,0]
    processedInstruction = [0, 0]
    for instruction in data:
        processedInstruction[0], processedInstruction[1] = instruction.split(' ')
        position = calculatePosition(processedInstruction, position)
    return position

position = getPosition(data)
print(f'Final position: {position}\nx * y: {position[0] * position[1]}')

#part2
def calculatePosition2(data, position):
    newPosition = position[:]
    if data[0] == 'forward':
        newPosition[0] += int(data[1])
        newPosition[1] += newPosition[2]*int(data[1]) #aim*depth
    elif data[0] == 'down':
        newPosition[2] += int(data[1])
    elif data[0] == 'up':
        newPosition[2] -= int(data[1])
    #print(newPosition)
    return newPosition

def getPosition2(data):
    position = [0,0,0] #x, y, aim
    processedInstruction = [0, 0]
    for instruction in data:
        processedInstruction[0], processedInstruction[1] = instruction.split(' ')
        position = calculatePosition2(processedInstruction, position)
    return position

position2 = getPosition2(data)
print(f'Final position: {position2}\nx * y: {position2[0] * position2[1]}')
    
# %%
