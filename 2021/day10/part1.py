
#%%
with open('input.txt') as f:
    data = f.read().split('\n')
    matrix = [list(line) for line in data]

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

ref = {
    ')' : '(',
    '}' : '{',
    ']' : '[',
    '>' : '<'
}

o_paran = [
    '(',
    '{',
    '[',
    '<'
    ]

def analyse(line):
    rg = len(line)-1
    cont = []
    def h(idx):
        #print(f'range: {len(line)-1}\nIndex: {idx}')
        if idx == 0:
            cont.append(line[idx])
            if idx < rg : return h(idx+1)
        else:
            if line[idx] in o_paran:
                cont.append(line[idx])
                if idx < rg : return h(idx+1)
                else: return ''
            else:
                #closing paranthesis
                closing = line[idx]
                #check the last item in cont to see if it matches this closing parenthesis
                if cont[-1] == ref[closing]:
                    cont.pop()
                    #print('Match')
                    if idx < rg : return h(idx+1)
                else:
                    #print(f'Faulty! {line[idx]}\nExpected {cont[-1]}')
                    return line[idx]
    return h(0)

err = []
for line in matrix:
    results = analyse(line)
    if results == '' or results == None:
        pass
    else : err.append(results)

print(err)
score = [points[i] for i in err]
total = sum(score)
print(f'Total score is: {total}')



#%%