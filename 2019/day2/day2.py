#%%
with open('input.txt', 'r') as f:
    data = f.readline().split(',')
    new_data = [int(x) for x in data]
GOAL = 19690720

#function that parses the data in chunks of 4
def computerParser(data):
    for i in range(0, len(data), 4):
        if data[i] == 1:
            data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
        elif data[i] == 2:
            data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
        elif data[i] == 99:
            break
        else:
            print('Error')
    return data

def incrementCounters(x, y):
    if y == 99:
        x += 1
        y = 0
    elif y < 99:
        y += 1
        
def Computer(data):
    safe_data = data.copy()
    noun_Counter, verb_Counter = 0, 0
    passes = 0
    noun, verb = 0, 0
    checking = True
    print('Doing Work...!')
    while checking:
        safe_data[1], safe_data[2] = noun_Counter, verb_Counter
        computerParser(safe_data)
        if safe_data[0] == GOAL:
            print(f'Found Solution!: noun => {noun_Counter}, verb => {verb_Counter}')
            noun, verb = noun_Counter, verb_Counter
            checking = False
            break
        elif noun_Counter > 99:
            checking = False
            break
        print(noun_Counter, verb_Counter)
        if verb_Counter == 99: 
            verb_Counter = 0
            noun_Counter += 1
        elif verb_Counter < 99:
            verb_Counter += 1
        print(noun_Counter, verb_Counter)
        safe_data = data.copy()
        passes += 1
    final_Solution = 100 * noun + verb
    print(f'Final solution: {final_Solution}\nPasses: {passes}')
        
    
    
Computer(new_data)



# %%
