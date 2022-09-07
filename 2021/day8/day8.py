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

#part 2
#%%

def get_data(line):
    res = tuple(line.split(' | '))
    return res

customDict = {} #CD
def splitNpack(CD, line):
    data = line.split(' ')
    for l in data:
        if len(l) in [2,4,3,7]:
            CD[len(l)] = l

def decode(line, CD):
    data = line.split(' ')
    res = []
    for i in data:
        if len(i) == 2:
            res.append(1)
        elif len(i) == 4:
            res.append(4)
        elif len(i) == 3:
            res.append(7)
        elif len(i) == 7:
            res.append(8)
        elif len(i) == 5:
            seven = CD[3]
            four = CD[4]
            if evalute(seven,i,3) and evalute(four,i,3): res.append(3)
            elif evalute(four, i, 3) and not evalute(seven,i,3): res.append(5)
            else: res.append(2)
            pass
        elif len(i) == 6:
            seven = CD[3]
            four = CD[4]
            if evalute(four,i,4) and evalute(seven,i,3): res.append(9)
            elif evalute(seven,i, 3) and evalute(four,i,3): res.append(0)        
            else: res.append(6)
    string = ''
    for num in res:
        string += str(num)
    final_res = string
    return final_res

def evalute(uniq, to_eval, match):
    '''
    Given a unique 7 seg number like 1,4,7,8
    and a number to decode, this func will return true if all the segments of the unique number appear in the number to evaluate
    the match is the number of segment that are meant to match to_eval
    '''
    len_uniq = len(uniq)
    count = 0
    for c in tuple(uniq):
        if c in to_eval:
            count += 1
    if count == match: return True
    return False

with open('input.txt') as f:
    data = f.read().split('\n')
    res = [get_data(line) for line in data]
    #print(res)
final_res = []
for tup in res:
    unique_patterns = tup[0]    #the 10 unique patterns that make up 0-9
    to_decode = tup[1] # the numbers i need to decode
    splitNpack(customDict, unique_patterns)
    #print(customDict) # {2: 'be', 7: 'cfbegad', 4: 'cgeb', 3: 'edb'}
    final_res.append(decode(to_decode,customDict))
print(final_res)

# sum up all the string numbers in final_res

number_list = map(int, final_res)
sum_of_numbers = sum(list(number_list))

print(f'The sum of all the numbers is: {sum_of_numbers}')
    




# %%
