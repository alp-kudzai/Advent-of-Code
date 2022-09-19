
#%%
with open('input.txt') as f:
    data = f.read().split('\n')
    matrix = [list(line) for line in data]

points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
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

auto_ref = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
}

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
                else: return cont
            else:
                #closing paranthesis
                closing = line[idx]
                #check the last item in cont to see if it matches this closing parenthesis
                if cont[-1] == ref[closing]:
                    cont.pop()
                    #print('Match')
                    if idx < rg : return h(idx+1)
                    else: return cont
                else:
                    #print(f'Faulty! {line[idx]}\nExpected {cont[-1]}')
                    return False
    return h(0)



auto_completed = []
total_points = []

def keep_score(chr):
    total_points = total_points*5
    total_points += points[chr]

for line in matrix:
    results = analyse(line)
    total_score = 0
    if results == False:
        pass
    else:
        rev_results = results[::-1]
        auto_line = [auto_ref[par] for par in rev_results]
        for chr in auto_line:
            total_score *= 5
            total_score += points[chr]
        total_points.append(total_score)
        #auto_completed.append(auto_line)
        #print(auto_line)

total_points.sort()
#get the middle point
idx = (len(total_points)-1)//2
print(total_points[idx])


#%%