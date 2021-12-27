#%%
with open('input.txt', 'r') as f:
    raw_data = f.read().split('\n\n')
    #print(raw_data)
def empty(x):
    return x != ''   
draw = raw_data[0].split(',')
#print(draw)
raw_boards = raw_data[1:]
boards = []
for brd in raw_boards:
    board = []
    rows = brd.split('\n')
    clean = [list(filter(empty,r.split(' '))) for r in rows]
    boards.append(clean)

#create a function that given a board with a list of columns, it returns a list of the boards rows
def createRows(board):
    r1, r2, r3, r4, r5 = [], [], [], [], []
    for col in board:
        r1.append(col[0])
        r2.append(col[1])
        r3.append(col[2])
        r4.append(col[3])
        r5.append(col[4])
    return [r1, r2, r3, r4, r5]

#create a function that checks a boards rows and columns to see if they contain the same number in draw
def checkBoard(board, draw):
    boardRows = createRows(board)
    boardCols = board
    def checkRow(boardRows, draw):
        for r in boardRows:
            rowCount = 0
            for num in r:
                if num in draw:
                    rowCount += 1
            if rowCount == 5:
                return {'found':True,
                        'in':'row',
                        'type':r}
        return {'found':False}
    def checkCol(boardCols, draw):
        for c in boardCols:
            colCount = 0
            for num in c:
                if num in draw:
                    colCount += 1
            if colCount == 5:
                return {'found':True,
                        'in':'col',
                        'type':c}
        return {'found':False}
    rowResult = checkRow(boardRows, draw)
    colResult = checkCol(boardCols, draw)
    if colResult['found'] and rowResult['found']:
        return {
            'found':True,
            'edgeCase':True,
            'obj1': {'found':True,
                'board':board,
                'in': 'col',
                'type':colResult['type'],
                'draw':draw},
            'obj2': {'found':True,
                'board':board,
                'in': 'row',
                'type':rowResult['type'],
                'draw':draw}
        }
    if colResult['found'] == True:
        return {'found':True,
                'edgeCase':False,
                'board':board,
                'in': 'col',
                'type':colResult['type'],
                'draw':draw}
    if rowResult['found'] == True:
        return {'found':True,
                'edgeCase':False,
                'board':board,
                'in': 'row',
                'type':rowResult['type'],
                'draw':draw}
    else:
        return {'found':False}
    
#create a function that increments the draw index by one number
def drawNumber(index):
    if index == len(draw)-1:
        pass
    else:
        return index+1
    
#create a function called play bingo that plays the game until it finds a winning board
def playBingo():
    drawIndex = 4 #start at the fifth number in the draw
    stop = False
    for d in range(len(draw)-4):
        for b in boards:
            result = checkBoard(b, draw[:drawIndex+1])
            if result['found'] == True:
                print('bingo!')
                print('board:', result['board'])
                print('in:', result['in'])
                print('type:', result['type'])
                print('draw:', draw[:drawIndex+1])
                print(f'Board Number: {boards.index(b)+1} of {len(boards)}')
                # drawIndex = drawNumber(drawIndex)
                stop = True
                return {
                    'board': result['board'],
                    'in': result['in'],
                    'type': result['type'],
                    'draw': draw[:drawIndex+1],
                }
        drawIndex = drawNumber(drawIndex)  
        if stop == True:
            break

#create a function that plays bingo until it finds the last winning board
def playBingo2():
    drawIndex = 4 #start at the fifth number in the draw
    winners = []
    won = False
    found = False
    removeBoard = False
    for d in range(len(draw)-4):
        for b in boards:
            result = checkBoard(b, draw[:drawIndex+1])
            if result['found'] and not result['edgeCase']:
                #stop = True
                found = True
                winners.append({
                    'board': result['board'],
                    'in': result['in'],
                    'type': result['type'],
                    'draw': result['draw'],
                })
                removeBoard = b
            elif result['found'] and result['edgeCase']:
                found = True
                winners.append({
                    'board': result['obj1']['board'],
                    'in': result['obj1']['in'],
                    'type': result['obj1']['type'],
                    'draw': result['obj1']['draw'],
                })
                winners.append({
                    'board': result['obj2']['board'],
                    'in': result['obj2']['in'],
                    'type': result['obj2']['type'],
                    'draw': result['obj2']['draw'],
                })
                removeBoard = b
        if found:
            print('Removing board:', removeBoard)
            print(f'Board Number: {boards.index(removeBoard)+1} of 100')
            boards.remove(removeBoard)
            print(f'Remaining boards: {len(boards)}')
            print(f'Remaining draws: {len(draw)-drawIndex-1}')
            found = False
        drawIndex = drawNumber(drawIndex)
    return winners[-1]
        
        

#resultData = playBingo()
resultData2 = playBingo2()
print(resultData2)

#create a function that sums the board numbers except the numbers in resultData['type'] and multiplies by resultData['draw'][-1] (the last number in the draw)
def part1(resultData):
    board = resultData['board']
   # type = resultData['type']
    d = resultData['draw']
    sum = 0
    for r in board:
        for n in r:
            if n not in d:
                sum += int(n)
    return sum*int(d[-1])

def part2(resultData):
    end = resultData
    #print(end)
    #print(resultData[-2])
    board = end['board']
    d = draw[:draw.index('41')+1]
    sum = 0
    for r in board:
        for n in r:
            if n not in d:
                #print(f'{n} not in {draw}')
                sum += int(n)
            #print(f'{n} in {draw}')
    return sum*int(d[-1])
    
#print(part1(resultData))
print(part1(resultData2))

            

#print(boards)
# %%
