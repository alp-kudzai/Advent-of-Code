#%%
from collections import defaultdict
from functools import lru_cache


with open('input.txt') as f:
    data = f.read().split('\n')

def clean(d:str):
    idx, char = d.split(' -> ')
    return idx,char

#print(data)
switch = False
init_seq = ''
ref = {}
for d in data:
    if switch:
        idx,char = clean(d)
        ref[idx] = char
    elif d != '':
        init_seq = list(d)
    elif d == '':
        switch = True

print(f'Intial sequence: {init_seq}\n')
#print(f'Reference: {ref}')


def build(pair):
    new_char = ref[pair]
    con = list(pair)
    #insert char in between the pair
    con.insert(1,new_char)
    return con

def add2seq(seq:list,pair):
    res = build(pair)
    if len(seq) == 0:
        for c in res:
            seq.append(c)
    else:
        # we only want the last char since the first is a repeating char
        for i in range(1,3):
            seq.append(res[i])
#@lru_cache
def recurse(qu:list, cont:list):
    if len(qu) < 2:
        return
    pair = f'{qu[0]}{qu[1]}'
    add2seq(cont,pair)
    qu.pop(0)
    recurse(qu,cont)

#stage_cont = []
b_copy = init_seq.copy()
# recurse(b_copy,stage_cont)
# print(f'\nResults {stage_cont}')

def step(num, seq):
    for s in range(num):
        cont = []
        recurse(seq,cont)
        seq = cont
    return seq

results = step(7,b_copy)

occurances = defaultdict(int)

def count_occ(data, dict:defaultdict):
    for c in data:
        dict[c] += 1

def get_minmax(dict:defaultdict):
    mini = 0
    maxi = 0
    for char,val in dict.items():
        if mini == 0 & maxi == 0:
            mini = val
            maxi = val 
        elif val > maxi:
            maxi = val 
        elif val < mini:
            mini = val
    return maxi,mini
        
        

#print(f'\nResults {results}')
count_occ(results,occurances)
mx,mn = get_minmax(occurances)
print(f'\nmax: {mx}\nmin: {mn}')
diff = mx-mn
print(f'\nDifference: {diff}')
    

#%%