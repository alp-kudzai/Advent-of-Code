#%%
with open('input.txt') as f:
    data = f.read().split('\n')
    matrix = [list(i) for i in data]

SIZE = 10

def sanitise(matrix):
    '''
    converts all the string into integers
    '''
    new_matrix = []
    for line in matrix:
        new_line = [int(num) for num in line]
        new_matrix.append(new_line)
    return new_matrix

matrix = sanitise(matrix)
# print(matrix)
# print('\n\n')

def get_neighbours(idx):
    '''
    Gets the neighbours of a cell given a matrix of 10*10 and the cell's index(x,y). Ir return a list of tuples with the neighbours coordinates
    '''
    x,y = idx
    l = (x,y-1)
    r = (x, y+1)
    u = (x-1,y)
    d = (x+1,y)
    ld = (x+1,y-1)
    lu = (x-1,y-1)
    rd = (x+1,y+1)
    ru = (x-1,y+1)
    neighbours = []
    
    for dir in [lu,u,ru,l,r,ld,d,rd]:
        if (-1 < dir[0] < SIZE) and (-1 < dir[1] < SIZE):
            neighbours.append((dir[0], dir[1]))

    return neighbours

#I just guessed, I noticed that the octopia had synced up by the 300 step.
# So I went backwards till all octopia were on 0 which was 296. I had i substracted 10 still I found the first de-synced moment which is before 276 there making 276 steps the first time it all synced up
STEPS = 276
Flashed_Total = []

def increase(level, step_flash):
    x,y = level
    octo = matrix[x][y]
    if (octo + 1) <= 9 and (level not in step_flash):
        matrix[x][y] = octo+1
    else:
        flash(level,step_flash)

def flash(idx,flashed):
    x,y = idx
    if idx not in flashed:
        matrix[x][y] = 0
        flashed.append(idx)
        neighbors = get_neighbours(idx)
        for n in neighbors:
            increase(n, flashed)
    
num_flashes = 0
while STEPS > 0:
    step_flashed = []
    for x in range(SIZE):
        for y in range(SIZE):
            increase((x,y), step_flashed)
    #print(f'\n{matrix}\n')
    num_flashes += len(step_flashed)
    Flashed_Total.append(step_flashed)
    STEPS -= 1


# def step(matrix):
#     for x in range(SIZE):
#         for y in range(SIZE):

print(matrix)
print(f'\n\n{num_flashes}')

#%%
